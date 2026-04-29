#!/usr/bin/env node
/* Generates SEO landing pages + legal pages.
 * Emits web/<slug>/index.html so URLs are clean on any static host.
 * Run: node build.js
 */
const fs = require("fs");
const path = require("path");

const WEB = path.resolve(__dirname);
const SITE = "https://yt2mp3.lol";
const BRAND = "yt2mp3.lol";
const BRAND_SHORT = "YT2MP3";

// ---------- PAGES ----------
// Each page has: slug, title, h1, kicker, defaultFormat, defaultQuality, keywords,
// optional variant ("multi" for multi-URL textarea card), sections, faqs.
// Sections are an array of [heading, bodyHtml]. bodyHtml may contain <p>, <ul>,
// <ol>, <table>, etc. — it's emitted as-is inside the section container.

const PAGES = [

  // =================================================================
  // MP4
  // =================================================================
  { slug: "youtube-to-mp4-converter",
    title: "YouTube to MP4 Converter (1080p & 4K, Free)",
    h1: "YouTube to MP4 Converter",
    kicker: `Download any YouTube video as MP4 in 360p, 720p, 1080p, or 4K. 100% free, no signup, no watermark.`,
    defaultFormat: "mp4", defaultQuality: "1080",
    keywords: "youtube to mp4, youtube mp4 converter, youtube mp4 downloader, youtube to 1080p, youtube to 4k",
    sections: [
      ["The best free YouTube to MP4 converter", `<p>${BRAND} converts any public YouTube link into a ready-to-play MP4 on the device you're already using. It runs entirely in the browser — there is nothing to install, nothing to sign up for, and no watermark is ever burned into the file. Paste the URL, pick MP4 and a resolution, and a few seconds later you have a clean H.264 / AAC file that plays everywhere.</p><p>MP4 remains the default container for video because it's trusted by every operating system, every browser, every TV, and every editor from CapCut and iMovie to Premiere and DaVinci Resolve. When you export with ${BRAND} you get a file that simply works — no conversion tools needed afterwards.</p>`],
      ["How to convert YouTube to MP4", `<ol class="steps"><li><strong>Copy</strong> the video URL from YouTube's share sheet or the address bar.</li><li><strong>Paste</strong> it into the input field above. The clipboard button fills it instantly.</li><li>Pick <strong>MP4</strong> and choose a resolution from 360p up to 2160p (4K).</li><li>Press <strong>Convert</strong>. Progress appears beside the button.</li><li>When the download link lights up, click it — the MP4 lands in your device's downloads folder.</li></ol><p>A typical 1080p three-minute clip finishes in under ten seconds on a fast connection.</p>`],
      ["Why people choose " + BRAND_SHORT + " for MP4", `<ul><li><strong>Full resolution ladder</strong> — 360p, 480p, 720p, 1080p, 1440p, and 2160p whenever the source supports them.</li><li><strong>Always with audio</strong> — the separate video and audio streams YouTube serves are remuxed into a single MP4 with AAC audio, so nothing is silent.</li><li><strong>Works anywhere</strong> — Chrome, Safari, Firefox, Edge, on Windows, macOS, Linux, iOS, and Android.</li><li><strong>No account, no app</strong> — paste and go.</li><li><strong>Zero ads and zero trackers</strong> inside the converter page.</li></ul>`],
      ["What makes our MP4 export different", `<p>Lots of converters give you a low-bitrate MP4 because they only grab the combined "progressive" stream YouTube serves to older devices. ${BRAND} pulls the best separate adaptive streams — the same streams the YouTube app uses for 1080p and 4K playback — and muxes them into one file. The result is noticeably sharper than what generic converters produce, with no re-encoding, so there is no extra quality loss.</p><p>For 4K output we preserve the original H.264 (or H.265 when your target device supports it) video exactly as YouTube uploaded it. The audio is re-encoded to AAC only when needed for container compatibility; most of the time it's copied straight through.</p>`],
      ["Supported resolutions and formats", `<table class="fmt-table"><thead><tr><th>Resolution</th><th>Typical bitrate</th><th>Good for</th></tr></thead><tbody><tr><td>360p</td><td>0.5 – 1 Mbps</td><td>Small phones, slow mobile data</td></tr><tr><td>480p</td><td>1 – 2 Mbps</td><td>Older devices, quick previews</td></tr><tr><td>720p (HD)</td><td>2 – 4 Mbps</td><td>Phones, tablets, social uploads</td></tr><tr><td>1080p (Full HD)</td><td>4 – 8 Mbps</td><td>Laptops, desktops, smart TVs</td></tr><tr><td>1440p (2K)</td><td>9 – 16 Mbps</td><td>High-DPI monitors, QHD editing</td></tr><tr><td>2160p (4K)</td><td>25 – 45 Mbps</td><td>4K TVs, editing timelines, archive</td></tr></tbody></table><p>We also offer audio-only output (MP3, M4A, WAV, OGG, Opus) from the same panel if you just want the soundtrack.</p>`],
      ["Use " + BRAND_SHORT + " on any device", `<p>The site is a single-page web app built mobile-first. The tap targets are at least 44 pixels tall, the layout reflows down to 320 px, and there is no horizontal scroll on any phone. On iOS 15 and later the download saves directly to the Files app; on Android it goes to your standard Downloads folder where the Photos or Gallery app indexes it automatically.</p><p>The site also works on laptops without any plugin. On Chromebooks and Linux boxes where traditional YouTube downloaders don't install, ${BRAND} just works.</p>`],
      ["Troubleshooting and tips", `<ul><li><strong>"Video unavailable"</strong> usually means the video is private, members-only, or blocked in the cookie we used. Open the video in an incognito tab; if you can watch it, we can convert it.</li><li><strong>1080p or 4K is greyed out</strong> — the uploader did not publish that resolution. We always show the highest height YouTube actually serves.</li><li><strong>Download stalls</strong> — the host is under brief load. Try again in 30 seconds; most retries succeed.</li><li><strong>Very long videos</strong> (over three hours) are supported but take proportionally longer. For best results, split them into chapters.</li></ul>`],
      ["Safety and legality", `<p>${BRAND} does not store videos. Converted files are deleted automatically within thirty minutes of completion, and we do not log personally identifying information about you or about which videos you converted. No account is ever created, so there is nothing to breach.</p><p>Downloading content for personal use is legal in many jurisdictions (personal-backup, fair-use, and private-copying exceptions vary by country). Redistributing copyrighted content without permission is not. You are responsible for how you use the files you export — review your local laws and YouTube's Terms of Service, and do not republish material you do not own.</p>`],
    ],
    faqs: [
      ["Is " + BRAND + " really free?", "Yes. There are no subscriptions, no free-trial traps, no hidden credit-card checks, and no watermarks on the output."],
      ["Do I need to install any software?", "No. The converter runs in your web browser on any device. No Chrome extension, no Windows installer, no app."],
      ["Does the MP4 include audio?", "Yes. Video and audio streams are muxed together into a single standards-compliant MP4 with AAC audio."],
      ["What's the highest quality I can get?", "2160p (4K) video, whenever the uploader provided it. We always pick the highest available height that matches your selection."],
      ["Does this work on iPhone and Android?", "Yes. On iOS the file saves to the Files app; on Android it lands in Downloads and is picked up by the gallery."],
      ["Can I download live streams or premieres?", "Finished live streams and premieres work once YouTube has processed the replay, usually within a few minutes of the stream ending."],
      ["Can I download age-restricted videos?", "Most age-restricted public videos work because we ship a signed-in cookie pool on the server. Private or members-only videos will not convert."],
      ["How long can a video be?", "Up to three hours by default. Longer videos are possible but take more time and memory."],
      ["Is my link or IP logged?", "No. The backend only keeps the minimum state required to hand you the file, and deletes it inside 30 minutes."],
      ["Why is the file size so big at 4K?", "4K video is inherently large — 25 – 45 Mbps bitrate is normal. Choose 1080p or 720p if bandwidth or storage is a concern."],
    ],
  },

  // =================================================================
  // SHORTS
  // =================================================================
  { slug: "youtube-shorts-downloader",
    title: "YouTube Shorts Downloader (MP3 & MP4, No Watermark)",
    h1: "YouTube Shorts Downloader",
    kicker: "Save any YouTube Short as MP3 audio or MP4 video in seconds. Vertical framing preserved. No watermark.",
    defaultFormat: "mp4", defaultQuality: "1080",
    keywords: "youtube shorts downloader, shorts to mp3, shorts to mp4, download youtube shorts, save youtube shorts, shorts downloader no watermark",
    sections: [
      ["The best YouTube Shorts downloader online", `<p>Shorts are just YouTube videos under sixty seconds, so ${BRAND} processes them through the same high-quality pipeline as long-form uploads. Paste a Shorts URL — anything that looks like <code>youtube.com/shorts/&lt;id&gt;</code> — pick MP3 or MP4, and the file is yours in a few seconds. No watermark, no "branded" intro, no trailer overlay.</p>`],
      ["How to download a YouTube Short", `<ol class="steps"><li>In the YouTube app or site, open the Short and tap <strong>Share → Copy link</strong>.</li><li>Paste the URL into ${BRAND}.</li><li>Pick MP4 for the full video or MP3 for just the audio.</li><li>Click Convert. Shorts are small, so most finish in under five seconds.</li><li>Tap the download button when it appears.</li></ol>`],
      ["Why people choose " + BRAND_SHORT + " for Shorts", `<ul><li><strong>Zero watermark</strong> — the exported file is identical to what the creator uploaded.</li><li><strong>Vertical 9:16 preserved</strong> — nothing is cropped, stretched, or re-framed.</li><li><strong>Audio-only option</strong> — perfect for memes, reactions, and ringtones.</li><li><strong>Mobile-first</strong> — the UI is built for phones, which is where Shorts live anyway.</li></ul>`],
      ["What makes our Shorts export different", `<p>Most Shorts downloaders re-encode the video at a low bitrate so the file is small, which introduces visible blocking and banding. ${BRAND} copies the best available stream directly, only remuxing the container. For a 30-second Short filmed in 1080p vertical, you end up with a pristine ~7 MB MP4 that looks identical to the source.</p>`],
      ["Download YouTube Shorts as MP3", `<p>Most Shorts are either full songs, remixes, viral clips, or short comedy bits — ideal source material for ringtones, samples, or meme libraries. Select MP3 at 320 kbps and ${BRAND} strips just the audio track and encodes it to a constant-bitrate MP3 that works in every music player. No video overhead, no wasted space.</p>`],
      ["Supported formats and quality", `<ul><li><strong>Video:</strong> MP4 at the source resolution (usually 720p or 1080p; occasionally 1440p).</li><li><strong>Audio:</strong> MP3 (128/192/256/320 kbps CBR), M4A (AAC), WAV (lossless), OGG Vorbis, Opus.</li><li><strong>Aspect ratio:</strong> 9:16 vertical, preserved as recorded.</li></ul>`],
      ["Use " + BRAND_SHORT + " on any device", `<p>Because Shorts are a mobile-first format, most people use this page from a phone. The converter is responsive from 320 px upward, tap targets are 44 px or larger, and the download triggers the native file picker on iOS and Android. No plugins, no apps.</p>`],
      ["Troubleshooting and tips", `<ul><li>If a Short will not convert, try opening it on desktop — some Shorts are restricted to signed-in mobile viewers, and we need a stable URL.</li><li>If the output looks low-resolution, the creator uploaded at that size. We always export the highest available height.</li><li>Age-restricted Shorts work thanks to our server-side cookie pool, but members-only Shorts will not.</li></ul>`],
    ],
    faqs: [
      ["Is it free and watermark-free?", "Yes. No fees, no account, no watermark ever added to the downloaded file."],
      ["Why can't I pick 1080p for this Short?", "The uploader did not publish at 1080p. We display only the heights YouTube serves for that specific video."],
      ["How do I save a Short on my iPhone?", "Tap the download button — Safari will offer to save to Files, Photos, or iCloud Drive."],
      ["Can I download only the audio from a Short?", "Yes. Pick MP3 (320 kbps for best quality) or M4A for a zero-loss AAC copy."],
      ["Why does the download finish so quickly?", "Shorts are short — a 30-second 1080p Short is under 10 MB, so even on mobile data it's done in a second or two."],
      ["Does it work on Android?", "Yes. The file saves to your Downloads folder and shows up in your gallery automatically."],
      ["Can I batch-download a channel's Shorts feed?", "Add them to a playlist, then paste the playlist URL on the playlist downloader page. Every Short will be queued individually."],
      ["Are the downloads stored anywhere?", "No. Files are deleted from the server within 30 minutes. Your link is not logged."],
    ],
  },

  // =================================================================
  // PLAYLIST  (expanded — 10 sections, 12 FAQs)
  // =================================================================
  { slug: "youtube-playlist-downloader",
    title: "YouTube Playlist Downloader (MP3 & MP4 Batch)",
    h1: "YouTube Playlist Downloader",
    kicker: "Convert an entire YouTube playlist to MP3 or MP4 in one click. Each video becomes its own clean file.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "youtube playlist downloader, playlist to mp3, youtube playlist to mp4, batch youtube converter, download playlist mp3, youtube music playlist downloader",
    sections: [
      ["Download full YouTube playlists in one click", `<p>${BRAND} is the simplest way to batch-convert an entire YouTube playlist into local MP3 or MP4 files. Paste the playlist URL (anything with <code>?list=PL…</code>), pick your format and quality, and we queue every video in the playlist as its own job. Each file is named after the original video title, so your local folder mirrors the playlist order.</p><p>This is the fastest workflow for building offline music libraries, archiving tutorial series, saving podcast uploads, and caching lecture series before a long flight. One paste, one click, and the whole list ends up on your disk.</p>`],
      ["Supported playlist types", `<ul><li><strong>User-created public playlists</strong> — anything you or another user curated and made public.</li><li><strong>Unlisted playlists</strong> — only if you have the link.</li><li><strong>Auto-generated "Topic" playlists</strong> for an artist or album on YouTube Music.</li><li><strong>Auto-generated "Mix" lists</strong> — these update frequently, so we snapshot what YouTube returns at convert time.</li><li><strong>Uploads from a channel</strong> — paste the channel uploads playlist URL.</li></ul><p>Private playlists will not resolve because they require an authenticated session we cannot reproduce on your behalf.</p>`],
      ["How to download a YouTube playlist", `<ol class="steps"><li>Open the playlist on YouTube and copy the URL — it looks like <code>https://www.youtube.com/playlist?list=PL…</code> or a watch URL with <code>&amp;list=PL…</code>.</li><li>Paste it into ${BRAND} above.</li><li>Pick <strong>MP3</strong> if you want each video as audio (128, 192, 256, or 320 kbps) or <strong>MP4</strong> if you want the video files (360p – 2160p).</li><li>Click <strong>Convert</strong>. A progress list appears; each video in the playlist is a separate download.</li><li>Click each file as it becomes ready, or use the "Download all" link at the end.</li></ol>`],
      ["Playlist to MP3: build an offline music library", `<p>Most people use the playlist downloader to turn a "liked songs", "road trip", or curated album playlist into a local MP3 library. Pick MP3 320 kbps for near-transparent audio, MP3 256 kbps for a balance of size and quality, or MP3 128 kbps if you're tight on storage. Each track is encoded to constant bitrate so the file is honest about its quality.</p><p>If you want to keep absolute fidelity, pick M4A — we copy the AAC audio directly out of YouTube's stream with no re-encoding. The file is slightly larger than MP3 128 and indistinguishable from the YouTube original.</p>`],
      ["Playlist to MP4: archive tutorials, lectures, and series", `<p>For video playlists, pick MP4 at 720p for a good balance between quality and size, 1080p for desktop viewing, or 2160p (4K) for maximum quality when the source supports it. A ten-video tutorial series at 1080p typically ends up around 800 MB – 1.5 GB total, small enough to store on a phone.</p>`],
      ["Works on any device, online", `<p>${BRAND} runs entirely in your browser. No desktop app, no Chrome extension, no Android APK. That matters for playlist conversions because our competitors often require a paid desktop installer for "batch" mode — we do it natively in the web.</p><p>It works on any modern Chromium browser, Firefox, Safari, iOS, Android, Linux, ChromeOS, and inside the in-app browsers that Twitter, Instagram, and Telegram use to preview YouTube links.</p>`],
      ["Why choose " + BRAND_SHORT + " for playlists", `<ul><li><strong>True batch processing</strong> — one paste, dozens of files.</li><li><strong>Per-video naming</strong> — files are named after the original title, not a generic "video_1".</li><li><strong>Format flexibility</strong> — MP3, MP4, M4A, WAV, OGG, Opus.</li><li><strong>Retry on failure</strong> — if one video in the playlist fails (private, deleted, region-blocked), the rest still complete.</li><li><strong>No playlist size cap</strong> — we've processed lists of over 500 videos.</li><li><strong>Auto-cleanup</strong> — files are removed from the server within 30 minutes of being served.</li></ul>`],
      ["Tips for faster playlist conversion", `<ul><li><strong>Start on MP3 before MP4</strong> — audio is smaller and quicker; you'll see the fastest wins there.</li><li><strong>Close other browser tabs</strong> — the polling logic runs client-side, so freeing up CPU helps.</li><li><strong>Wired connection on desktop</strong> — downloads from our backend are I/O bound at about 50 – 80 MB/s on a good pipe.</li><li><strong>Pause and resume</strong> — if you close the tab, re-paste the playlist URL and any already-completed files will be served from cache within the 30-minute window.</li></ul>`],
      ["Legal and safety notes", `<p>Playlists often mix your own uploads, Creative-Commons-licensed tracks, and copyrighted music. Downloading them for personal, non-commercial use is covered by private-copying exceptions in many countries, but redistribution is not. We do not host the media — we produce the file in your browser session and delete it from our side within thirty minutes. You are responsible for reviewing your local law and YouTube's Terms of Service before you share any downloaded file.</p>`],
    ],
    faqs: [
      ["Is there a maximum playlist length?", "There's no hard cap on the site; we have processed playlists over 500 videos. Very long lists do take proportionally longer to complete."],
      ["Can I download an entire YouTube channel's uploads?", "Yes — every channel has an 'uploads' playlist (the URL on the channel's Videos tab). Paste that and all uploads queue up."],
      ["Will it work with an auto-generated Mix?", "Yes, but Mixes change based on YouTube's recommendation engine. We snapshot what's in the list when you submit."],
      ["Can I download a playlist as MP3 at 320 kbps?", "Yes, pick MP3 and 320 kbps. Every track in the playlist is encoded at that bitrate."],
      ["Do I need an account?", "No. There is no signup, no login, and no personal data collection."],
      ["Does YouTube know that I'm downloading?", "We talk to YouTube's public endpoints from our server. Your IP address is not sent to YouTube when you click convert — only ours is."],
      ["Are age-restricted videos supported inside a playlist?", "Yes. Our server uses a signed-in cookie pool so the vast majority of age-restricted videos convert. Members-only videos do not."],
      ["Why did one video in my playlist fail?", "It was probably deleted, set to private, or region-blocked for the cookie we used. The rest of the playlist still completes."],
      ["Can I keep the playlist order?", "Yes — files are named with a numeric prefix matching the playlist index, so sorted folder listings preserve the order."],
      ["Does it work on mobile?", "Fully. On iPhone the files save to the Files app; on Android they go to Downloads."],
      ["Can I download private playlists?", "No — private playlists require an authenticated YouTube session that only you have."],
      ["Is the service really free?", "Yes. Free, with no ads on the converter page, no watermarks, and no feature gate."],
    ],
  },

  // =================================================================
  // MULTI (textarea variant — 8 sections, 10 FAQs)
  // =================================================================
  { slug: "youtube-multi-downloader",
    title: "YouTube Multi Downloader (Batch MP3 & MP4)",
    h1: "YouTube Multi Downloader",
    kicker: "Paste multiple YouTube URLs — one per line — and download them all as MP3 or MP4 in a single batch.",
    defaultFormat: "mp3", defaultQuality: "320",
    variant: "multi",
    keywords: "youtube multi downloader, batch youtube downloader, multiple youtube videos to mp3, bulk youtube converter, download many youtube videos at once",
    sections: [
      ["Download multiple YouTube videos at once", `<p>Sometimes you don't have a single playlist — you have a handful of links you want to grab in one go. ${BRAND}'s multi downloader takes a list of YouTube URLs (one per line) and queues every one of them individually. Each file is named after its original video title, so there's no renaming to do afterwards.</p><p>You can mix and match: drop in long videos, Shorts, Music tracks, and live-stream replays in the same list. Each one is processed independently.</p>`],
      ["What is a YouTube multi downloader?", `<p>A multi downloader is a batch converter — instead of pasting one URL at a time, you paste an entire list. On ${BRAND} the textarea accepts up to a few hundred lines. We validate each URL, spin up one conversion job per video, and hand you a row of download buttons the moment each finishes.</p>`],
      ["How to download multiple videos at once", `<ol class="steps"><li><strong>Copy each YouTube URL</strong> to your clipboard — from the share sheet, address bar, or anywhere the link is visible.</li><li><strong>Paste them</strong> into the big textarea above, one URL per line.</li><li>Select <strong>MP3</strong> or <strong>MP4</strong> and pick your preferred quality. All videos will use the same format and quality.</li><li>Click <strong>Convert</strong>. Each video gets a progress row; finished files expose a direct download button.</li><li>Click each download link as it turns on, or use "Download all" to grab every file in one go.</li></ol>`],
      ["How to paste multiple YouTube links", `<p>Any of these forms work, and you can mix them freely in the same batch:</p><ul><li><code>https://www.youtube.com/watch?v=&lt;id&gt;</code></li><li><code>https://youtu.be/&lt;id&gt;</code></li><li><code>https://www.youtube.com/shorts/&lt;id&gt;</code></li><li><code>https://music.youtube.com/watch?v=&lt;id&gt;</code></li><li><code>https://m.youtube.com/watch?v=&lt;id&gt;</code></li></ul><p>Blank lines are ignored; duplicates are deduplicated; anything that isn't a YouTube URL is skipped with a visible warning so you know which lines to fix.</p>`],
      ["Download multiple YouTube videos as MP3", `<p>Pick MP3 and 320 kbps for the highest-quality audio batch. This is the usual workflow for building a local music library or bulk-ripping podcast episodes. Each track is encoded to a constant 320 kbps MP3 with ID3 metadata populated from the video title when possible.</p>`],
      ["Download multiple YouTube videos as MP4", `<p>Select MP4 and 1080p for the best video balance. The batch handles a mix of aspect ratios (16:9 long-form and 9:16 Shorts in the same queue) without any manual configuration.</p>`],
      ["Why choose " + BRAND_SHORT + " for bulk downloads", `<ul><li><strong>Unlimited batch size</strong> — the textarea accepts several hundred URLs.</li><li><strong>Fair-use parallelism</strong> — we process a handful in parallel to keep the batch fast without stressing the backend.</li><li><strong>Per-URL retry</strong> — if one video fails, the rest still finish. You get a clear "retry" button on any failure.</li><li><strong>No app, no account, no watermark.</strong></li><li><strong>Works on any device</strong> — including phones, where the textarea supports multi-select paste.</li></ul>`],
      ["Troubleshooting bulk downloads", `<ul><li><strong>"Rate limited"</strong> — try a smaller batch (50 – 100 URLs). YouTube has global rate limits that we respect to avoid disruptions.</li><li><strong>One video fails</strong> — most likely deleted, private, or members-only. Re-submit with that line removed.</li><li><strong>Browser warns "too many downloads"</strong> — Chrome and Safari prompt on the first auto-download of a session. Click Allow once and the rest sail through.</li></ul>`],
    ],
    faqs: [
      ["Can I download multiple YouTube videos at once?", "Yes. Paste each URL on its own line in the textarea above and every URL is processed as an independent job."],
      ["Do the videos need to be in the same playlist?", "No. Any public YouTube URL is accepted. You can mix long videos, Shorts, and YouTube Music tracks in the same batch."],
      ["How should I paste the video links?", "One URL per line. youtu.be, youtube.com/watch, and youtube.com/shorts formats all work. Blank lines and malformed URLs are ignored with a warning."],
      ["Can I download multiple videos as MP3?", "Yes, pick MP3 and any bitrate from 128 – 320 kbps. All videos in the batch use the same format and quality."],
      ["Is there a limit on the number of videos?", "No hard cap, but large batches are slower. We recommend 50 – 100 URLs at a time for a responsive experience."],
      ["Do all videos have to be the same length?", "No — short and long videos can be mixed. The batch waits for all jobs to finish before offering 'Download all', but you can grab each file the moment it's ready."],
      ["Can I pick different quality per video?", "No. The batch uses one format and quality for every URL. Run the batch twice if you need different settings."],
      ["Does it work on mobile?", "Yes. The textarea fully supports multi-line paste from Notes, WhatsApp, Telegram, Gmail, and any other app that can paste plain text."],
      ["Are the files stored?", "No. Each file is deleted from the server within 30 minutes of being generated."],
      ["Is it free?", "Yes. There's no paywall, no ad unit inside the converter, and no watermark on the output."],
    ],
  },

  // =================================================================
  // 320 KBPS
  // =================================================================
  { slug: "youtube-to-mp3-320kbps-converter",
    title: "YouTube to MP3 320kbps Converter (Best Quality, Free)",
    h1: "YouTube to MP3 320kbps",
    kicker: "Convert any YouTube video to a 320 kbps constant-bitrate MP3. Highest quality, smallest possible artifacts.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "youtube to mp3 320kbps, youtube mp3 320, best quality youtube mp3, 320 kbps converter, youtube music 320",
    sections: [
      ["The best YouTube to MP3 320kbps converter", `<p>320 kbps is the highest bitrate the MP3 format supports. Above that, the format itself saturates — there is simply no more audio information that LAME, FFmpeg, or any encoder can pack into an MP3 frame. ${BRAND} uses a LAME-compatible encoder (shipped inside FFmpeg) with constant bitrate mode, so every frame in your output is genuinely at 320 kbps, not a lower variable-bitrate average relabelled as 320.</p>`],
      ["How to convert YouTube to MP3 320kbps", `<ol class="steps"><li>Copy any YouTube link (video, music, or Shorts).</li><li>Paste it into the converter.</li><li>Pick <strong>MP3</strong> and then <strong>320 kbps</strong>.</li><li>Click Convert. A three-minute song takes around six to ten seconds.</li><li>Download the MP3 to your device.</li></ol>`],
      ["Why people choose " + BRAND_SHORT + " for 320 kbps MP3", `<ul><li><strong>Honest bitrate</strong> — we encode in CBR, not VBR-pretending-to-be-320.</li><li><strong>No re-compression hop</strong> — we pull YouTube's best Opus or AAC stream and encode once, not twice.</li><li><strong>Fast encoding</strong> — three to six seconds per typical song on our backend.</li><li><strong>Works on any device</strong> — the MP3 plays on every device, every player, every car stereo ever made.</li></ul>`],
      ["What makes our 320 kbps different", `<p>Most free converters transcode from YouTube's already-compressed 128 kbps AAC and then upsample to 320 kbps. That looks like 320 kbps in a file-info panel but sounds like 128 kbps because the original bits are gone. ${BRAND} reaches for the Opus stream (up to ~160 kbps perceptually-transparent) and encodes from that, which preserves significantly more detail through the MP3 step. The difference is audible on cymbals, breathy vocals, and reverb tails.</p>`],
      ["Supported formats and quality", `<ul><li><strong>MP3:</strong> 128, 192, 256, 320 kbps constant bitrate.</li><li><strong>M4A:</strong> AAC direct-copy from YouTube's stream — no re-encoding at all.</li><li><strong>WAV:</strong> uncompressed 44.1 kHz / 16-bit PCM.</li><li><strong>OGG Vorbis / Opus:</strong> for devices that prefer open codecs.</li></ul><p>Every format is available on every video. Pick whatever your target player supports best.</p>`],
      ["Use " + BRAND_SHORT + " on any device", `<p>The converter works on Chrome, Safari, Firefox, and Edge across Windows, macOS, Linux, iOS, and Android. On iPhone the 320 kbps MP3 can be opened in the Music app via "Share → Open in Music". On Android it shows up in the system music player instantly. In a car head unit with USB, just drop the file onto a stick.</p>`],
      ["Troubleshooting and tips", `<ul><li><strong>Is 320 always better?</strong> On good headphones, yes — but below 128 kbps source material, you can't add information that isn't there.</li><li><strong>My player says "320 kbps" but the quality is poor.</strong> The source upload was low-bitrate. Nothing a converter can do about that.</li><li><strong>No metadata?</strong> We populate ID3 tags from the YouTube title and uploader. You can edit them in iTunes, foobar2000, or Mp3tag.</li></ul>`],
      ["Safety and legality", `<p>We don't store files, we don't log your IP, and we don't sell data. Downloading for personal offline listening is legal in many countries; redistributing copyrighted music is not. Check your local law and YouTube's Terms of Service — you are responsible for how you use the files.</p>`],
    ],
    faqs: [
      ["Is 320 kbps always better than 128 kbps?", "On good headphones or speakers, yes — there's more spatial detail and cleaner high frequencies. On phone speakers the difference is subtle."],
      ["Do you add ID3 metadata or cover art?", "We populate title, artist, and album when YouTube exposes them. Cover art is embedded for most YouTube Music tracks."],
      ["Is " + BRAND + " free and safe?", "Yes — free, no account, no ads on the converter page, no watermark, no malware."],
      ["Will this work on iPhone and Android?", "Yes. Safari saves to Files on iOS; Chrome on Android saves to Downloads and the system music player picks it up."],
      ["Can I convert very long videos to MP3 320?", "Yes, up to three hours by default. Longer files are still supported but take more time."],
      ["Is it legal to convert YouTube to MP3?", "It depends on your country and what you do with the file. Personal-use downloading is legal in many jurisdictions; redistribution generally is not. Review your local laws and YouTube's TOS."],
      ["Will 320 kbps fix a bad-sounding source?", "No. A converter can't reconstruct information that was lost when the source was encoded at a lower bitrate."],
      ["How big is a typical 320 kbps MP3?", "About 2.4 MB per minute of audio — so a 4-minute song is around 9 – 10 MB."],
      ["Does this work for YouTube Music tracks?", "Yes. YouTube Music URLs are accepted directly."],
    ],
  },

  // =================================================================
  // WAV
  // =================================================================
  { slug: "wav-converter",
    title: "YouTube to WAV Converter (Lossless, 44.1 kHz)",
    h1: "YouTube to WAV",
    kicker: "Convert YouTube audio to lossless 44.1 kHz WAV for editing, sampling, or studio work.",
    defaultFormat: "wav", defaultQuality: "320",
    keywords: "youtube to wav, wav converter, youtube lossless wav, yt to wav, wav from youtube",
    sections: [
      ["YouTube to WAV, lossless", `<p>WAV is the simplest lossless container — uncompressed PCM samples with a tiny header. Every DAW on earth (Ableton Live, Logic Pro, FL Studio, Reaper, Pro Tools) opens it instantly, and it round-trips through editing without cumulative quality loss. ${BRAND} converts any YouTube video to 44.1 kHz 16-bit stereo WAV, which is CD-quality and the industry baseline for sampling and editing.</p>`],
      ["How to convert YouTube to WAV", `<ol class="steps"><li>Paste the YouTube URL.</li><li>Pick <strong>WAV</strong> as the format.</li><li>Click Convert.</li><li>Drop the WAV into your DAW.</li></ol>`],
      ["When WAV makes sense", `<ul><li><strong>Sampling and remixing</strong> — don't stack compressed-format losses.</li><li><strong>Editing for podcasts or video</strong> — edit in WAV, export the finished mix to MP3 or AAC.</li><li><strong>Archival copies</strong> — lossless is future-proof.</li><li><strong>Transcription</strong> — WAV is what most transcription models want.</li></ul>`],
      ["Size and quality", `<p>WAV is uncompressed, so a 3-minute clip is roughly 30 MB. If you need lossless but smaller, we also offer FLAC-like M4A-ALAC output. For maximum compression with minimal audible loss, use MP3 320 or M4A AAC.</p>`],
      ["Works on any device", `<p>WAV plays natively on Windows, macOS, Linux, iOS, and Android. Drop it on a USB stick and any modern car stereo will play it.</p>`],
    ],
    faqs: [
      ["Is the WAV really lossless?", "Yes — we decode the best available YouTube audio and render it to 44.1 kHz 16-bit PCM with no lossy re-encoding step."],
      ["Can I get 48 kHz or 24-bit WAV?", "By default we output 44.1 kHz 16-bit for universal compatibility. DAWs will resample/re-bit-depth on import if you need higher."],
      ["How big is a typical WAV?", "About 10 MB per minute of stereo audio."],
      ["Is WAV better than 320 kbps MP3?", "In absolute terms yes (no lossy compression), but most listeners cannot reliably tell the difference on good MP3 320."],
      ["Does WAV preserve the original dynamic range?", "Yes — we don't apply normalization or compression."],
    ],
  },

  // =================================================================
  // M4A
  // =================================================================
  { slug: "m4a-converter",
    title: "YouTube to M4A Converter (AAC Direct Copy)",
    h1: "YouTube to M4A",
    kicker: "Convert YouTube audio to high-quality M4A (AAC). Perfect for iPhone, iTunes, and Apple Music.",
    defaultFormat: "m4a", defaultQuality: "320",
    keywords: "youtube to m4a, m4a converter, aac from youtube, youtube music m4a",
    sections: [
      ["YouTube to M4A, direct AAC copy", `<p>YouTube's native audio stream is AAC inside an .m4a container. When you pick M4A in ${BRAND} we skip the re-encoding step and copy YouTube's AAC track straight through — so the output is bit-for-bit identical to what YouTube streams, without any second-generation compression loss.</p>`],
      ["Why choose M4A over MP3", `<ul><li><strong>Native on Apple</strong> — iPhone, iPad, Mac, and Apple Music all treat M4A as first-class.</li><li><strong>Smaller at the same perceived quality</strong> — AAC is a more modern codec than MP3.</li><li><strong>Gapless playback</strong> — for albums, M4A/AAC supports gapless better than MP3.</li><li><strong>Metadata and artwork</strong> — M4A files carry embedded art reliably across players.</li></ul>`],
      ["How to convert YouTube to M4A", `<ol class="steps"><li>Paste the URL.</li><li>Pick <strong>M4A</strong>.</li><li>Click Convert.</li><li>Add the file to iTunes, Apple Music, or drag it into the Files app on iPhone.</li></ol>`],
    ],
    faqs: [
      ["Is the M4A lossless?", "It's as lossless as YouTube's original upload — we copy the AAC audio through without re-encoding. The only quality loss is whatever happened during YouTube's original transcode."],
      ["What bitrate is the M4A?", "Matches the YouTube source — typically 128 kbps AAC for music, sometimes up to 256 kbps for premium content."],
      ["Will it play in iTunes?", "Yes — M4A is the native iTunes format."],
      ["Can I set custom metadata?", "We populate title, artist, and album from the YouTube title. You can edit in Mp3tag, Music.app, or any tag editor."],
    ],
  },

  // =================================================================
  // IPHONE
  // =================================================================
  { slug: "iphone-converter",
    title: "YouTube to MP3 Converter for iPhone (Safari, No App)",
    h1: "YouTube to MP3 on iPhone",
    kicker: "Convert any YouTube video to MP3 or MP4 directly in Safari on your iPhone. No app, no jailbreak, no subscription.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "youtube to mp3 iphone, yt to mp3 iphone, youtube converter ios safari, iphone youtube downloader",
    sections: [
      ["Convert YouTube on iPhone without an app", `<p>Apple has removed most YouTube downloaders from the App Store. ${BRAND} works around that by running entirely in Safari — there is no native app to install, so there is nothing for Apple to block. Paste a YouTube URL, pick MP3 or MP4, and the file downloads to the Files app just like any other Safari download.</p>`],
      ["Step-by-step on iPhone", `<ol class="steps"><li>Open YouTube, tap the video, then <strong>Share → Copy link</strong>.</li><li>Switch to Safari and open <code>${BRAND}</code>.</li><li>Long-press the URL field and tap <strong>Paste</strong>, or use the clipboard icon.</li><li>Pick format and quality. Tap <strong>Convert</strong>.</li><li>When the download link appears, tap it. Safari offers to save to Files, iCloud Drive, or Photos.</li><li>To move the MP3 into the Music app: open Files → tap the MP3 → share → <strong>Open in Music</strong>.</li></ol>`],
      ["Which iOS versions are supported", `<p>Any iPhone running iOS 14 or later works. The Files-app integration exists in iOS 11+, but the download prompts are cleaner in iOS 14 and later.</p>`],
      ["Adding to Apple Music or ringtones", `<p>MP3 and M4A files downloaded through ${BRAND} can be imported into the Music app via the Files app share sheet. For a custom ringtone, trim the MP3 to under 30 seconds in GarageBand, then Export → Share → Ringtone.</p>`],
    ],
    faqs: [
      ["Do I need to jailbreak my iPhone?", "No. ${BRAND} runs in Safari — nothing is installed on your phone."],
      ["Will downloads save to Photos or Files?", "By default they go to Files (Downloads folder). You can tap Share → Save to Photos if you prefer."],
      ["Can I convert to MP4 on iPhone?", "Yes — pick MP4 and the file saves directly to Files or Photos."],
      ["Does this work on iPad?", "Yes — the interface is identical on iPadOS."],
      ["Is there an app version?", "No. There is deliberately no native app — keeping it web-only means Apple can't remove it from an app store."],
    ],
  },

  // =================================================================
  // ANDROID
  // =================================================================
  { slug: "android-converter",
    title: "YouTube to MP3 Converter for Android (Chrome, No APK)",
    h1: "YouTube to MP3 on Android",
    kicker: "Convert YouTube to MP3 or MP4 on any Android phone using Chrome. No APK, no root, no Play-Store approval needed.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "youtube to mp3 android, yt to mp3 android, youtube converter android chrome, android youtube downloader no apk",
    sections: [
      ["Download YouTube on Android without an APK", `<p>Google blocks most converter APKs from the Play Store for obvious reasons, and side-loading a random APK from the internet is a security risk. ${BRAND} lets you convert YouTube links to MP3 or MP4 entirely in Chrome, Samsung Internet, or any modern Android browser — no APK, no root required, nothing to give permissions to beyond Downloads.</p>`],
      ["Step-by-step on Android", `<ol class="steps"><li>Open YouTube, tap <strong>Share → Copy link</strong>.</li><li>Switch to Chrome and open <code>${BRAND}</code>.</li><li>Tap the URL field and paste.</li><li>Pick MP3 or MP4 and the quality you want.</li><li>Tap Convert. When the download button appears, tap it.</li><li>The file lands in Downloads and appears in your gallery or music player.</li></ol>`],
      ["Install as a PWA for one-tap access", `<p>On the Install page we offer a one-tap "Add to Home Screen" shortcut that pins ${BRAND} to your launcher like a regular app. It loads offline-capable assets, opens in its own window (no browser chrome), and weighs less than 100 KB.</p>`],
      ["Samsung, OnePlus, Xiaomi and other OEMs", `<p>Because we rely on standard web APIs (Fetch, Blob, Download Attribute), we work identically on every major Android skin — One UI, OxygenOS, MIUI, ColorOS, stock Pixel. The only OEM-specific thing is where the file lands (usually <code>Download/</code>, sometimes <code>Downloads/</code>).</p>`],
    ],
    faqs: [
      ["Do I need root?", "No. Chrome's standard download API handles everything."],
      ["Why aren't there YouTube-to-MP3 apps on the Play Store?", "Google's policy blocks most of them. The web-based approach sidesteps that entirely."],
      ["Where do downloads go?", "Your Downloads folder. Most Android music players and galleries index that folder automatically."],
      ["Can I install " + BRAND + " as an app?", "Yes — tap the three-dot menu in Chrome and pick 'Add to Home screen' (the prompt appears automatically on our Install page)."],
      ["Will it work on a tablet?", "Yes — the interface scales up to Android tablets and Chromebooks."],
    ],
  },

  // =================================================================
  // FAQ
  // =================================================================
  { slug: "faq", title: "FAQ", h1: "Frequently Asked Questions",
    kicker: "Everything people ask about " + BRAND + ", in one place.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: BRAND + " faq, youtube converter faq, ytmp3 questions",
    sections: [
      ["About the service", `<p>${BRAND} is a free web-based YouTube to MP3 and MP4 converter. No accounts, no apps, no ads inside the converter, no watermarks. Everything runs in your browser on any device — iPhone, Android, laptop, Chromebook.</p>`],
      ["Supported formats and quality", `<ul><li><strong>Audio</strong>: MP3 (128/192/256/320 kbps), M4A (direct AAC copy), WAV (44.1 kHz lossless), OGG Vorbis, Opus.</li><li><strong>Video</strong>: MP4 in 360p, 480p, 720p, 1080p, 1440p, 2160p (4K) whenever the source supports it.</li></ul>`],
      ["Supported URL types", `<ul><li>Standard video watch URLs: <code>youtube.com/watch?v=…</code></li><li>Short URLs: <code>youtu.be/…</code></li><li>Shorts: <code>youtube.com/shorts/…</code></li><li>Playlists: <code>youtube.com/playlist?list=…</code></li><li>Music: <code>music.youtube.com/watch?v=…</code></li><li>Mobile: <code>m.youtube.com/watch?v=…</code></li></ul>`],
    ],
    faqs: [
      ["Is " + BRAND + " free?", "Yes — completely. No free trial, no credit-card wall, no feature gate."],
      ["Do I need an account?", "No."],
      ["Are there any ads or watermarks on the file?", "No watermarks ever; the converter page itself is ad-free."],
      ["Does it work on iPhone and Android?", "Yes, in Safari and Chrome respectively. No app required."],
      ["What's the longest video I can convert?", "Three hours by default. Longer videos work but take more time."],
      ["How is my privacy protected?", "No account, no login, and converted files are deleted within 30 minutes."],
      ["Can I download private videos?", "No. Private videos require an authenticated session we don't have."],
      ["Can I download members-only or paid content?", "No — those also require credentials we don't collect."],
      ["Is it legal?", "It depends on your country and what you do with the file. Personal-use offline listening is legal in many jurisdictions; redistribution generally is not. Review your local law."],
      ["Who runs " + BRAND + "?", "A small independent team. See the About page for contact details."],
    ],
  },

  // =================================================================
  // ABOUT
  // =================================================================
  { slug: "about", title: "About", h1: "About " + BRAND,
    kicker: "A fast, free, privacy-respecting YouTube-to-MP3 and MP4 converter — no account, no ads, no app.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "about " + BRAND + ", " + BRAND + " team, youtube converter about",
    sections: [
      ["Who we are", `<p>${BRAND} is a small team of developers who got tired of YouTube converters that were covered in malware pop-ups, required sign-ups, locked features behind paywalls, or burned watermarks into downloaded files. We built the service we wanted to use ourselves: paste a URL, get a file, move on with your day.</p>`],
      ["What we stand for", `<ul><li><strong>No dark patterns.</strong> No "Convert for free!" buttons that actually start a trial. No "By clicking this you agree to…" buried in footers.</li><li><strong>No ads on the converter.</strong> We pay for hosting with donations via the Supporter button and nothing else.</li><li><strong>No data hoarding.</strong> We don't know who you are and don't want to.</li><li><strong>Web-first, forever.</strong> No native app means nothing an app store can delete and nothing to install.</li></ul>`],
      ["How we keep costs down", `<p>The whole site is static files served from a global CDN (Vercel), plus a tiny Python backend on a free container host (Render). Using yt-dlp and FFmpeg's free open-source tooling means there are no per-conversion licensing costs. Donations through the Supporter button pay for bandwidth and the occasional residential-proxy bill.</p>`],
      ["Contact", `<p>See the <a href="/contact">Contact</a> page. We read every message and reply within 48 hours on weekdays.</p>`],
    ],
    faqs: [
      ["Is " + BRAND + " related to ytmp3.gg or ytmp3.cc?", "No. We are an independent service with no corporate relationship to any other YouTube-converter site."],
      ["Is the source code open?", "Some of it. Our frontend template and encoding pipeline configuration are public; the specific request-routing and anti-abuse code is not."],
      ["Can I embed " + BRAND + " on my site?", "We don't provide an iframe-embed officially — but we do offer a simple HTTP API for developers on request."],
    ],
  },

  // =================================================================
  // CONTACT
  // =================================================================
  { slug: "contact", title: "Contact", h1: "Contact Us",
    kicker: "Email us for support, copyright concerns, or partnerships.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "contact " + BRAND + ", " + BRAND + " support, " + BRAND + " dmca",
    sections: [
      ["How to reach us", `<ul><li><strong>Support &amp; bug reports</strong> — <a href="mailto:support@${BRAND}">support@${BRAND}</a>. Please include the URL you tried, the format and quality you picked, and the browser / device you used. Screenshots help a lot.</li><li><strong>Copyright / DMCA notices</strong> — <a href="mailto:dmca@${BRAND}">dmca@${BRAND}</a>. See the <a href="/copyright-claims">Copyright Claims</a> page for the required format.</li><li><strong>Press, partnerships, proxy vendors</strong> — <a href="mailto:hello@${BRAND}">hello@${BRAND}</a>.</li></ul>`],
      ["Response time", `<p>We reply to every inbound email within 48 hours on weekdays. Copyright notices are handled on priority.</p>`],
    ],
    faqs: [
      ["Is there a contact form?", "Not currently — email is faster for us to triage, and it gives you a paper trail."],
      ["Can I request a new feature?", "Yes — email support@" + BRAND + " with the use case and we'll add it to the backlog."],
    ],
  },

  // =================================================================
  // HOW TO INSTALL (PWA)
  // =================================================================
  { slug: "how-to-install", title: "How to Install " + BRAND,
    h1: "How to Install " + BRAND,
    kicker: "Pin " + BRAND + " to your home screen in one tap — no app store, no APK, no installer.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "install " + BRAND + ", " + BRAND + " pwa, youtube converter pwa install",
    sections: [
      ["Why install " + BRAND + " as a PWA", `<p>${BRAND} is a Progressive Web App — which means your browser can "install" it to your home screen as a self-contained app icon. It opens in its own window (no browser chrome), loads instantly on second visit, and works on Wi-Fi dropouts thanks to a cached shell. There is no APK, no IPA, no App Store review, and nothing to remove a week later.</p>`],
      ["Install on Android (Chrome)", `<ol class="steps"><li>Open <code>${BRAND}</code> in Chrome.</li><li>Tap the three-dot menu in the top-right.</li><li>Tap <strong>Add to Home screen</strong> or <strong>Install app</strong>.</li><li>Confirm the name. The icon appears on your launcher.</li></ol>`],
      ["Install on iPhone / iPad (Safari)", `<ol class="steps"><li>Open <code>${BRAND}</code> in Safari.</li><li>Tap the Share icon (square with arrow up).</li><li>Scroll and tap <strong>Add to Home Screen</strong>.</li><li>Tap <strong>Add</strong> in the top-right. The icon lands on your Home Screen.</li></ol>`],
      ["Install on desktop (Chrome, Edge, Brave)", `<ol class="steps"><li>Open ${BRAND} on your laptop or desktop.</li><li>Click the install icon in the address bar (little monitor with down-arrow).</li><li>Confirm Install. ${BRAND} opens in its own window and pins to your dock / taskbar.</li></ol>`],
      ["Uninstalling", `<p>Long-press the icon on Android or iOS and pick Remove. On desktop, open ${BRAND} as an app, click the three-dot menu, and pick Uninstall.</p>`],
    ],
    faqs: [
      ["Is the PWA the same as a native app?", "Functionally yes. It opens in its own window, has an icon, works offline for the UI, and never shows a browser URL bar."],
      ["Will it update automatically?", "Yes — every launch fetches the latest version in the background."],
      ["Does the PWA work offline?", "The UI shell loads offline. Conversions still require an internet connection because they depend on YouTube."],
      ["Can I install it on a Chromebook?", "Yes — Chromebooks install PWAs identically to desktop Chrome."],
    ],
  },

  // =================================================================
  // COPYRIGHT CLAIMS
  // =================================================================
  { slug: "copyright-claims", title: "Copyright Claims", h1: "Copyright Claims & DMCA",
    kicker: "How to file a copyright takedown request with " + BRAND + ".",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "dmca " + BRAND + ", " + BRAND + " copyright, copyright takedown " + BRAND,
    sections: [
      ["Our position on copyright", `<p>${BRAND} does not host, index, cache, or redistribute any YouTube videos. We convert a URL you supply to a file for your personal, transient use, then delete that file from our servers within thirty minutes. Because we do not retain content, there is no persistent media for us to "remove" on the server side.</p><p>That said, we take copyright seriously and will cooperate with rights-holders. If you are a rights-holder and you want ${BRAND} to block all future conversions of a specific video or channel, the procedure below applies.</p>`],
      ["How to file a takedown", `<p>Send an email to <a href="mailto:dmca@${BRAND}">dmca@${BRAND}</a> containing:</p><ol class="steps"><li>Your name, physical address, phone number, and email address.</li><li>Identification of the copyrighted work — title, URL of the original, registration number if applicable.</li><li>The YouTube URL(s) you want blocked from future conversion.</li><li>A statement under penalty of perjury that the information is accurate and that you are authorized to act on behalf of the rights-holder.</li><li>Your physical or electronic signature.</li></ol><p>We process valid notices within 72 hours on business days. Rejected or invalid notices will be responded to with the specific issue.</p>`],
      ["Counter-notices", `<p>If you believe a takedown was filed in error, send a counter-notice to <a href="mailto:dmca@${BRAND}">dmca@${BRAND}</a> with your name, contact details, URL at issue, a statement under penalty of perjury that you believe the removal was a mistake or misidentification, and your consent to the jurisdiction of the federal district court where you reside (or the UK High Court if outside the US).</p>`],
      ["Repeat infringers", `<p>We do not maintain user accounts, so we cannot "ban" users — but we can and do block specific video IDs and channel IDs permanently when we receive repeated valid notices. After three valid notices against a single channel, that channel is hard-blocked indefinitely.</p>`],
    ],
    faqs: [
      ["Do I need a lawyer to file a notice?", "No. The steps above are the same ones you'd follow with any hosting provider."],
      ["Can you disclose who converted my video?", "We don't log IPs tied to specific conversions, so we have nothing to disclose even under subpoena."],
    ],
  },

  // =================================================================
  // PRIVACY
  // =================================================================
  { slug: "privacy-policy", title: "Privacy Policy", h1: "Privacy Policy",
    kicker: "How " + BRAND + " handles (and does not handle) your data.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: BRAND + " privacy, " + BRAND + " data, youtube converter privacy",
    sections: [
      ["Summary — the short version", `<p>${BRAND} does not require an account, does not use tracking cookies, does not set advertising identifiers, does not sell data, and deletes converted files from the server within thirty minutes. Everything that follows is the same point restated with specifics so you can verify it.</p>`],
      ["What data we collect", `<ul><li><strong>The URL you paste</strong> — used only to perform the conversion, held in memory and not written to a persistent database.</li><li><strong>A job ID</strong> — a random string we hand back to your browser so it can ask about status. Automatically expired after 30 minutes.</li><li><strong>Standard HTTP server logs</strong> — IP, user agent, request URL, status, response size, timestamp. Retained for a maximum of 14 days for abuse prevention and then automatically deleted.</li></ul>`],
      ["What data we do NOT collect", `<ul><li>Your name, email address, or any other identifier.</li><li>Your YouTube account, cookies, or login state.</li><li>Tracking cookies or advertising IDs. We set no cookies except a single theme-preference cookie that stays in your browser.</li><li>Analytics fingerprints, cross-site IDs, or any third-party trackers.</li></ul>`],
      ["Third parties", `<p>The service is hosted on two providers: Vercel (static frontend) and Render (API backend). Each sees the standard HTTP logs described above under their respective privacy policies. We do not use Google Analytics, Facebook Pixel, or any similar third-party tracker.</p>`],
      ["Cookies", `<p>We set one first-party cookie (<code>tr-theme</code>) to remember your dark / light mode preference. It never leaves your browser and is not used for tracking. We set no other cookies.</p>`],
      ["Children's privacy", `<p>${BRAND} is not directed at children under 13. We do not knowingly collect personal information from anyone in that age group.</p>`],
      ["International users and GDPR", `<p>Because we do not collect personal data as defined by the GDPR, there is nothing to export, rectify, or erase. You exercise your rights simply by not using the service. If you have specific questions, email <a href="mailto:privacy@${BRAND}">privacy@${BRAND}</a>.</p>`],
      ["Changes to this policy", `<p>We will post any material changes to this policy on this page with a revised "Last updated" date. Continuing to use the service after changes are posted constitutes acceptance.</p>`],
    ],
    faqs: [
      ["Do you sell my data?", "No. We have no advertising partners, affiliate deals, or data brokers."],
      ["Do you share data with YouTube or Google?", "We send the YouTube URL to YouTube's public endpoints to fetch the video. We do not share your IP with YouTube — their logs see our server's IP, not yours."],
      ["Is my IP stored?", "Only in short-lived server logs (max 14 days) for abuse prevention."],
      ["Do you have any analytics?", "No third-party analytics. We use only aggregate request counts from our hosting provider."],
    ],
  },

  // =================================================================
  // TERMS
  // =================================================================
  { slug: "terms-of-use", title: "Terms of Use", h1: "Terms of Use",
    kicker: "The rules you agree to by using " + BRAND + ".",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: BRAND + " terms, " + BRAND + " tos, youtube converter terms",
    sections: [
      ["Acceptance of terms", `<p>By using ${BRAND}, you agree to these terms. If you do not agree, do not use the service.</p>`],
      ["Acceptable use", `<ul><li>Do not use ${BRAND} to convert content you do not have the right to download.</li><li>Do not attempt to circumvent rate limits, abuse the API, or resell access.</li><li>Do not use the service for commercial redistribution of copyrighted material.</li><li>Do not attempt to upload, inject, or host malicious content through the URL field.</li></ul>`],
      ["Intellectual property", `<p>${BRAND} does not claim ownership over any content you convert. The video and audio remain the intellectual property of their original rights-holders. The ${BRAND} brand, site design, and code are the property of the ${BRAND} team.</p>`],
      ["Disclaimer of warranties", `<p>The service is provided "as is" without warranty of any kind. We do not guarantee uninterrupted availability, compatibility with any specific video, or any specific quality level.</p>`],
      ["Limitation of liability", `<p>To the maximum extent permitted by law, ${BRAND} and its operators are not liable for indirect, incidental, or consequential damages arising from the use or inability to use the service.</p>`],
      ["Changes to the service", `<p>We may change, suspend, or terminate the service at any time without notice.</p>`],
      ["Governing law", `<p>These terms are governed by the laws of the jurisdiction where ${BRAND} is operated, without regard to conflict-of-laws principles.</p>`],
      ["Contact", `<p>Questions about these terms: <a href="mailto:legal@${BRAND}">legal@${BRAND}</a>.</p>`],
    ],
    faqs: [
      ["When were these terms last updated?", "See the date at the bottom of this page. We post changes here, not by email."],
      ["Can I scrape the site?", "No. Please don't — our anti-abuse systems may flag it and there's no upside for anyone."],
    ],
  },
];

// ---------- Shared template ----------
function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }

function header() {
  return `<header class="site-header"><div class="container header-row"><a class="brand" href="/" aria-label="${BRAND} home">yt2mp3<span class="brand-dot">.lol</span></a><div class="header-actions"><button type="button" class="btn-supporter" aria-label="Support"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 2l2.5 6L21 9l-5 4.5L17.5 20 12 16.8 6.5 20 8 13.5 3 9l6.5-1L12 2z" fill="currentColor"/></svg><span class="s-label">Supporter</span></button><details class="lang-menu"><summary class="btn-lang" role="button" aria-label="Language"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18" stroke="currentColor" stroke-width="1.5" fill="none"/></svg><span class="l-label">English</span><svg width="10" height="10" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></summary><div class="lang-list" role="menu"><a role="menuitem" href="#" class="lang-active">English</a><a role="menuitem" href="#">العربية</a><a role="menuitem" href="#">বাংলা</a><a role="menuitem" href="#">Deutsch</a><a role="menuitem" href="#">Español</a><a role="menuitem" href="#">Filipino</a><a role="menuitem" href="#">Français</a><a role="menuitem" href="#">हिन्दी</a><a role="menuitem" href="#">Bahasa Indonesia</a><a role="menuitem" href="#">Italiano</a><a role="menuitem" href="#">日本語</a><a role="menuitem" href="#">한국어</a><a role="menuitem" href="#">Bahasa Melayu</a><a role="menuitem" href="#">မြန်မာ</a><a role="menuitem" href="#">Português</a><a role="menuitem" href="#">Русский</a><a role="menuitem" href="#">ภาษาไทย</a><a role="menuitem" href="#">Türkçe</a><a role="menuitem" href="#">اردو</a><a role="menuitem" href="#">Tiếng Việt</a></div></details><button type="button" class="btn-theme" id="theme-toggle" aria-label="Toggle theme" title="Toggle theme"><svg class="icon-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M20 14.5A8 8 0 019.5 4 8 8 0 1020 14.5z" fill="currentColor"/></svg><svg class="icon-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="4" fill="currentColor"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.5 4.5l2 2M17.5 17.5l2 2M4.5 19.5l2-2M17.5 6.5l2-2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button></div></div></header>`;
}

function footer() {
  return `<footer class="site-footer"><div class="container"><nav class="footer-nav" aria-label="Footer primary"><a href="/youtube-to-mp4-converter">YouTube to MP4</a><a href="/youtube-playlist-downloader">Playlist Downloader</a><a href="/youtube-shorts-downloader">Shorts Downloader</a><a href="/youtube-multi-downloader">Multiple Download</a><a href="/youtube-to-mp3-320kbps-converter">MP3 320kbps</a><a href="/how-to-install">How to Install</a><a href="/faq">FAQ</a><a href="/about">About</a><a href="/contact">Contact</a></nav><nav class="footer-nav footer-legal" aria-label="Footer legal"><a href="/copyright-claims">Copyright Claims</a><a href="/privacy-policy">Privacy Policy</a><a href="/terms-of-use">Terms of Use</a></nav><p class="footer-copy">&copy; <span id="year"></span> ${BRAND}. Not affiliated with YouTube or Google.</p></div></footer>`;
}

function converterCard(variant = "single", titleOverride) {
  const title = titleOverride || (variant === "multi" ? `${BRAND_SHORT} - YouTube Multi Downloader` : `${BRAND_SHORT} - YouTube to MP3`);
  const input = variant === "multi"
    ? `<div class="url-wrap url-wrap-multi">
      <textarea id="yt-url-multi" name="urls" rows="5" placeholder="Paste YouTube URLs here (one per line).\nhttps://youtube.com/watch?v=VID_1\nhttps://youtube.com/watch?v=VID_2" aria-label="Paste multiple YouTube links" spellcheck="false"></textarea>
      <button type="button" id="paste-btn-multi" aria-label="Paste from clipboard" title="Paste"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="8" y="3" width="8" height="4" rx="1" stroke="currentColor" stroke-width="1.8"/><path d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V7a2 2 0 00-2-2h-2" stroke="currentColor" stroke-width="1.8" fill="none"/></svg></button>
    </div>`
    : `<div class="url-wrap">
      <input id="yt-url" name="url" type="url" inputmode="url" placeholder="Paste YouTube URL or search keywords" aria-label="Paste a YouTube link" required autocomplete="off" spellcheck="false">
      <button type="button" id="paste-btn" aria-label="Paste from clipboard" title="Paste"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="8" y="3" width="8" height="4" rx="1" stroke="currentColor" stroke-width="1.8"/><path d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V7a2 2 0 00-2-2h-2" stroke="currentColor" stroke-width="1.8" fill="none"/></svg></button>
    </div>`;
  return `<div id="converter" class="converter-card${variant === "multi" ? " converter-multi" : ""}" role="region" aria-label="YouTube converter" data-variant="${variant}">
  <h2 class="converter-title">${title}</h2>
  <form id="convert-form" autocomplete="off" novalidate>
    ${input}
    <div class="controls-row">
      <div class="seg" role="tablist" aria-label="Output format"><button type="button" class="seg-btn active" role="tab" aria-selected="true" data-format="mp3">MP3</button><button type="button" class="seg-btn" role="tab" aria-selected="false" data-format="mp4">MP4</button></div>
      <label for="quality" class="sr-only">Quality</label>
      <select id="quality" class="select-pill" aria-label="Quality"></select>
      <details class="track-menu"><summary class="track-pill" role="button" aria-label="Audio track"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="9" y="3" width="6" height="12" rx="3" fill="currentColor"/><path d="M5 11a7 7 0 0014 0M12 18v3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span id="track-label">Origin</span><svg width="10" height="10" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></summary><div class="track-list" role="menu"><button type="button" class="track-opt" data-track="" role="menuitem">Origin (default)</button><p class="track-note">Multi-track videos expose alternate audio languages here after you paste the URL.</p></div></details>
      <div class="spacer"></div>
      <button id="convert-btn" type="submit">Convert</button>
    </div>
    <div id="status" class="status hidden" aria-live="polite"></div>
  </form>
</div>`;
}

function renderLandingPage(p) {
  const sectionsHtml = p.sections.map((s, i) =>
    `<section class="section${i % 2 ? " alt" : ""}"><div class="container"><h2>${esc(s[0])}</h2>${s[1]}</div></section>`
  ).join("\n");
  const faqsHtml = p.faqs && p.faqs.length
    ? `<section class="section"><div class="container"><h2>Frequently Asked Questions</h2>${p.faqs.map(f => `<details class="faq-item"><summary>${esc(f[0])}</summary><p>${esc(f[1])}</p></details>`).join("")}</div></section>`
    : "";
  const faqLd = p.faqs && p.faqs.length
    ? `<script type="application/ld+json">${JSON.stringify({ "@context": "https://schema.org", "@type": "FAQPage", mainEntity: p.faqs.map(f => ({ "@type": "Question", name: f[0], acceptedAnswer: { "@type": "Answer", text: f[1] } })) })}</script>`
    : "";
  const variant = p.variant || "single";

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0b0d14" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#f3f4f9" media="(prefers-color-scheme: light)">
<title>${esc(p.title)} - ${BRAND}</title>
<meta name="description" content="${esc(p.kicker)}">
<meta name="keywords" content="${esc(p.keywords)}">
<link rel="canonical" href="${SITE}/${p.slug}">
<meta property="og:title" content="${esc(p.title)}">
<meta property="og:description" content="${esc(p.kicker)}">
<meta property="og:type" content="website">
<meta property="og:url" content="${SITE}/${p.slug}">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="stylesheet" href="/assets/style.css">
<script>(function(){try{var t=localStorage.getItem("tr-theme");if(t)document.documentElement.setAttribute("data-theme",t);}catch(e){}})();</script>
${faqLd}
</head>
<body>
<a href="#converter" class="skip">Skip to converter</a>
${header()}
<main>
<section class="hero">
  <div class="container">
    <p class="crumb"><a href="/">&larr; Home</a></p>
    <h1 class="page-h1">${esc(p.h1)}</h1>
    <p class="page-kicker">${esc(p.kicker)}</p>
    ${converterCard(variant)}
  </div>
</section>
${sectionsHtml}
${faqsHtml}
</main>
${footer()}
<script>window.__DEFAULT_FORMAT__=${JSON.stringify(p.defaultFormat)};window.__DEFAULT_QUALITY__=${JSON.stringify(p.defaultQuality)};</script>
<script src="/assets/app.js" defer></script>
</body>
</html>
`;
}

// Emit each page at web/<slug>/index.html for clean URLs on any static host.
for (const p of PAGES) {
  const dir = path.join(WEB, p.slug);
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, "index.html"), renderLandingPage(p));
  console.log("wrote", p.slug + "/index.html");
}

// Emit sitemap.
const urls = [
  { loc: "/", pri: "1.0", freq: "daily" },
  ...PAGES.filter(p => !["privacy-policy", "terms-of-use", "copyright-claims", "contact"].includes(p.slug))
    .map(p => ({ loc: "/" + p.slug, pri: ["youtube-to-mp4-converter", "youtube-shorts-downloader", "youtube-to-mp3-320kbps-converter", "youtube-playlist-downloader", "youtube-multi-downloader"].includes(p.slug) ? "0.9" : "0.8", freq: "weekly" })),
  ...PAGES.filter(p => ["privacy-policy", "terms-of-use", "copyright-claims", "contact"].includes(p.slug))
    .map(p => ({ loc: "/" + p.slug, pri: "0.4", freq: "yearly" })),
];
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map(u => `  <url><loc>${SITE}${u.loc}</loc><priority>${u.pri}</priority><changefreq>${u.freq}</changefreq></url>`).join("\n")}
</urlset>
`;
fs.writeFileSync(path.join(WEB, "sitemap.xml"), sitemap);
console.log("wrote sitemap.xml");
