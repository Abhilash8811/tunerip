// ytmp3.pro frontend — talks to the FastAPI backend.
(function () {
  "use strict";

  var API_BASE = (function () {
    var m = location.search.match(/[?&]api=([^&]+)/);
    if (m) return decodeURIComponent(m[1]).replace(/\/+$/, "");
    if (window.__API_BASE__) return String(window.__API_BASE__).replace(/\/+$/, "");
    return "https://ytmp3-api-2cas.onrender.com";
  })();

  var AUDIO_FORMATS = ["mp3", "m4a", "wav", "ogg", "opus"];
  var AUDIO_BITRATES = [
    { v: "128", l: "MP3 - 128 kbps" },
    { v: "192", l: "MP3 - 192 kbps" },
    { v: "256", l: "MP3 - 256 kbps" },
    { v: "320", l: "MP3 - 320 kbps" },
  ];
  var VIDEO_HEIGHTS = [
    { v: "360", l: "MP4 - 360p" },
    { v: "480", l: "MP4 - 480p" },
    { v: "720", l: "MP4 - 720p" },
    { v: "1080", l: "MP4 - 1080p" },
    { v: "1440", l: "MP4 - 1440p QHD" },
    { v: "2160", l: "MP4 - 2160p 4K" },
  ];

  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  // Theme toggle
  var themeBtn = document.getElementById("theme-toggle");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var current = document.documentElement.getAttribute("data-theme");
      var next = current === "light" ? "dark" : "light";
      document.documentElement.setAttribute("data-theme", next);
      try { localStorage.setItem("tr-theme", next); } catch (e) {}
    });
  }

  // Close native <details> dropdowns when clicking outside.
  document.addEventListener("click", function (e) {
    document.querySelectorAll("details[open]").forEach(function (d) {
      if (!d.contains(e.target)) d.removeAttribute("open");
    });
  });

  var form = document.getElementById("convert-form");
  if (!form) return;

  var urlInput = document.getElementById("yt-url");
  var pasteBtn = document.getElementById("paste-btn");
  var qualitySel = document.getElementById("quality");
  var convertBtn = document.getElementById("convert-btn");
  var segBtns = Array.prototype.slice.call(document.querySelectorAll(".seg-btn"));
  var statusBox = document.getElementById("status");

  var currentFormat = (window.__DEFAULT_FORMAT__ || "mp3");
  var defaultQuality = (window.__DEFAULT_QUALITY__ || "320");

  segBtns.forEach(function (t) {
    var isActive = t.getAttribute("data-format") === currentFormat;
    t.classList.toggle("active", isActive);
    t.setAttribute("aria-selected", isActive ? "true" : "false");
  });

  function renderQualityOptions() {
    var opts = currentFormat === "mp4" ? VIDEO_HEIGHTS : AUDIO_BITRATES;
    var prev = qualitySel.value;
    qualitySel.innerHTML = "";
    opts.forEach(function (o) {
      var el = document.createElement("option");
      el.value = o.v;
      el.textContent = o.l;
      if (o.v === prev || (!prev && o.v === defaultQuality)) el.selected = true;
      qualitySel.appendChild(el);
    });
    if (!qualitySel.value) qualitySel.value = currentFormat === "mp4" ? "1080" : "320";
  }
  renderQualityOptions();

  segBtns.forEach(function (t) {
    t.addEventListener("click", function () {
      segBtns.forEach(function (x) {
        x.classList.remove("active");
        x.setAttribute("aria-selected", "false");
      });
      t.classList.add("active");
      t.setAttribute("aria-selected", "true");
      currentFormat = t.getAttribute("data-format");
      renderQualityOptions();
    });
  });

  var trackLabel = document.getElementById("track-label");
  var trackSearch = document.getElementById("track-search");
  var trackBtns = Array.prototype.slice.call(document.querySelectorAll(".track-opt"));
  var currentTrack = "";

  trackBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      currentTrack = btn.getAttribute("data-track") || "";
      if (trackLabel) trackLabel.textContent = btn.textContent;
      var details = btn.closest("details");
      if (details) details.removeAttribute("open");
    });
  });

  if (trackSearch) {
    trackSearch.addEventListener("input", function (e) {
      var term = (e.target.value || "").toLowerCase();
      trackBtns.forEach(function (btn) {
        if (btn.textContent.toLowerCase().indexOf(term) > -1) {
          btn.style.display = "";
        } else {
          btn.style.display = "none";
        }
      });
    });
  }

  if (pasteBtn) {
    pasteBtn.addEventListener("click", function () {
      if (!navigator.clipboard || !navigator.clipboard.readText) {
        urlInput.focus();
        return;
      }
      navigator.clipboard.readText().then(function (text) {
        if (text) { urlInput.value = text.trim(); urlInput.focus(); }
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
    var u = ["B","KB","MB","GB"], i = 0;
    while (b >= 1024 && i < u.length - 1) { b /= 1024; i++; }
    return b.toFixed(b >= 10 ? 0 : 1) + " " + u[i];
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

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c];
    });
  }

  function renderProgress(job) {
    var pct = Math.max(0, Math.min(100, Number(job.progress) || 0));
    var labels = { queued: "Queued…", downloading: "Downloading from YouTube…", processing: "Converting with FFmpeg…", done: "Ready", error: "Failed" };
    var stateLabel = labels[job.state] || "Working…";
    var thumb = job.thumbnail ? '<img alt="" src="' + escapeHtml(job.thumbnail) + '" loading="lazy" />' : "";
    var title = job.title ? '<span class="status-title">' + escapeHtml(job.title) + "</span>" : "";
    var meta = [];
    if (job.duration) meta.push(fmtDuration(job.duration));
    if (job.size) meta.push(fmtBytes(job.size));
    var html =
      '<div class="status-meta">' + thumb + title + '<span>' + stateLabel + " · " + pct + "%</span>"
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

  function pollStatus(jobId) {
    var tries = 0;
    function tick() {
      tries++;
      fetch(API_BASE + "/api/status/" + encodeURIComponent(jobId))
        .then(function (r) { return r.json(); })
        .then(function (job) {
          renderProgress(job);
          if (job.state === "done" || job.state === "error") {
            convertBtn.disabled = false; return;
          }
          if (tries > 600) {
            showStatus('<div class="error">Conversion is taking too long. Please retry.</div>');
            convertBtn.disabled = false; return;
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
      if (url.length > 0 && !url.match(/^https?:\/\//i)) {
        url = "ytsearch1:" + url;
      } else {
        showStatus('<div class="error">Please paste a valid YouTube link (youtube.com or youtu.be) or enter a search keyword.</div>');
        return;
      }
    }
    convertBtn.disabled = true;
    showStatus('<div class="status-meta"><span>Starting…</span></div><div class="progress"><div style="width:5%"></div></div>');

    fetch(API_BASE + "/api/convert", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: url, format: currentFormat, quality: qualitySel.value }),
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
