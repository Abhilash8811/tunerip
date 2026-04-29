// yt2mp3.lol frontend — talks to the FastAPI backend.
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

  var card = document.getElementById("converter");
  var variant = (card && card.getAttribute("data-variant")) || "single";
  var urlInput = document.getElementById("yt-url");
  var urlTextarea = document.getElementById("yt-url-multi");
  var pasteBtn = document.getElementById("paste-btn");
  var pasteBtnMulti = document.getElementById("paste-btn-multi");
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

  function wirePaste(btn, target, joinMulti) {
    if (!btn || !target) return;
    btn.addEventListener("click", function () {
      if (!navigator.clipboard || !navigator.clipboard.readText) { target.focus(); return; }
      navigator.clipboard.readText().then(function (text) {
        if (!text) return;
        if (joinMulti) {
          var existing = target.value.trim();
          target.value = (existing ? existing + "\n" : "") + text.trim();
        } else {
          target.value = text.trim();
        }
        target.focus();
      }).catch(function () { target.focus(); });
    });
  }
  wirePaste(pasteBtn, urlInput, false);
  wirePaste(pasteBtnMulti, urlTextarea, true);

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

  function convertOne(url, slot) {
    return fetch(API_BASE + "/api/convert", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: url, format: currentFormat, quality: qualitySel.value }),
    })
      .then(function (r) {
        if (!r.ok) return r.json().then(function (j) { throw new Error(j.detail || "Request failed"); });
        return r.json();
      })
      .then(function (j) {
        return new Promise(function (resolve) {
          var tries = 0;
          function tick() {
            tries++;
            fetch(API_BASE + "/api/status/" + encodeURIComponent(j.job_id))
              .then(function (r) { return r.json(); })
              .then(function (job) {
                slot(job);
                if (job.state === "done" || job.state === "error") { resolve(job); return; }
                if (tries > 600) { slot({ state: "error", error: "Timeout" }); resolve({ state: "error" }); return; }
                setTimeout(tick, 1500);
              })
              .catch(function () { slot({ state: "error", error: "Network error" }); resolve({ state: "error" }); });
          }
          tick();
        });
      });
  }

  function renderJobRow(urlStr, job) {
    var pct = Math.max(0, Math.min(100, Number(job.progress) || 0));
    var labels = { queued: "Queued…", downloading: "Downloading…", processing: "Encoding…", done: "Ready", error: "Failed" };
    var stateLabel = labels[job.state] || "Working…";
    var title = job.title ? escapeHtml(job.title) : escapeHtml(urlStr);
    var meta = [];
    if (job.duration) meta.push(fmtDuration(job.duration));
    if (job.size) meta.push(fmtBytes(job.size));
    var body = '<div class="status-meta"><span class="status-title">' + title + '</span><span>' + stateLabel + " · " + pct + "%</span>"
      + (meta.length ? "<span>" + meta.join(" · ") + "</span>" : "")
      + "</div>"
      + '<div class="progress"><div style="width:' + pct + '%"></div></div>';
    if (job.state === "done") {
      var dl = API_BASE + "/api/download/" + encodeURIComponent(job.id);
      body += '<div class="download-row"><a class="download-btn" href="' + dl + '" download>Download ' + (job.filename ? escapeHtml(job.filename) : "file") + "</a></div>";
    }
    if (job.state === "error") {
      body += '<div class="error">' + escapeHtml(job.error || "Conversion failed.") + "</div>";
    }
    return body;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (variant === "multi") {
      var raw = (urlTextarea.value || "").split(/\r?\n/).map(function (s) { return s.trim(); }).filter(Boolean);
      // dedupe
      var seen = {}; var urls = [];
      raw.forEach(function (u) { if (!seen[u]) { seen[u] = 1; urls.push(u); } });
      var valid = urls.filter(isYouTubeUrl);
      var invalid = urls.filter(function (u) { return !isYouTubeUrl(u); });
      if (!valid.length) {
        showStatus('<div class="error">Paste at least one valid YouTube URL (one per line).</div>');
        return;
      }
      convertBtn.disabled = true;
      var rowsState = valid.map(function (u) { return { url: u, html: renderJobRow(u, { state: "queued", progress: 0 }) }; });
      function flush() {
        var html = rowsState.map(function (r) { return '<div class="job-row">' + r.html + "</div>"; }).join("");
        if (invalid.length) html += '<div class="error">Skipped ' + invalid.length + ' non-YouTube line' + (invalid.length > 1 ? "s" : "") + ".</div>";
        showStatus(html);
      }
      flush();
      // Sequential to respect rate limits on free tier.
      var p = Promise.resolve();
      valid.forEach(function (u, idx) {
        p = p.then(function () {
          return convertOne(u, function (job) {
            rowsState[idx].html = renderJobRow(u, job);
            flush();
          });
        });
      });
      p.then(function () { convertBtn.disabled = false; });
      return;
    }

    var url = (urlInput.value || "").trim();
    if (!isYouTubeUrl(url)) {
      showStatus('<div class="error">Please paste a valid YouTube link (youtube.com or youtu.be).</div>');
      return;
    }
    convertBtn.disabled = true;
    showStatus('<div class="status-meta"><span>Starting…</span></div><div class="progress"><div style="width:5%"></div></div>');

    convertOne(url, renderProgress).then(function () { convertBtn.disabled = false; });
  });
})();
