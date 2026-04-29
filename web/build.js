#!/usr/bin/env node
/* Generates SEO landing pages from a shared template.
 * Run: node build.js
 */
const fs = require("fs");
const path = require("path");

const WEB = path.resolve(__dirname);
const OUT = path.join(WEB, "pages");
fs.mkdirSync(OUT, { recursive: true });

const PAGES = [
  {
    slug: "mp4",
    title: "YouTube to MP4 Converter (1080p & 4K, Free) — TuneRip",
    h1: "YouTube to MP4 Converter",
    kicker: "Download any YouTube video as MP4 in 360p, 720p, 1080p, or 4K. Free, fast, no signup.",
    defaultFormat: "mp4",
    defaultQuality: "1080",
    keywords: "youtube to mp4, youtube mp4 converter, youtube mp4 downloader, youtube to 1080p, youtube to 4k",
    sections: [
      ["Save YouTube videos as MP4 in seconds", `MP4 is the universally-compatible container for H.264 video and AAC audio — it plays on every phone, tablet, TV, and editor. TuneRip pulls the highest-quality MP4 streams YouTube serves, merges them with FFmpeg, and hands you a single file that's ready for offline viewing, archiving, or video editing.`],
      ["Available resolutions", `We always select the best track that matches your chosen height. 360p and 720p are the safest bet for small phones and slow connections. 1080p is the sweet spot for laptops and TVs. 1440p and 2160p (4K) are exported when the original video was uploaded at those resolutions — for most talking-head and music videos, 1080p is the ceiling.`],
      ["How to download YouTube as MP4", `Copy the video URL from YouTube's share menu or your browser address bar, paste it into the converter above, select MP4 and your preferred resolution, then click Convert. Processing time scales with length and resolution — a three-minute 1080p clip typically takes under 10 seconds.`],
      ["Does it work for Shorts and live replays?", `Yes. Shorts export in their native vertical aspect ratio. Live stream replays (VODs) work once YouTube has finished processing them, usually within minutes of the stream ending.`],
    ],
    faqs: [
      ["What is the highest MP4 quality you support?", "2160p (4K) when the source offers it. We transparently fall back to the best available height otherwise."],
      ["Does the MP4 include audio?", "Yes. Video and audio tracks are merged into a single MP4 with H.264 video and AAC audio."],
      ["Is the MP4 watermark-free?", "Yes. We do not add watermarks, overlays, or trailers to the file."],
    ],
  },
  {
    slug: "shorts",
    title: "YouTube Shorts Downloader (MP3 & MP4) — TuneRip",
    h1: "YouTube Shorts Downloader",
    kicker: "Save YouTube Shorts as MP3 audio or MP4 video in seconds. Original vertical aspect ratio preserved.",
    defaultFormat: "mp4",
    defaultQuality: "1080",
    keywords: "youtube shorts downloader, shorts to mp3, shorts to mp4, download youtube shorts, save youtube shorts",
    sections: [
      ["Download YouTube Shorts without an app", `Shorts are just YouTube videos under a minute, so TuneRip handles them with the same pipeline as full-length clips. Paste a Shorts URL (anything matching youtube.com/shorts/…), pick MP3 or MP4, and the file is yours in seconds.`],
      ["Shorts keep their vertical framing", `We export MP4 in the original 9:16 portrait aspect ratio whenever the uploader filmed that way. Nothing is cropped, stretched, or re-centered, so the Short looks identical offline.`],
      ["Grab the audio only", `Some Shorts are really short songs, remixes, or memes — pick MP3 at 320 kbps and you'll get the audio without the video wrapper. Useful for making ringtones, memes, or sample libraries.`],
    ],
    faqs: [
      ["Can I download a Shorts channel's entire feed?", "Yes, if you can create a playlist containing those Shorts. Paste the playlist URL into the converter and every video will be processed individually."],
      ["Why does my Short look blurry?", "Shorts are often uploaded at lower resolutions by creators. We pull the highest resolution available; if that's 720p or less, the download will reflect that."],
    ],
  },
  {
    slug: "playlist",
    title: "YouTube Playlist Downloader (MP3 & MP4 Batch) — TuneRip",
    h1: "YouTube Playlist Downloader",
    kicker: "Convert an entire YouTube playlist to MP3 or MP4 in one click. Each video downloads as its own file.",
    defaultFormat: "mp3",
    defaultQuality: "320",
    keywords: "youtube playlist downloader, playlist to mp3, youtube playlist to mp4, batch youtube converter",
    sections: [
      ["Bulk-convert every video in a playlist", `Paste any public YouTube playlist URL (for example ?list=PL…) and TuneRip queues every video individually. Each conversion runs in parallel where possible, so even long playlists finish quickly. You'll get one clean file per video, named with the original title.`],
      ["Supports mixes and topic playlists", `Auto-generated mixes, Topic artist playlists, and user-curated playlists all work as long as they're set to Public or Unlisted. Private playlists won't resolve.`],
      ["Picking the right format for a playlist", `For music playlists, MP3 at 320 kbps is the standard. For podcast-style playlists, M4A produces smaller files at equal quality. For lecture series you plan to re-watch, MP4 at 720p keeps storage reasonable without sacrificing clarity.`],
    ],
    faqs: [
      ["Is there a maximum playlist length?", "No hard cap, but very large playlists (500+ videos) may take several minutes to process in full."],
      ["Are playlists downloaded in order?", "Yes. We preserve the creator's playlist ordering by default."],
    ],
  },
  {
    slug: "320kbps",
    title: "YouTube to MP3 320kbps Converter — TuneRip",
    h1: "YouTube to MP3 at 320 kbps",
    kicker: "True 320 kbps constant bitrate MP3 re-encoded with FFmpeg — not a padded fake.",
    defaultFormat: "mp3",
    defaultQuality: "320",
    keywords: "youtube to 320kbps, youtube to mp3 320kbps, high quality youtube mp3, 320 kbps converter",
    sections: [
      ["What 320 kbps actually means", `320 kbps is the highest bitrate allowed by the MP3 codec. At this rate, compression artifacts are very close to inaudible for most material. TuneRip uses FFmpeg's libmp3lame at CBR 320 kbps with joint stereo, which is the standard configuration for high-quality music MP3s.`],
      ["Why many converters lie about bitrate", `Some sites advertise "320 kbps" but re-package a lower-bitrate file with a higher bitrate header. The file sounds identical to the 128 kbps source. We re-encode from the best source stream YouTube offers (typically 160 kbps Opus) so the tag and the content match.`],
      ["When to pick WAV or FLAC instead", `If you're mastering, looping, or sampling the audio, even 320 kbps lossy compression can stack up. Choose WAV from the format tabs for a lossless export, at the cost of roughly 10x the file size.`],
    ],
    faqs: [
      ["Will 320 kbps make a 128 kbps source sound better?", "No — you can't add information that isn't there. 320 kbps just ensures our re-encode doesn't add further compression loss."],
      ["Is 320 kbps audible difference vs 192 kbps?", "On good headphones with dense material (rock mixes, orchestral), yes. On earbuds with pop or speech, usually not."],
    ],
  },
  {
    slug: "wav",
    title: "YouTube to WAV Converter (Lossless) — TuneRip",
    h1: "YouTube to WAV Converter",
    kicker: "Export YouTube audio as uncompressed 16-bit 44.1kHz WAV for editing, sampling, or archival.",
    defaultFormat: "wav",
    defaultQuality: "320",
    keywords: "youtube to wav, youtube wav converter, lossless youtube audio, wav download youtube",
    sections: [
      ["Uncompressed WAV for producers", `WAV is an uncompressed PCM container — perfect for loading into a DAW, chopping into samples, or archiving speech without generational loss. TuneRip decodes the source audio once and writes a 16-bit 44.1 kHz stereo WAV, matching the CD audio standard.`],
      ["Note on source quality", `WAV does not improve audio beyond the original YouTube stream. If the uploader submitted a 128 kbps MP3, your WAV is a lossless container around a lossy source. For pristine sources (official music channels, live recordings), WAV preserves everything that's there.`],
    ],
    faqs: [
      ["How large will a WAV file be?", "Roughly 10 MB per minute at 16-bit 44.1 kHz stereo."],
      ["Is WAV supported on iPhone?", "Yes, QuickTime and most iOS apps handle WAV. For mobile listening, MP3 or M4A is more practical."],
    ],
  },
  {
    slug: "m4a",
    title: "YouTube to M4A (AAC) Converter — TuneRip",
    h1: "YouTube to M4A Converter",
    kicker: "Export YouTube audio as M4A (AAC) — the most efficient audio format for Apple devices.",
    defaultFormat: "m4a",
    defaultQuality: "320",
    keywords: "youtube to m4a, youtube m4a converter, aac youtube download, youtube to aac",
    sections: [
      ["M4A = AAC in an MP4 container", `M4A is the native audio format used by Apple Music and the iTunes Store. At any given bitrate, AAC sounds noticeably better than MP3, especially at lower rates like 128 kbps. If you're listening on iPhone, iPad, Mac, or HomePod, M4A is the smarter default.`],
      ["Direct mux where possible", `YouTube's native audio stream is already AAC for most videos. When that's the case, we simply re-mux the AAC bitstream into an M4A container without re-encoding — meaning zero generation loss and near-instant processing.`],
    ],
    faqs: [
      ["Can Android play M4A?", "Yes. Android has supported M4A/AAC natively since version 3."],
      ["Does M4A include album art?", "We embed the video thumbnail as cover art whenever the source provides one."],
    ],
  },
  {
    slug: "iphone",
    title: "YouTube to MP3 on iPhone (No App) — TuneRip",
    h1: "YouTube to MP3 on iPhone",
    kicker: "Convert YouTube to MP3 directly on iPhone or iPad — no App Store install required.",
    defaultFormat: "mp3",
    defaultQuality: "320",
    keywords: "youtube to mp3 iphone, iphone youtube converter, safari youtube mp3, ios youtube to mp3",
    sections: [
      ["Works entirely in Safari", `Apple restricts apps that download YouTube content, so App Store tools are limited. TuneRip runs in mobile Safari — open the YouTube app, tap Share → Copy Link, switch to Safari, paste into the converter, pick MP3 or MP4, and tap Convert.`],
      ["Saving to the Files app", `When the download finishes, Safari will prompt you to save the file. Choose "Save to Files" and pick a folder on iCloud Drive or On My iPhone. From there the MP3 shows up in any audio app that reads the Files app (VLC, Documents by Readdle, etc.).`],
      ["Adding to your Music library", `To play the MP3 in the Music app, use a free tool like WALTR or the Finder on macOS to sync it. iOS itself doesn't let Safari drop files directly into the Apple Music library.`],
    ],
    faqs: [
      ["Do I need a jailbreak?", "No. Everything happens in the browser on a stock iPhone."],
      ["Can I use Shortcuts to automate this?", "Yes — you can build a Shortcut that takes a shared URL and opens our converter with it pre-filled."],
    ],
  },
  {
    slug: "android",
    title: "YouTube to MP3 on Android — TuneRip",
    h1: "YouTube to MP3 on Android",
    kicker: "Fast YouTube conversion on any Android phone through Chrome, Firefox, or Samsung Internet.",
    defaultFormat: "mp3",
    defaultQuality: "320",
    keywords: "youtube to mp3 android, android youtube converter, chrome youtube mp3, samsung internet youtube",
    sections: [
      ["Zero-install workflow", `Open the YouTube app, tap Share on the video, and choose Copy link. Open Chrome (or your favorite Android browser) and go to TuneRip. Paste the URL, pick MP3 or MP4, and tap Convert. Android's download manager will save the file into your Downloads folder automatically.`],
      ["Integrate with your music player", `Downloaded MP3s are picked up automatically by most Android music players that scan the Downloads or Music folder. Apps like Poweramp, Musicolet, Phonograph, and VLC find them instantly. You can also long-press the file in Files by Google to move it into a custom folder.`],
    ],
    faqs: [
      ["Does this work on Samsung Internet and Firefox?", "Yes. The site uses standard web APIs and works in every modern Android browser."],
      ["Do I need storage permission?", "The browser handles downloads; you do not need to grant extra permissions to TuneRip."],
    ],
  },
  {
    slug: "faq",
    title: "TuneRip FAQ — YouTube Converter Questions",
    h1: "Frequently Asked Questions",
    kicker: "Everything you might want to know about TuneRip's YouTube converter.",
    defaultFormat: "mp3",
    defaultQuality: "320",
    keywords: "ytmp3 faq, youtube converter questions, youtube to mp3 help",
    sections: [
      ["Is the service really free?", `Yes, completely. No ads, no pop-ups, no email gates, no trial limits. We may add an optional Pro tier later for priority processing queues, but the core converter stays free.`],
      ["Do you store my conversions?", `No. Temporary files live on disk only long enough for you to download them (usually less than 30 minutes) and are wiped automatically by a background cleanup job. We do not keep logs of which URLs users convert.`],
      ["Why did my conversion fail?", `The most common causes are: the video is private or age-restricted without an account, YouTube is rate-limiting our server (retry in a minute), the video was removed, or the URL is malformed. Try another link or a different quality.`],
      ["Do you support live streams?", `Only finished VODs (past broadcasts). Live streams in progress can't be converted because they don't have a fixed length yet.`],
      ["Are there length limits?", `We cap conversions at three hours by default. Contact us if you need longer conversions for a specific use case.`],
    ],
    faqs: [],
  },
  {
    slug: "about",
    title: "About TuneRip — Free YouTube Converter",
    h1: "About TuneRip",
    kicker: "A minimalist, ad-free YouTube converter focused on speed, clarity, and privacy.",
    defaultFormat: "mp3",
    defaultQuality: "320",
    keywords: "about ytmp3 alternative, tunerip about, youtube converter about",
    sections: [
      ["Why we built this", `Most YouTube converters are buried in pop-ups, redirect chains, and fake download buttons. We wanted something that does one job — link in, file out — with zero friction. TuneRip is that.`],
      ["How it works under the hood", `The frontend is a static, pre-rendered site hosted on a CDN for instant load. The backend runs yt-dlp to resolve the best available YouTube streams, then FFmpeg to package them as MP3 (libmp3lame CBR), M4A (AAC re-mux), WAV (PCM), or MP4 (H.264 + AAC). Jobs are processed asynchronously so the UI stays responsive.`],
      ["Responsible use", `TuneRip is intended for downloading content that you have the right to save — your own uploads, Creative Commons material, public-domain works, or content you've licensed. Please respect the terms of the platforms you use and the copyright of the creators whose work you enjoy.`],
    ],
    faqs: [],
  },
];

const FORMAT_TABS = ["mp3", "m4a", "wav", "ogg", "opus", "mp4"];

function renderPage(p) {
  const tabsHtml = FORMAT_TABS
    .map(
      (f) =>
        `<button type="button" class="tab${
          f === p.defaultFormat ? " active" : ""
        }" role="tab" aria-selected="${f === p.defaultFormat ? "true" : "false"}" data-format="${f}">${f.toUpperCase()}</button>`
    )
    .join("\n            ");

  const sectionsHtml = p.sections
    .map(
      (s, i) =>
        `<section class="section${i % 2 ? " alt" : ""}"><div class="container narrow"><h2>${escape(
          s[0]
        )}</h2><p>${escape(s[1])}</p></div></section>`
    )
    .join("\n");

  const faqsHtml = p.faqs && p.faqs.length
    ? `<section class="section"><div class="container narrow"><h2>FAQ</h2>${p.faqs
        .map(
          (f) =>
            `<details><summary>${escape(f[0])}</summary><p>${escape(f[1])}</p></details>`
        )
        .join("")}</div></section>`
    : "";

  const faqLd = p.faqs && p.faqs.length
    ? `<script type="application/ld+json">${JSON.stringify({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        mainEntity: p.faqs.map((f) => ({
          "@type": "Question",
          name: f[0],
          acceptedAnswer: { "@type": "Answer", text: f[1] },
        })),
      })}</script>`
    : "";

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>${escape(p.title)}</title>
<meta name="description" content="${escape(p.kicker)}" />
<meta name="keywords" content="${escape(p.keywords)}" />
<link rel="canonical" href="https://example.com/pages/${p.slug}.html" />
<meta property="og:title" content="${escape(p.title)}" />
<meta property="og:description" content="${escape(p.kicker)}" />
<meta property="og:type" content="website" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="robots" content="index,follow,max-image-preview:large" />
<meta name="theme-color" content="#0b1020" />
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/style.css" />
${faqLd}
</head>
<body>
<a href="#converter" class="skip">Skip to converter</a>
<header class="site-header">
  <div class="container header-row">
    <a class="brand" href="/" aria-label="TuneRip home"><span class="brand-mark" aria-hidden="true"></span><span class="brand-text">TuneRip</span></a>
    <nav class="nav" aria-label="Primary">
      <a href="/pages/mp4.html">YouTube to MP4</a>
      <a href="/pages/shorts.html">Shorts</a>
      <a href="/pages/playlist.html">Playlist</a>
      <a href="/pages/320kbps.html">320kbps</a>
      <a href="/pages/faq.html">FAQ</a>
    </nav>
  </div>
</header>
<main>
<section class="hero">
  <div class="container">
    <p><a href="/">&larr; Home</a></p>
    <h1>${escape(p.h1)}</h1>
    <p class="lede">${escape(p.kicker)}</p>
    <div id="converter" class="converter" role="region" aria-label="YouTube converter">
      <form id="convert-form" class="convert-form" autocomplete="off" novalidate>
        <label for="yt-url" class="sr-only">YouTube URL</label>
        <div class="input-row">
          <input id="yt-url" name="url" type="url" inputmode="url" placeholder="https://www.youtube.com/watch?v=..." aria-label="Paste a YouTube link" required />
          <button type="button" id="paste-btn" class="btn-ghost" title="Paste from clipboard">Paste</button>
        </div>
        <div class="options">
          <div class="tabs" role="tablist" aria-label="Output format">
            ${tabsHtml}
          </div>
          <label for="quality" class="sr-only">Quality</label>
          <select id="quality" aria-label="Quality"></select>
          <button id="convert-btn" type="submit" class="btn-primary">Convert</button>
        </div>
      </form>
      <div id="status" class="status hidden" aria-live="polite"></div>
    </div>
  </div>
</section>
${sectionsHtml}
${faqsHtml}
</main>
<footer class="site-footer">
  <div class="container footer-row">
    <p>&copy; <span id="year"></span> TuneRip. Not affiliated with YouTube or Google.</p>
    <nav aria-label="Footer">
      <a href="/pages/faq.html">FAQ</a>
      <a href="/pages/about.html">About</a>
      <a href="/pages/mp4.html">YouTube to MP4</a>
      <a href="/pages/shorts.html">Shorts</a>
      <a href="/pages/playlist.html">Playlist</a>
      <a href="/pages/320kbps.html">320kbps</a>
    </nav>
  </div>
</footer>
<script>window.__DEFAULT_FORMAT__=${JSON.stringify(p.defaultFormat)};window.__DEFAULT_QUALITY__=${JSON.stringify(p.defaultQuality)};</script>
<script src="/assets/app.js" defer></script>
</body>
</html>
`;
}

function escape(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

for (const p of PAGES) {
  const html = renderPage(p);
  fs.writeFileSync(path.join(OUT, p.slug + ".html"), html);
  console.log("wrote", p.slug + ".html");
}
