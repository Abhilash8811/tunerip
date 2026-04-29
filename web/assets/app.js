// TuneRip frontend — talks to the FastAPI backend.
(function () {
  "use strict";

  // Configure the API base in one place. Overridden by ?api= for testing.
  var API_BASE = (function () {
    var m = location.search.match(/[?&]api=([^&]+)/);
    if (m) return decodeURIComponent(m[1]).replace(/\/+$/, "");
    if (window.__API_BASE__) return String(window.__API_BASE__).replace(/\/+$/, "");
    // Fallback: same-origin /api proxy (useful for local dev).
    return "";
  })();

  var AUDIO_FORMATS = ["mp3", "m4a", "wav", "ogg", "opus"];
  var AUDIO_BITRATES = [
    { v: "128", l: "128 kbps" },
    { v: "192", l: "192 kbps" },
    { v: "256", l: "256 kbps" },
    { v: "320", l: "320 kbps" },
  ];
  var VIDEO_HEIGHTS = [
    { v: "360", l: "360p" },
    { v: "480", l: "480p" },
    { v: "720", l: "720p" },
    { v: "1080", l: "1080p" },
    { v: "1440", l: "1440p QHD" },
    { v: "2160", l: "2160p 4K" },
  ];

  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  var form = document.getElementById("convert-form");
  if (!form) return;

  var urlInput = document.getElementById("yt-url");
  var pasteBtn = document.getElementById("paste-btn");
  var qualitySel = document.getElementById("quality");
  var convertBtn = document.getElementById("convert-btn");
  var tabs = Array.prototype.slice.call(document.querySelectorAll(".tab"));
  var statusBox = document.getElementById("status");

  var currentFormat = (window.__DEFAULT_FORMAT__ || "mp3");
  var defaultQuality = (window.__DEFAULT_QUALITY__ || "320");

  // Pre-select the requested format tab if the page overrides it.
  tabs.forEach(function (t) {
    var isActive = t.getAttribute("data-format") === currentFormat;
    t.classList.toggle("active", isActive);
    t.setAttribute("aria-selected", isActive ? "true" : "false");
  });

  function renderQualityOptions() {
    var opts = AUDIO_FORMATS.indexOf(currentFormat) >= 0 ? AUDIO_BITRATES : VIDEO_HEIGHTS;
    var prev = qualitySel.value;
    qualitySel.innerHTML = "";
    opts.forEach(function (o) {
      var el = document.createElement("option");
      el.value = o.v;
      el.textContent = o.l;
      if (o.v === prev || (!prev && o.v === defaultQuality)) el.selected = true;
      qualitySel.appendChild(el);
    });
    if (!qualitySel.value) {
      qualitySel.value = currentFormat === "mp4" ? "1080" : "320";
    }
  }
  renderQualityOptions();

  tabs.forEach(function (t) {
    t.addEventListener("click", function () {
      tabs.forEach(function (x) {
        x.classList.remove("active");
        x.setAttribute("aria-selected", "false");
      });
      t.classList.add("active");
      t.setAttribute("aria-selected", "true");
      currentFormat = t.getAttribute("data-format");
      renderQualityOptions();
    });
  });

  if (pasteBtn) {
    pasteBtn.addEventListener("click", function () {
      if (!navigator.clipboard || !navigator.clipboard.readText) {
        urlInput.focus();
        return;
      }
      navigator.clipboard.readText().then(function (text) {
        if (text) {
          urlInput.value = text.trim();
          urlInput.focus();
        }
      }).catch(function () { urlInput.focus(); });
    });
  }

  function isYouTubeUrl(u) {
    try {
      var url = new URL(u);
      var h = url.hostname.replace(/^www\.|^m\.|^music\./, "");
      return h === "youtube.com" || h === "youtu.be" || h === "youtube-nocookie.com";
    } catch (e) { return false; }
  }

  function showStatus(html) {
    statusBox.innerHTML = html;
    statusBox.classList.remove("hidden");
  }

  function fmtBytes(b) {
    if (!b) return "";
    var units = ["B", "KB", "MB", "GB"];
    var i = 0;
    while (b >= 1024 && i < units.length - 1) { b /= 1024; i++; }
    return b.toFixed(b >= 10 ? 0 : 1) + " " + units[i];
  }

  function fmtDuration(s) {
    if (!s) return "";
    s = Math.floor(s);
    var h = Math.floor(s / 3600);
    var m = Math.floor((s % 3600) / 60);
    var sec = s % 60;
    var pad = function (n) { return (n < 10 ? "0" : "") + n; };
    return (h ? h + ":" : "") + pad(m) + ":" + pad(sec);
  }

  function renderProgress(job) {
    var pct = Math.max(0, Math.min(100, Number(job.progress) || 0));
    var stateLabel = ({
      queued: "Queued…",
      downloading: "Downloading from YouTube…",
      processing: "Converting with FFmpeg…",
      done: "Ready",
      error: "Failed",
    })[job.state] || "Working…";
    var thumb = job.thumbnail ? '<img alt="" src="' + job.thumbnail + '" />' : "";
    var title = job.title ? '<span class="status-title">' + escapeHtml(job.title) + "</span>" : "";
    var meta = [];
    if (job.duration) meta.push(fmtDuration(job.duration));
    if (job.size) meta.push(fmtBytes(job.size));
    var html = ""
      + '<div class="status-meta">' + thumb + title + '<span>' + stateLabel + " · " + pct + "%</span>"
      + (meta.length ? "<span>" + meta.join(" · ") + "</span>" : "")
      + "</div>"
      + '<div class="progress"><div style="width:' + pct + '%"></div></div>';
    if (job.state === "done") {
      var dl = API_BASE + "/api/download/" + encodeURIComponent(job.id);
      html += '<div class="download-row"><a class="download-btn" href="' + dl + '" download>Download ' + (job.filename ? escapeHtml(job.filename) : "file") + "</a></div>";
    }
    if (job.state === "error") {
      html += '<div class="error">' + escapeHtml(job.error || "Conversion failed. Try again or pick a different quality.") + "</div>";
    }
    showStatus(html);
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c];
    });
  }

  function pollStatus(jobId) {
    var tries = 0;
    function tick() {
      tries++;
      fetch(API_BASE + "/api/status/" + encodeURIComponent(jobId))
        .then(function (r) { return r.json(); })
        .then(function (job) {
          renderProgress(job);
          if (job.state === "done" || job.state === "error") {
            convertBtn.disabled = false;
            return;
          }
          if (tries > 600) {
            showStatus('<div class="error">Conversion is taking too long. Please retry.</div>');
            convertBtn.disabled = false;
            return;
          }
          setTimeout(tick, 1500);
        })
        .catch(function () {
          showStatus('<div class="error">Network error while checking status. Please retry.</div>');
          convertBtn.disabled = false;
        });
    }
    tick();
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var url = (urlInput.value || "").trim();
    if (!isYouTubeUrl(url)) {
      showStatus('<div class="error">Please paste a valid YouTube link (youtube.com or youtu.be).</div>');
      return;
    }
    convertBtn.disabled = true;
    showStatus('<div class="status-meta"><span>Starting…</span></div><div class="progress"><div style="width:5%"></div></div>');

    fetch(API_BASE + "/api/convert", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        url: url,
        format: currentFormat,
        quality: qualitySel.value,
      }),
    })
      .then(function (r) {
        if (!r.ok) return r.json().then(function (j) { throw new Error(j.detail || "Request failed"); });
        return r.json();
      })
      .then(function (j) { pollStatus(j.job_id); })
      .catch(function (err) {
        showStatus('<div class="error">' + escapeHtml(err.message || "Failed to start conversion.") + "</div>");
        convertBtn.disabled = false;
      });
  });
})();
