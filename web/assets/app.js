// ytmp3.pro frontend — talks to the FastAPI backend.
(function () {
  "use strict";

  var API_BASE = (function () {
    var m = location.search.match(/[?&]api=([^&]+)/);
    if (m) return decodeURIComponent(m[1]).replace(/\/+$/, "");
    if (window.__API_BASE__) return String(window.__API_BASE__).replace(/\/+$/, "");
    return "https://api.yt2mp3.lol";
  })();

  var AUDIO_FORMATS = ["mp3", "m4a", "wav", "ogg", "opus", "flac"];
  var AUDIO_BITRATES = [
    { v: "320", l: "MP3 - 320kbps" },
    { v: "256", l: "MP3 - 256kbps" },
    { v: "192", l: "MP3 - 192kbps" },
    { v: "128", l: "MP3 - 128kbps" },
    { v: "64", l: "MP3 - 64kbps" },
    { v: "wav", l: "WAV" },
    { v: "flac", l: "FLAC" },
    { v: "m4a", l: "M4A" },
    { v: "ogg", l: "OGG" },
    { v: "opus", l: "Opus" }
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

  // Supporter button interaction
  var supporterBtn = document.querySelector(".btn-supporter");
  if (supporterBtn) {
    supporterBtn.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();
      // Create modal overlay
      var modal = document.createElement("div");
      modal.className = "supporter-modal";
      modal.innerHTML = 
        '<div class="supporter-modal-content">' +
          '<button class="supporter-modal-close" aria-label="Close">&times;</button>' +
          '<div class="supporter-modal-header">' +
            '<svg width="48" height="48" viewBox="0 0 24 24" fill="none" style="color:var(--accent)">' +
              '<path d="M12 2l2.5 6L21 9l-5 4.5L17.5 20 12 16.8 6.5 20 8 13.5 3 9l6.5-1L12 2z" fill="currentColor"/>' +
            '</svg>' +
            '<h2>Support yt2mp3.lol</h2>' +
          '</div>' +
          '<div class="supporter-modal-body">' +
            '<p>Thank you for using our free YouTube converter! Your support helps us keep this service running.</p>' +
            '<div class="supporter-options">' +
              '<div class="supporter-option">' +
                '<h3>🌟 Share with Friends</h3>' +
                '<p>Help others discover our free converter by sharing it on social media.</p>' +
                '<div class="share-buttons">' +
                  '<button class="share-btn" data-platform="twitter" title="Share on Twitter">' +
                    '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"/></svg>' +
                  '</button>' +
                  '<button class="share-btn" data-platform="facebook" title="Share on Facebook">' +
                    '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg>' +
                  '</button>' +
                  '<button class="share-btn" data-platform="whatsapp" title="Share on WhatsApp">' +
                    '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>' +
                  '</button>' +
                  '<button class="share-btn" data-platform="copy" title="Copy Link">' +
                    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71"/></svg>' +
                  '</button>' +
                '</div>' +
              '</div>' +
              '<div class="supporter-option">' +
                '<h3>⭐ Rate Us</h3>' +
                '<p>Leave a review or rating to help others find us.</p>' +
                '<div class="rating-stars">' +
                  '<button class="star-btn" data-rating="1">★</button>' +
                  '<button class="star-btn" data-rating="2">★</button>' +
                  '<button class="star-btn" data-rating="3">★</button>' +
                  '<button class="star-btn" data-rating="4">★</button>' +
                  '<button class="star-btn" data-rating="5">★</button>' +
                '</div>' +
                '<p class="rating-thanks" style="display:none;color:var(--success);margin-top:8px;">Thank you for your rating! 🎉</p>' +
              '</div>' +
              '<div class="supporter-option">' +
                '<h3>💬 Feedback</h3>' +
                '<p>Have suggestions? Let us know how we can improve!</p>' +
                '<textarea class="feedback-textarea" placeholder="Your feedback..." rows="3"></textarea>' +
                '<button class="feedback-submit-btn">Send Feedback</button>' +
                '<p class="feedback-thanks" style="display:none;color:var(--success);margin-top:8px;">Thank you for your feedback! 🙏</p>' +
              '</div>' +
            '</div>' +
          '</div>' +
        '</div>';
      
      document.body.appendChild(modal);
      document.body.style.overflow = "hidden";
      
      // Close modal function
      function closeModal() {
        document.body.removeChild(modal);
        document.body.style.overflow = "";
      }
      
      // Close button
      modal.querySelector(".supporter-modal-close").addEventListener("click", closeModal);
      
      // Click outside to close
      modal.addEventListener("click", function(e) {
        if (e.target === modal) closeModal();
      });
      
      // Share buttons
      var shareButtons = modal.querySelectorAll(".share-btn");
      shareButtons.forEach(function(btn) {
        btn.addEventListener("click", function() {
          var platform = btn.getAttribute("data-platform");
          var url = encodeURIComponent(window.location.origin);
          var text = encodeURIComponent("Check out this free YouTube to MP3 converter!");
          
          if (platform === "twitter") {
            window.open("https://twitter.com/intent/tweet?text=" + text + "&url=" + url, "_blank");
          } else if (platform === "facebook") {
            window.open("https://www.facebook.com/sharer/sharer.php?u=" + url, "_blank");
          } else if (platform === "whatsapp") {
            window.open("https://wa.me/?text=" + text + " " + url, "_blank");
          } else if (platform === "copy") {
            if (navigator.clipboard) {
              navigator.clipboard.writeText(window.location.origin).then(function() {
                btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>';
                setTimeout(function() {
                  btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71"/></svg>';
                }, 2000);
              });
            }
          }
        });
      });
      
      // Rating stars
      var starButtons = modal.querySelectorAll(".star-btn");
      var ratingThanks = modal.querySelector(".rating-thanks");
      starButtons.forEach(function(btn, index) {
        btn.addEventListener("click", function() {
          var rating = btn.getAttribute("data-rating");
          // Highlight stars up to clicked one
          starButtons.forEach(function(s, i) {
            s.style.color = i < index + 1 ? "gold" : "var(--muted)";
          });
          ratingThanks.style.display = "block";
          // Track rating (you can send to analytics)
          console.log("User rated:", rating, "stars");
        });
        
        // Hover effect
        btn.addEventListener("mouseenter", function() {
          starButtons.forEach(function(s, i) {
            s.style.color = i <= index ? "gold" : "var(--muted)";
          });
        });
      });
      
      var ratingContainer = modal.querySelector(".rating-stars");
      ratingContainer.addEventListener("mouseleave", function() {
        var rated = Array.from(starButtons).some(function(s) { return s.style.color === "gold"; });
        if (!rated) {
          starButtons.forEach(function(s) { s.style.color = "var(--muted)"; });
        }
      });
      
      // Feedback submission
      var feedbackBtn = modal.querySelector(".feedback-submit-btn");
      var feedbackTextarea = modal.querySelector(".feedback-textarea");
      var feedbackThanks = modal.querySelector(".feedback-thanks");
      
      feedbackBtn.addEventListener("click", function() {
        var feedback = feedbackTextarea.value.trim();
        if (feedback) {
          // You can send this to your backend
          console.log("User feedback:", feedback);
          feedbackTextarea.value = "";
          feedbackThanks.style.display = "block";
          setTimeout(function() {
            feedbackThanks.style.display = "none";
          }, 3000);
        }
      });
    });
  }

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
    var labels = { queued: "Queued…", downloading: "Downloading from YouTube…", processing: "Processing…", done: "Ready", error: "Failed" };
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

  function renderSearchResults(results) {
    var html = '<div class="search-results-grid">';
    results.forEach(function (item) {
      var dur = fmtDuration(item.duration);
      html += 
        '<div class="search-item" onclick="window.__START_CONVERSION__(\'' + escapeHtml(item.url) + '\')">' +
          '<div class="search-thumb">' +
            '<img src="' + escapeHtml(item.thumbnail) + '" loading="lazy">' +
            '<span class="search-duration">' + dur + '</span>' +
          '</div>' +
          '<div class="search-info">' +
            '<div class="search-title">' + escapeHtml(item.title) + '</div>' +
            '<div class="search-uploader">' + escapeHtml(item.uploader || "") + '</div>' +
          '</div>' +
        '</div>';
    });
    html += '</div>';
    showStatus(html);
  }

  window.__START_CONVERSION__ = function(url) {
    urlInput.value = url;
    form.dispatchEvent(new Event("submit"));
  };

  // Playlist state management
  var playlistState = {
    items: [],
    convertQueue: [],
    downloadQueue: []
  };

  function startJob(url, fmt, qual, itemId) {
    // Create a container for this specific job
    var jobEl = document.createElement("div");
    jobEl.className = "status-job";
    jobEl.innerHTML = '<div class="status-meta"><span>Starting ' + escapeHtml(url.substring(0, 30)) + '...</span></div>';
    statusBox.appendChild(jobEl);

    function updateJobStatus(html) {
      jobEl.innerHTML = html;
    }

    function pollJobStatus(jobId) {
      var tries = 0;
      function tick() {
        tries++;
        fetch(API_BASE + "/api/status/" + encodeURIComponent(jobId))
          .then(function (r) { return r.json(); })
          .then(function (job) {
            var pct = Math.max(0, Math.min(100, Number(job.progress) || 0));
            var labels = { queued: "Queued…", downloading: "Downloading…", processing: "Processing…", done: "Ready", error: "Failed" };
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
              html += '<div class="download-row"><a class="download-btn" href="' + dl + '" download>Download</a></div>';
              updateJobStatus(html);
              
              // Move to download tab if this is a playlist item
              if (itemId) {
                var item = playlistState.items.find(function(i) { return i.id === itemId; });
                if (item) {
                  item.state = "done";
                  item.downloadUrl = dl;
                  item.filename = job.filename;
                  updatePlaylistUI();
                }
              }
              return;
            }
            if (job.state === "error") {
              html += '<div class="error">' + escapeHtml(job.error || "Failed") + "</div>";
              updateJobStatus(html);
              
              if (itemId) {
                var item = playlistState.items.find(function(i) { return i.id === itemId; });
                if (item) {
                  item.state = "error";
                  item.error = job.error;
                  updatePlaylistUI();
                }
              }
              return;
            }
            updateJobStatus(html);
            
            // Update playlist item progress
            if (itemId) {
              var item = playlistState.items.find(function(i) { return i.id === itemId; });
              if (item) {
                item.progress = pct;
                item.state = job.state;
                updatePlaylistUI();
              }
            }
            
            if (tries < 600) setTimeout(tick, 1500);
          })
          .catch(function () {
            updateJobStatus('<div class="error">Network error</div>');
          });
      }
      tick();
    }

    fetch(API_BASE + "/api/convert", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: url, format: fmt, quality: qual }),
    })
      .then(function (r) { return r.json(); })
      .then(function (j) { 
        if (itemId) {
          var item = playlistState.items.find(function(i) { return i.id === itemId; });
          if (item) {
            item.jobId = j.job_id;
            item.state = "converting";
          }
        }
        pollJobStatus(j.job_id); 
      })
      .catch(function (err) {
        updateJobStatus('<div class="error">' + escapeHtml(err.message) + '</div>');
      });
  }

  function renderPlaylistUI(playlistData, playlistTitle) {
    playlistState.items = playlistData.map(function(item, idx) {
      return {
        id: "pl-" + idx + "-" + Date.now(),
        url: item.url,
        title: item.title,
        thumbnail: item.thumbnail,
        uploader: item.uploader,
        duration: item.duration,
        format: currentFormat,
        quality: qualitySel.value,
        track: currentTrack,
        state: "pending",
        selected: false,
        progress: 0
      };
    });

    var html = '<div class="playlist-container">';
    
    // Playlist header
    html += '<div class="playlist-header">';
    html += '<button type="button" class="playlist-toggle" onclick="window.__togglePlaylist__()">';
    html += '<svg width="12" height="12" viewBox="0 0 12 12" class="playlist-arrow"><path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    html += '<span class="playlist-title">' + escapeHtml(playlistTitle || "Playlist") + ' (' + playlistData.length + ' items)</span>';
    html += '</button>';
    html += '<div class="playlist-header-actions">';
    html += '<button type="button" class="tab-btn active" data-tab="convert">Convert Tab (<span id="convert-count">' + playlistData.length + '</span>)</button>';
    html += '<button type="button" class="tab-btn" data-tab="download">Download Tab (<span id="download-count">0</span>)</button>';
    html += '</div>';
    html += '</div>';

    // Playlist body
    html += '<div class="playlist-body">';
    
    // Convert tab
    html += '<div class="playlist-tab active" data-tab="convert">';
    html += '<div class="playlist-controls">';
    html += '<label class="checkbox-label"><input type="checkbox" id="select-all-checkbox"> <span id="selected-count">0 selected</span></label>';
    html += '<button type="button" class="btn-convert-selected" id="convert-selected-btn" disabled>Convert selected (0)</button>';
    html += '</div>';
    html += '<div class="playlist-items" id="playlist-items-convert"></div>';
    html += '</div>';
    
    // Download tab
    html += '<div class="playlist-tab" data-tab="download">';
    html += '<div class="playlist-items" id="playlist-items-download"></div>';
    html += '</div>';
    
    html += '</div>';
    html += '</div>';

    showStatus(html);
    
    // Attach event listeners
    attachPlaylistEventListeners();
    updatePlaylistUI();
  }

  function attachPlaylistEventListeners() {
    // Tab switching
    var tabBtns = document.querySelectorAll(".tab-btn");
    tabBtns.forEach(function(btn) {
      btn.addEventListener("click", function() {
        var tab = btn.getAttribute("data-tab");
        tabBtns.forEach(function(b) { b.classList.remove("active"); });
        btn.classList.add("active");
        
        var tabs = document.querySelectorAll(".playlist-tab");
        tabs.forEach(function(t) {
          t.classList.toggle("active", t.getAttribute("data-tab") === tab);
        });
      });
    });

    // Select all checkbox
    var selectAllCheckbox = document.getElementById("select-all-checkbox");
    if (selectAllCheckbox) {
      selectAllCheckbox.addEventListener("change", function() {
        var checked = this.checked;
        playlistState.items.forEach(function(item) {
          if (item.state === "pending") {
            item.selected = checked;
          }
        });
        updatePlaylistUI();
      });
    }

    // Convert selected button
    var convertSelectedBtn = document.getElementById("convert-selected-btn");
    if (convertSelectedBtn) {
      convertSelectedBtn.addEventListener("click", function() {
        var selectedItems = playlistState.items.filter(function(item) {
          return item.selected && item.state === "pending";
        });
        
        selectedItems.forEach(function(item) {
          var qual = item.quality;
          var fmt = item.format;
          if (["wav", "flac", "m4a", "ogg", "opus"].indexOf(qual) !== -1) {
            fmt = qual;
            qual = "320";
          }
          startJob(item.url, fmt, qual, item.id);
        });
      });
    }
  }

  function updatePlaylistUI() {
    var convertContainer = document.getElementById("playlist-items-convert");
    var downloadContainer = document.getElementById("playlist-items-download");
    
    if (!convertContainer || !downloadContainer) return;

    var pendingItems = playlistState.items.filter(function(i) { return i.state === "pending"; });
    var convertingItems = playlistState.items.filter(function(i) { return i.state === "converting" || i.state === "queued" || i.state === "downloading" || i.state === "processing"; });
    var doneItems = playlistState.items.filter(function(i) { return i.state === "done"; });
    var errorItems = playlistState.items.filter(function(i) { return i.state === "error"; });

    // Update counts
    var convertCount = document.getElementById("convert-count");
    var downloadCount = document.getElementById("download-count");
    if (convertCount) convertCount.textContent = pendingItems.length + convertingItems.length + errorItems.length;
    if (downloadCount) downloadCount.textContent = doneItems.length;

    // Render convert tab items
    var convertHtml = "";
    pendingItems.concat(convertingItems).concat(errorItems).forEach(function(item) {
      convertHtml += renderPlaylistItem(item, "convert");
    });
    convertContainer.innerHTML = convertHtml;

    // Render download tab items
    var downloadHtml = "";
    doneItems.forEach(function(item) {
      downloadHtml += renderPlaylistItem(item, "download");
    });
    if (downloadHtml === "") {
      downloadHtml = '<div class="empty-state">No downloads yet. Convert videos to see them here.</div>';
    }
    downloadContainer.innerHTML = downloadHtml;

    // Update selected count
    var selectedCount = playlistState.items.filter(function(i) { return i.selected && i.state === "pending"; }).length;
    var selectedCountEl = document.getElementById("selected-count");
    if (selectedCountEl) selectedCountEl.textContent = selectedCount + " selected";

    // Update convert selected button
    var convertSelectedBtn = document.getElementById("convert-selected-btn");
    if (convertSelectedBtn) {
      convertSelectedBtn.disabled = selectedCount === 0;
      convertSelectedBtn.textContent = "Convert selected (" + selectedCount + ")";
    }

    // Update select all checkbox
    var selectAllCheckbox = document.getElementById("select-all-checkbox");
    if (selectAllCheckbox) {
      var allSelected = pendingItems.length > 0 && pendingItems.every(function(i) { return i.selected; });
      selectAllCheckbox.checked = allSelected;
    }

    // Re-attach item event listeners
    attachItemEventListeners();
  }

  function renderPlaylistItem(item, context) {
    var html = '<div class="playlist-item" data-id="' + item.id + '">';
    
    if (context === "convert" && item.state === "pending") {
      html += '<label class="item-checkbox"><input type="checkbox" class="item-select" data-id="' + item.id + '" ' + (item.selected ? "checked" : "") + '></label>';
    } else {
      html += '<div class="item-checkbox-placeholder"></div>';
    }
    
    html += '<div class="item-thumbnail">';
    if (item.thumbnail) {
      html += '<img src="' + escapeHtml(item.thumbnail) + '" alt="" loading="lazy">';
    }
    if (item.duration) {
      html += '<span class="item-duration">' + fmtDuration(item.duration) + '</span>';
    }
    html += '</div>';
    
    html += '<div class="item-info">';
    html += '<div class="item-title">' + escapeHtml(item.title) + '</div>';
    if (item.uploader) {
      html += '<div class="item-uploader">' + escapeHtml(item.uploader) + '</div>';
    }
    html += '</div>';

    if (item.state === "pending") {
      // Show format controls
      html += '<select class="item-select-small item-track" data-id="' + item.id + '">';
      html += '<option value="">Origin</option>';
      html += '<option value="en">English</option>';
      html += '<option value="hi">Hindi</option>';
      html += '<option value="es">Spanish</option>';
      html += '<option value="fr">French</option>';
      html += '<option value="de">German</option>';
      html += '<option value="ja">Japanese</option>';
      html += '<option value="ko">Korean</option>';
      html += '</select>';

      html += '<select class="item-select-small item-format" data-id="' + item.id + '">';
      html += '<option value="mp3"' + (item.format === "mp3" ? " selected" : "") + '>MP3</option>';
      html += '<option value="mp4"' + (item.format === "mp4" ? " selected" : "") + '>MP4</option>';
      html += '</select>';

      var qualities = item.format === "mp4" ? VIDEO_HEIGHTS : AUDIO_BITRATES;
      html += '<select class="item-select-small item-quality" data-id="' + item.id + '">';
      qualities.forEach(function(q) {
        html += '<option value="' + q.v + '"' + (item.quality === q.v ? " selected" : "") + '>' + q.l + '</option>';
      });
      html += '</select>';

      html += '<button type="button" class="item-delete" data-id="' + item.id + '" title="Remove">';
      html += '<svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M3 6h18M8 6V4h8v2M10 11v6M14 11v6M5 6l1 14h12l1-14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>';
      html += '</button>';
    } else if (item.state === "converting" || item.state === "queued" || item.state === "downloading" || item.state === "processing") {
      html += '<div class="item-progress-container">';
      html += '<div class="item-progress-bar"><div style="width:' + item.progress + '%"></div></div>';
      html += '<span class="item-progress-text">' + item.progress + '%</span>';
      html += '</div>';
    } else if (item.state === "done") {
      html += '<a class="item-download-btn" href="' + item.downloadUrl + '" download>Download</a>';
    } else if (item.state === "error") {
      html += '<span class="item-error">Failed</span>';
      html += '<button type="button" class="item-retry" data-id="' + item.id + '">Retry</button>';
    }

    html += '</div>';
    return html;
  }

  function attachItemEventListeners() {
    // Item checkboxes
    var checkboxes = document.querySelectorAll(".item-select");
    checkboxes.forEach(function(cb) {
      cb.addEventListener("change", function() {
        var id = cb.getAttribute("data-id");
        var item = playlistState.items.find(function(i) { return i.id === id; });
        if (item) {
          item.selected = cb.checked;
          updatePlaylistUI();
        }
      });
    });

    // Format selectors
    var formatSelects = document.querySelectorAll(".item-format");
    formatSelects.forEach(function(sel) {
      sel.addEventListener("change", function() {
        var id = sel.getAttribute("data-id");
        var item = playlistState.items.find(function(i) { return i.id === id; });
        if (item) {
          item.format = sel.value;
          // Reset quality to default when format changes
          if (sel.value === "mp4") {
            item.quality = "1080"; // Default video quality
          } else {
            item.quality = "320"; // Default audio quality
          }
          // Update quality options
          updatePlaylistUI();
        }
      });
    });

    // Quality selectors
    var qualitySelects = document.querySelectorAll(".item-quality");
    qualitySelects.forEach(function(sel) {
      sel.addEventListener("change", function() {
        var id = sel.getAttribute("data-id");
        var item = playlistState.items.find(function(i) { return i.id === id; });
        if (item) item.quality = sel.value;
      });
    });

    // Track selectors
    var trackSelects = document.querySelectorAll(".item-track");
    trackSelects.forEach(function(sel) {
      sel.addEventListener("change", function() {
        var id = sel.getAttribute("data-id");
        var item = playlistState.items.find(function(i) { return i.id === id; });
        if (item) item.track = sel.value;
      });
    });

    // Delete buttons
    var deleteBtns = document.querySelectorAll(".item-delete");
    deleteBtns.forEach(function(btn) {
      btn.addEventListener("click", function() {
        var id = btn.getAttribute("data-id");
        playlistState.items = playlistState.items.filter(function(i) { return i.id !== id; });
        updatePlaylistUI();
      });
    });

    // Retry buttons
    var retryBtns = document.querySelectorAll(".item-retry");
    retryBtns.forEach(function(btn) {
      btn.addEventListener("click", function() {
        var id = btn.getAttribute("data-id");
        var item = playlistState.items.find(function(i) { return i.id === id; });
        if (item) {
          item.state = "pending";
          item.progress = 0;
          item.error = null;
          updatePlaylistUI();
        }
      });
    });
  }

  window.__togglePlaylist__ = function() {
    var body = document.querySelector(".playlist-body");
    var arrow = document.querySelector(".playlist-arrow");
    if (body && arrow) {
      body.classList.toggle("collapsed");
      arrow.classList.toggle("collapsed");
    }
  };

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var rawValue = (urlInput.value || "").trim();
    if (!rawValue) return;

    var fmt = currentFormat;
    var qual = qualitySel.value;
    if (["wav", "flac", "m4a", "ogg", "opus"].indexOf(qual) !== -1) {
      fmt = qual; qual = "320";
    }

    // Clear previous status
    statusBox.innerHTML = "";
    statusBox.classList.remove("hidden");

    // Split by lines or commas
    var urls = rawValue.split(/[\n,]+/).map(function(s){ return s.trim(); }).filter(function(s){ return s.length > 0; });

    // Handle search (only if single non-URL keyword)
    if (urls.length === 1 && !isYouTubeUrl(urls[0])) {
      convertBtn.disabled = true;
      showStatus('<div class="status-meta"><span>Searching YouTube…</span></div>');
      fetch(API_BASE + "/api/search?q=" + encodeURIComponent(urls[0]))
        .then(function(r) { return r.json(); })
        .then(function(data) {
          convertBtn.disabled = false;
          if (data.status === "ok" && data.results.length > 0) {
            renderSearchResults(data.results);
          } else {
            showStatus('<div class="error">No results found</div>');
          }
        });
      return;
    }

    // Process URLs
    urls.forEach(function(url) {
      // Check if it's a playlist
      if (url.indexOf("list=") !== -1) {
        showStatus('<div class="status-meta"><span>Parsing playlist...</span></div>');
        
        var apiUrl = API_BASE + "/api/playlist?url=" + encodeURIComponent(url);
        console.log("Fetching playlist from:", apiUrl);
        
        fetch(apiUrl)
          .then(function(r) { 
            console.log("Response status:", r.status);
            return r.json(); 
          })
          .then(function(data) {
            console.log("Playlist API response:", data);
            if (data.status === "ok" && data.results && data.results.length > 0) {
              renderPlaylistUI(data.results, data.title || "Playlist");
            } else {
              var errorMsg = data.error || "Failed to parse playlist or playlist is empty";
              showStatus('<div class="error">' + escapeHtml(errorMsg) + '</div>');
            }
          })
          .catch(function(err) {
            console.error("Playlist fetch error:", err);
            showStatus('<div class="error">Failed to fetch playlist. Check console for details.</div>');
          });
      } else {
        startJob(url, fmt, qual, null);
      }
    });
  });
})();
