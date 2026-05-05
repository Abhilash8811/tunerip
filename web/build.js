#!/usr/bin/env node
/* Generates SEO landing pages + legal pages from one template.
 * Emits web/<slug>/index.html so URLs are clean on any static host.
 * Run: node build.js
 */
const fs = require("fs");
const path = require("path");

const currentDate = new Date().toISOString().split('T')[0];
const WEB = path.resolve(__dirname);
const SITE = "https://yt2mp3.lol";
const BRAND = "yt2mp3.lol";

// Check if building for Vercel (no canonical tags for independent indexing)
const IS_VERCEL_BUILD = process.env.VERCEL === '1' || process.argv.includes('--vercel');

// URL slugs mirror yt2mp3.lol's structure so SEO equity transfers.
const PAGES = [
  { slug: "youtube-to-mp4-converter", title: "YouTube to MP4 Converter (1080p & 4K, Free)", h1: "YouTube to MP4 Converter",
    converterTitle: "YouTube to MP4 Converter",
    kicker: "Download any YouTube video as MP4 in 360p, 720p, 1080p, or 4K. Free, fast, no signup.",
    defaultFormat: "mp4", defaultQuality: "1080",
    keywords: "youtube to mp4, youtube mp4 converter, youtube mp4 downloader, youtube to 1080p, youtube to 4k",
    sections: [
      ["Save YouTube videos as MP4 in seconds", `MP4 is the universally-compatible container for H.264 video and AAC audio — it plays on every phone, tablet, TV, and video editor. ${BRAND} pulls the highest-quality MP4 streams YouTube serves, merges them with FFmpeg, and hands you a single file that's ready for offline viewing, archiving, or editing.`],
      ["Available resolutions", "We always select the best track that matches your chosen height. 360p and 720p are the safest bet for small phones and slow connections. 1080p is the sweet spot for laptops and TVs. 1440p and 2160p (4K) are exported when the original video was uploaded at those resolutions."],
      ["How to download YouTube as MP4", "Copy the video URL from YouTube's share menu or your browser address bar, paste it into the converter, select MP4 and your preferred resolution, then click Convert. A three-minute 1080p clip typically takes under 10 seconds."],
      ["Shorts and live replays", "Shorts export in their native vertical aspect ratio. Live stream replays (VODs) work once YouTube has finished processing them, usually within minutes of the stream ending."],
    ],
    faqs: [
      ["What is the highest MP4 quality you support?", "2160p (4K) when the source offers it. Falls back to the best available height otherwise."],
      ["Does the MP4 include audio?", "Yes. Video and audio tracks are merged into a single MP4 with H.264 video and AAC audio."],
      ["Is the MP4 watermark-free?", "Yes. No watermarks, overlays, or trailers are added to the file."],
    ] },
  { slug: "youtube-shorts-downloader", title: "YouTube Shorts Downloader (MP3 & MP4)", h1: "YouTube Shorts Downloader",
    converterTitle: "YouTube Shorts Downloader",
    kicker: "Save YouTube Shorts as MP3 audio or MP4 video in seconds. Original vertical aspect ratio preserved.",
    defaultFormat: "mp4", defaultQuality: "1080",
    keywords: "youtube shorts downloader, shorts to mp3, shorts to mp4, download youtube shorts, save youtube shorts",
    sections: [
      ["Download YouTube Shorts without an app", `Shorts are just YouTube videos under a minute, so ${BRAND} handles them through the same pipeline as full-length clips. Paste a Shorts URL (anything matching youtube.com/shorts/…), pick MP3 or MP4, and the file is yours in seconds.`],
      ["Shorts keep their vertical framing", "We export MP4 in the original 9:16 portrait aspect ratio whenever the uploader filmed that way. Nothing is cropped, stretched, or re-centered, so the Short looks identical offline."],
      ["Grab the audio only", "Some Shorts are just short songs, remixes, or memes — pick MP3 at 320 kbps and you get the audio without the video wrapper. Useful for making ringtones, memes, or sample libraries."],
    ],
    faqs: [
      ["Can I download a channel's entire Shorts feed?", "Yes, if you can create a playlist containing those Shorts. Paste the playlist URL and every video will be processed individually."],
      ["Why does my Short look blurry?", "Shorts are often uploaded at lower resolutions by creators. We pull the highest resolution available; if that's 720p, the download will reflect that."],
    ] },
  { slug: "youtube-playlist-downloader", title: "YouTube Playlist Downloader (MP3 & MP4 Batch)", h1: "YouTube Playlist Downloader",
    converterTitle: "YouTube Playlist Downloader",
    kicker: "Convert an entire YouTube playlist to MP3 or MP4 in one click. Each video downloads as its own file.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "youtube playlist downloader, playlist to mp3, youtube playlist to mp4, batch youtube converter",
    sections: [
      ["Bulk-convert every video in a playlist", `Paste any public YouTube playlist URL (for example ?list=PL…) and ${BRAND} queues every video individually. Each conversion runs in parallel where possible, so even long playlists finish quickly. You get one clean file per video, named with the original title.`],
      ["Supports mixes and topic playlists", "Auto-generated mixes, Topic artist playlists, and user-curated playlists all work as long as they're set to Public or Unlisted. Private playlists won't resolve."],
      ["Picking the right format", "For music, MP3 at 320 kbps is the standard. For podcasts, M4A produces smaller files at equal quality. For lecture series you plan to re-watch, MP4 at 720p balances storage and clarity."],
    ],
    faqs: [
      ["Is there a maximum playlist length?", "No hard cap, but very large playlists (500+ videos) may take several minutes to process in full."],
      ["Are playlists downloaded in order?", "Yes. Original playlist ordering is preserved by default."],
    ] },
  { slug: "youtube-multi-downloader", title: "Multiple YouTube Downloader (Batch Convert)", h1: "Multiple YouTube Downloader",
    converterTitle: "Multiple YouTube Downloader",
    kicker: "Paste several YouTube URLs at once and convert them all in parallel. Great for playlists, curated lists, and research workflows.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "multiple youtube downloader, batch youtube to mp3, bulk youtube converter, multi youtube download",
    sections: [
      ["Why batch is faster", "Instead of converting videos one at a time, paste multiple links separated by newlines or commas. The server processes each in parallel and hands you a download list when everything is ready. For 10 short videos this is roughly 5x faster than sequential conversion."],
      ["How to batch", "Open the converter, paste your first link and hit Enter, then paste the next on the following line. Press Convert when you're done — each URL is queued as its own job and shows independent progress."],
      ["Works with mixed formats", "You can choose one format (e.g. MP3 320 kbps) for the whole batch, or queue separate batches with different formats one after another. Combining playlists and loose URLs is fine."],
    ],
    faqs: [
      ["Is there a batch size limit?", "Soft limit of 50 URLs per batch to keep the server responsive for everyone. Larger batches can be split."],
      ["What if one URL fails?", "That job is marked failed and the rest keep running. You can retry just the failed URL."],
    ] },
  { slug: "youtube-to-mp3-320kbps-converter", title: "YouTube to MP3 320kbps Converter", h1: "YouTube to MP3 at 320 kbps",
    converterTitle: "YouTube to MP3 320kbps",
    kicker: "True 320 kbps constant bitrate MP3 re-encoded with FFmpeg — not a padded fake.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "youtube to 320kbps, youtube to mp3 320kbps, high quality youtube mp3, 320 kbps converter",
    sections: [
      ["What 320 kbps actually means", `320 kbps is the highest bitrate allowed by the MP3 codec. At this rate, compression artifacts are close to inaudible for most material. ${BRAND} uses FFmpeg's libmp3lame at CBR 320 kbps with joint stereo, which is the standard configuration for high-quality music MP3s.`],
      ["Why many converters fake bitrate", "Some sites advertise 320 kbps but re-package a lower-bitrate file with a higher bitrate header. The file sounds identical to the 128 kbps source. We re-encode from the best source stream YouTube offers (typically 160 kbps Opus) so the tag matches the actual bitrate."],
      ["When to pick WAV instead", "If you're mastering, looping, or sampling the audio, even 320 kbps lossy compression can stack up. Choose WAV for a lossless export at the cost of roughly 10x the file size."],
    ],
    faqs: [
      ["Will 320 kbps make a 128 kbps source sound better?", "No — you can't add information that isn't there. 320 kbps just ensures our re-encode doesn't add further compression loss."],
      ["Audible difference vs 192 kbps?", "On good headphones with dense material, yes. On earbuds with pop or speech, usually not."],
    ] },
  // Extras we keep for long-tail SEO value
  { slug: "wav-converter", title: "YouTube to WAV Converter (Lossless)", h1: "YouTube to WAV Converter",
    converterTitle: "YouTube to WAV Converter",
    kicker: "Export YouTube audio as uncompressed 16-bit 44.1kHz WAV for editing, sampling, or archival.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "youtube to wav, youtube wav converter, lossless youtube audio, wav download youtube",
    sections: [
      ["Uncompressed WAV for producers", `WAV is an uncompressed PCM container — ideal for loading into a DAW, chopping into samples, or archiving speech without generational loss. ${BRAND} decodes the source once and writes a 16-bit 44.1 kHz stereo WAV, matching CD audio.`],
      ["Note on source quality", "WAV does not improve audio beyond the original YouTube stream. For pristine sources (official music channels, live recordings), WAV preserves everything that's there."],
    ],
    faqs: [
      ["How large will a WAV file be?", "Roughly 10 MB per minute at 16-bit 44.1 kHz stereo."],
      ["Is WAV supported on iPhone?", "Yes. For mobile listening, MP3 or M4A is more practical."],
    ] },
  { slug: "m4a-converter", title: "YouTube to M4A (AAC) Converter", h1: "YouTube to M4A Converter",
    converterTitle: "YouTube to M4A Converter",
    kicker: "Export YouTube audio as M4A (AAC) — the most efficient audio format for Apple devices.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "youtube to m4a, youtube m4a converter, aac youtube download, youtube to aac",
    sections: [
      ["M4A = AAC in an MP4 container", "M4A is the native audio format used by Apple Music and the iTunes Store. At any given bitrate, AAC sounds noticeably better than MP3, especially at lower rates. For iPhone, iPad, Mac, or HomePod, M4A is the smarter default."],
      ["Direct mux where possible", "YouTube's native audio stream is already AAC for most videos. When that's the case, we simply re-mux the AAC bitstream into an M4A container without re-encoding — zero generation loss and near-instant processing."],
    ],
    faqs: [
      ["Can Android play M4A?", "Yes. Android has supported M4A/AAC natively since version 3."],
      ["Does M4A include album art?", "The video thumbnail is embedded as cover art when the source provides one."],
    ] },
  { slug: "iphone-converter", title: "YouTube to MP3 on iPhone (No App)", h1: "YouTube to MP3 on iPhone",
    converterTitle: "YouTube to MP3 on iPhone",
    kicker: "Convert YouTube to MP3 directly on iPhone or iPad — no App Store install required.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "youtube to mp3 iphone, iphone youtube converter, safari youtube mp3, ios youtube to mp3",
    sections: [
      ["Works entirely in Safari", `Apple restricts apps that download YouTube content, so App Store tools are limited. ${BRAND} runs in mobile Safari — open the YouTube app, tap Share → Copy Link, switch to Safari, paste into the converter, pick MP3 or MP4, and tap Convert.`],
      ["Saving to the Files app", "When the download finishes, Safari will prompt you to save the file. Choose 'Save to Files' and pick a folder on iCloud Drive or On My iPhone. From there the MP3 shows up in any audio app that reads the Files app."],
    ],
    faqs: [
      ["Do I need a jailbreak?", "No. Everything happens in the browser on a stock iPhone."],
      ["Can I automate this with Shortcuts?", "Yes — build a Shortcut that takes a shared URL and opens the converter with it pre-filled."],
    ] },
  { slug: "android-converter", title: "YouTube to MP3 on Android", h1: "YouTube to MP3 on Android",
    converterTitle: "YouTube to MP3 on Android",
    kicker: "Fast YouTube conversion on any Android phone through Chrome, Firefox, or Samsung Internet.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "youtube to mp3 android, android youtube converter, chrome youtube mp3, samsung internet youtube",
    sections: [
      ["Zero-install workflow", `Open the YouTube app, tap Share → Copy link. Open Chrome and go to ${BRAND}. Paste the URL, pick MP3 or MP4, and tap Convert. Android's download manager will save the file into your Downloads folder automatically.`],
      ["Integrate with your music player", "Downloaded MP3s are picked up automatically by most Android music players that scan the Downloads or Music folder — Poweramp, Musicolet, Phonograph, and VLC find them instantly."],
    ],
    faqs: [
      ["Does this work on Samsung Internet and Firefox?", "Yes. Works in every modern Android browser."],
      ["Do I need storage permission?", "No extra permissions needed — the browser handles downloads."],
    ] },
  { slug: "how-to-install", title: "How to Install - Add to Home Screen", h1: "How to Install",
    converterTitle: "Install YouTube Converter",
    kicker: `Add ${BRAND} to your phone's home screen so it opens like a native app. No App Store listing, no APK, no permissions beyond what the browser already has.`,
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "install ytmp3, add to home screen, ytmp3 app, youtube converter app",
    sections: [
      ["Install on iPhone / iPad", `Open ${BRAND} in Safari. Tap the Share button at the bottom of the screen, scroll down, and tap Add to Home Screen. Give it a name and tap Add. You now have a home-screen icon that opens the converter in a full-screen web app, without the browser chrome.`],
      ["Install on Android (Chrome)", "Open the site in Chrome. Tap the three-dot menu and pick Add to Home screen (or Install app if you see it). Confirm the name. Android installs a WebAPK that behaves like a regular app — including in the app drawer and recent apps switcher."],
      ["Install on desktop (Chrome, Edge, Brave)", "Look for the small install icon in the address bar (a monitor with a down arrow). Click it to install the site as a standalone desktop app. It gets its own Dock / Start menu entry and opens in a frameless window."],
      ["What you get", "The site runs faster on subsequent visits because assets are cached. It opens without browser tabs or menus, giving you more screen space for the converter. Your URL history stays inside the app and is never mixed with normal browsing."],
    ],
    faqs: [
      ["Does installing give it extra access to my phone?", "No. It runs in the same sandbox as any webpage. It only has access to the clipboard when you explicitly use the paste button."],
      ["Can I uninstall it easily?", "Yes. Long-press the icon and tap Delete (iOS) or Uninstall (Android) — same as any other app."],
    ] },
  { slug: "faq", title: `${BRAND} FAQ — YouTube Converter Questions`, h1: "Frequently Asked Questions",
    kicker: "Everything you might want to know about our YouTube converter.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "ytmp3 faq, youtube converter questions, youtube to mp3 help",
    sections: [
      ["Is the service really free?", "Yes, completely. No ads, no pop-ups, no email gates, no trial limits. We may add an optional Pro tier later for priority processing, but the core converter stays free."],
      ["Do you store my conversions?", "No. Temporary files live on disk only long enough for you to download them (usually less than 30 minutes) and are wiped automatically. We do not keep logs of which URLs users convert."],
      ["Why did my conversion fail?", "Most common causes: the video is private or age-restricted, YouTube is rate-limiting our server (retry in a minute), the video was removed, or the URL is malformed. Try another link or a different quality."],
      ["Do you support live streams?", "Only finished VODs (past broadcasts). Live streams in progress can't be converted because they don't have a fixed length yet."],
      ["Are there length limits?", "We cap conversions at three hours by default. Contact us if you need longer conversions for a specific use case."],
    ], faqs: [] },
  { slug: "about", title: `About ${BRAND}`, h1: `About ${BRAND}`,
    kicker: "A minimalist, ad-free YouTube converter focused on speed, clarity, and privacy.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "about ytmp3, youtube converter about",
    sections: [
      ["Why we built this", `Most YouTube converters are buried in pop-ups, redirect chains, and fake download buttons. We wanted something that does one job — link in, file out — with zero friction. ${BRAND} is that.`],
      ["How it works under the hood", "The frontend is a static, pre-rendered site hosted on a CDN for instant load. The backend runs yt-dlp to resolve the best available YouTube streams, then FFmpeg to package them as MP3 (libmp3lame CBR), M4A (AAC re-mux), WAV (PCM), or MP4 (H.264 + AAC). Jobs are processed asynchronously so the UI stays responsive."],
      ["Responsible use", `${BRAND} is intended for downloading content that you have the right to save — your own uploads, Creative Commons material, public-domain works, or content you've licensed. Please respect the terms of the platforms you use and the copyright of the creators whose work you enjoy.`],
    ], faqs: [] },
  { slug: "contact", title: `Contact ${BRAND}`, h1: "Contact",
    kicker: "Questions, feedback, bug reports, or business inquiries — pick the right channel below and we'll read every message.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "ytmp3 contact, contact support, youtube converter support",
    sections: [
      ["General support & bug reports", `Email support@${BRAND.replace("yt2mp3.lol", "yt2mp3.lol")} with a description of the issue, the URL you were converting, the format and quality you picked, and the browser / device you used. Screenshots help. We triage every inbound message within 48 hours.`],
      ["Copyright takedown requests", "If you own the rights to content you believe has been converted in violation of your copyright, please see the Copyright Claims page for the DMCA-style notice format we require. Misdirected takedown emails may be delayed — the dedicated form routes to our legal inbox immediately."],
      ["Business & partnerships", "For ad-free sponsorship, API licensing, or white-label inquiries, email partnerships at our domain with a short pitch and your contact details."],
    ],
    faqs: [
      ["Why haven't I received a reply?", "Check your spam folder. Our auto-reply sometimes lands there. If you're still not seeing anything after 72 hours, re-send from a different address."],
      ["Do you have a phone number?", "We operate asynchronously over email to keep operating costs low, which is what lets the service stay free."],
    ] },
  { slug: "copyright-claims", title: "Copyright Claims & DMCA Notices", h1: "Copyright Claims",
    converterTitle: "Copyright Claims",
    kicker: "If you believe content available through our service infringes your copyright, submit a notice using the format below and we will respond promptly.",
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "ytmp3 copyright, dmca notice, copyright claim, takedown request",
    sections: [
      ["Our approach", `${BRAND} hosts no content of its own. Files are generated on demand from URLs users supply and are deleted shortly after download. That said, we take copyright seriously and act on valid notices quickly.`],
      ["What to include in a notice", "A complete notice needs: (1) your contact information (name, address, email, phone); (2) identification of the copyrighted work you claim was infringed; (3) the specific URL(s) that were used with our converter and that you want us to block; (4) a good-faith statement that the use is not authorized; (5) a statement, under penalty of perjury, that the information is accurate and you are the rights holder or authorized to act on their behalf; (6) your physical or electronic signature."],
      ["Where to send it", `Email the notice to dmca at our domain. Incomplete notices will be returned for correction. We reserve the right to share valid notices with the user who submitted the URL, in accordance with the counter-notification process below.`],
      ["Counter-notifications", "Users whose URLs have been blocked may submit a counter-notification using the same structure, asserting under penalty of perjury that the material was blocked by mistake or misidentification. If no court action is filed within 10 business days, access is restored."],
      ["Repeat infringers", "We reserve the right to permanently block URLs, IP addresses, or accounts associated with repeat infringement."],
    ], faqs: [] },
  { slug: "privacy-policy", title: "Privacy Policy", h1: "Privacy Policy",
    converterTitle: "Privacy Policy",
    kicker: `How ${BRAND} collects, uses, and protects information. Plain language, no dark patterns.`,
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "ytmp3 privacy policy, youtube converter privacy",
    sections: [
      ["What we collect", "Minimal technical data: IP address (for abuse prevention and rate limiting), user-agent string (browser and OS), and the URLs you submit for conversion (only while a job is in progress). We do not set identification cookies, do not use fingerprinting, and do not share data with advertising networks."],
      ["What we do not collect", "No name, no email unless you contact support, no location beyond the rough inference from IP, no browsing history, no information about other tabs or apps on your device."],
      ["Conversion files", "Converted files are stored on our servers only long enough for you to download them (default 30 minutes) and are then permanently deleted. We do not scan, catalog, or back up the content."],
      ["Analytics", "We use privacy-respecting server-side logging to count requests per endpoint and troubleshoot errors. No per-user analytics or session recording."],
      ["Third parties", "The only third-party services our backend contacts are YouTube itself (to fetch the source video) and our hosting provider's infrastructure. We do not integrate ad networks, trackers, or social widgets."],
      ["Your rights", "You can request deletion of any information we hold about you by emailing privacy at our domain. We will respond within 30 days. If you are in the EU, you have additional rights under GDPR; if you are in California, you have additional rights under the CCPA — we honor both."],
      ["Changes", "Material changes to this policy will be announced at the top of this page for at least 30 days before taking effect."],
    ], faqs: [] },
  { slug: "terms-of-use", title: "Terms of Use", h1: "Terms of Use",
    converterTitle: "Terms of Use",
    kicker: `By using ${BRAND} you agree to the terms below. Read them carefully — they are binding.`,
    defaultFormat: "mp3", defaultQuality: "320",
    keywords: "ytmp3 terms, terms of use, service agreement",
    sections: [
      ["1. The service", `${BRAND} provides a web-based media conversion utility. You paste a URL; we fetch the media from the source platform and re-encode it into the format you requested. The service is provided free of charge on an "as is" basis.`],
      ["2. Acceptable use", "You agree to use the service only for lawful purposes. In particular, you represent that for any URL you submit, you have the right to download and save the underlying content — because it is your own upload, because it is under a permissive license (Creative Commons, public domain), because you have the rights holder's authorization, or because your jurisdiction's law allows personal-use private copying. Using the service to reproduce copyrighted works without authorization is prohibited."],
      ["3. Prohibited activities", "You may not: (a) use the service to stalk, harass, or defame anyone; (b) attempt to break, overwhelm, or reverse-engineer the infrastructure; (c) scrape or resell the converted files; (d) use automation to generate more than 50 requests per minute from a single IP."],
      ["4. No warranty", "The service is provided without warranty of any kind, express or implied. We do not guarantee uptime, conversion quality, or compatibility with any specific device or file format. YouTube may change its infrastructure at any time, which can temporarily or permanently break the service."],
      ["5. Limitation of liability", "To the maximum extent permitted by law, we are not liable for any indirect, incidental, consequential, special, or exemplary damages arising from your use of the service. Our total liability for any claim is capped at the amount you have paid us in the last 12 months, which for free users is zero."],
      ["6. Termination", "We may suspend or terminate your access at any time for violations of these terms, for abuse of the service, or at our discretion to protect the service."],
      ["7. Governing law", "These terms are governed by the laws of the operator's jurisdiction. Disputes will be resolved by binding arbitration or in a court of competent jurisdiction, at our election."],
      ["8. Changes", "We may update these terms. Material changes will be posted at the top of this page at least 30 days before taking effect. Continued use after the effective date constitutes acceptance."],
    ], faqs: [] }
];

function esc(s) { 
  // Don't escape if it's already HTML (contains tags)
  if (String(s).includes('<') && String(s).includes('>')) return s;
  return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"); 
}

function generateHreflang() {
  const langs = [
    ["en", "/"], ["ar", "/ar/"], ["bn", "/bn/"], ["de", "/de/"],
    ["es", "/es/"], ["fil", "/fil/"], ["fr", "/fr/"], ["hi", "/hi/"],
    ["id", "/id/"], ["it", "/it/"], ["ja", "/ja/"], ["ko", "/ko/"],
    ["pt", "/pt/"], ["ru", "/ru/"], ["th", "/th/"], ["tr", "/tr/"],
    ["ur", "/ur/"], ["vi", "/vi/"]
  ];
  let tags = '<link rel="alternate" hreflang="x-default" href="' + SITE + '/">\n';
  for (const [code, path] of langs) {
    tags += '<link rel="alternate" hreflang="' + code + '" href="' + SITE + path + '">\n';
  }
  return tags;
}

function header() {
  return `<header class="site-header"><div class="container header-row"><a class="brand" href="/" aria-label="${BRAND} home">yt2mp3<span class="brand-dot">.lol</span></a><div class="header-actions"><button type="button" class="btn-supporter" aria-label="Support"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 2l2.5 6L21 9l-5 4.5L17.5 20 12 16.8 6.5 20 8 13.5 3 9l6.5-1L12 2z" fill="currentColor"/></svg><span class="s-label">Supporter</span></button><details class="lang-menu"><summary class="btn-lang" role="button" aria-label="Language"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18" stroke="currentColor" stroke-width="1.5" fill="none"/></svg><span class="l-label">English</span><svg width="10" height="10" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></summary><div class="lang-list" role="menu"><a role="menuitem" href="/" class="lang-active">English</a><a role="menuitem" href="/ar/">العربية</a><a role="menuitem" href="/bn/">বাংলা</a><a role="menuitem" href="/de/">Deutsch</a><a role="menuitem" href="/es/">Español</a><a role="menuitem" href="/fil/">Filipino</a><a role="menuitem" href="/fr/">Français</a><a role="menuitem" href="/hi/">हिन्दी</a><a role="menuitem" href="/id/">Bahasa Indonesia</a><a role="menuitem" href="/it/">Italiano</a><a role="menuitem" href="/ja/">日本語</a><a role="menuitem" href="/ko/">한국어</a><a role="menuitem" href="/pt/">Português</a><a role="menuitem" href="/ru/">Русский</a><a role="menuitem" href="/th/">ภาษาไทย</a><a role="menuitem" href="/tr/">Türkçe</a><a role="menuitem" href="/ur/">اردو</a><a role="menuitem" href="/vi/">Tiếng Việt</a></div></details><button type="button" class="btn-theme" id="theme-toggle" aria-label="Toggle theme" title="Toggle theme"><svg class="icon-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M20 14.5A8 8 0 019.5 4 8 8 0 1020 14.5z" fill="currentColor"/></svg><svg class="icon-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="4" fill="currentColor"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.5 4.5l2 2M17.5 17.5l2 2M4.5 19.5l2-2M17.5 6.5l2-2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button></div></div></header>`;
}

function footer() {
  return `<footer class="site-footer"><div class="container"><nav class="footer-nav" aria-label="Footer primary"><a href="/youtube-to-mp4-converter">YouTube to MP4</a><a href="/youtube-playlist-downloader">Playlist Downloader</a><a href="/youtube-shorts-downloader">Shorts Downloader</a><a href="/youtube-multi-downloader">Multiple Download</a><a href="/how-to-install">How to Install</a><a href="/faq">FAQ</a><a href="/about">About</a><a href="/contact">Contact</a></nav><nav class="footer-nav footer-legal" aria-label="Footer legal"><a href="/copyright-claims">Copyright Claims</a><a href="/privacy-policy">Privacy Policy</a><a href="/terms-of-use">Terms of Use</a></nav><p class="footer-copy">&copy; <span id="year"></span> ${BRAND}. Not affiliated with YouTube or Google.</p></div></footer>`;
}

function converterCard(p) {
  const isMulti = p && p.slug === "youtube-multi-downloader";
  const inputHtml = isMulti 
    ? `<textarea id="yt-url" name="url" placeholder="Paste YouTube URLs here (one per line)" aria-label="Paste YouTube links" required autocomplete="off" spellcheck="false" rows="4" style="resize:vertical;"></textarea>`
    : `<input id="yt-url" name="url" type="text" inputmode="url" placeholder="Paste YouTube URL or search keywords" aria-label="Paste a YouTube link" required autocomplete="off" spellcheck="false">`;

  return `<div id="converter" class="converter-card" role="region" aria-label="YouTube converter">
  <h2 class="converter-title">${p.converterTitle || "YT2MP3 - YouTube to MP3"}</h2>
  <form id="convert-form" autocomplete="off" novalidate>
    <div class="url-wrap">
      ${inputHtml}
      ${!isMulti ? `<button type="button" id="paste-btn" aria-label="Paste from clipboard" title="Paste"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="8" y="3" width="8" height="4" rx="1" stroke="currentColor" stroke-width="1.8"/><path d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2V7a2 2 0 00-2-2h-2" stroke="currentColor" stroke-width="1.8" fill="none"/></svg></button>` : ''}
    </div>
    <div class="controls-row">
      <div class="seg" role="tablist" aria-label="Output format"><button type="button" class="seg-btn active" role="tab" aria-selected="true" data-format="mp3">MP3</button><button type="button" class="seg-btn" role="tab" aria-selected="false" data-format="mp4">MP4</button></div>
      <label for="quality" class="sr-only">Quality</label>
      <select id="quality" class="select-pill" aria-label="Quality"></select>
      <details class="track-menu">
        <summary class="track-pill" role="button" aria-label="Audio track"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="9" y="3" width="6" height="12" rx="3" fill="currentColor"/><path d="M5 11a7 7 0 0014 0M12 18v3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span id="track-label">Origin</span><svg width="10" height="10" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></summary>
        <div class="track-list" role="menu" style="min-width:200px;">
          <div class="track-search-wrap" style="padding:8px 12px;border-bottom:1px solid var(--border);">
            <input type="text" id="track-search" class="track-search" placeholder="Search languages..." aria-label="Search languages" style="width:100%;padding:6px;border:1px solid var(--border);border-radius:4px;background:var(--bg);color:var(--text);font-size:14px;">
          </div>
          <div class="track-scroll" style="max-height:220px;overflow-y:auto;padding:4px;">
            <button type="button" class="track-opt" data-track="" role="menuitem">Origin (default)</button>
            <button type="button" class="track-opt" data-track="en" role="menuitem">🇬🇧 English</button>
            <button type="button" class="track-opt" data-track="hi" role="menuitem">🇮🇳 Hindi</button>
            <button type="button" class="track-opt" data-track="en-IN" role="menuitem">🇮🇳 English (India)</button>
            <button type="button" class="track-opt" data-track="fr-CA" role="menuitem">🇨🇦 French (Canada)</button>
            <button type="button" class="track-opt" data-track="es-419" role="menuitem">🇲🇽 Spanish (LatAm)</button>
            <button type="button" class="track-opt" data-track="ar" role="menuitem">🇸🇦 Arabic</button>
            <button type="button" class="track-opt" data-track="ja" role="menuitem">🇯🇵 Japanese</button>
            <button type="button" class="track-opt" data-track="ko" role="menuitem">🇰🇷 Korean</button>
            <button type="button" class="track-opt" data-track="fr" role="menuitem">🇫🇷 French</button>
            <button type="button" class="track-opt" data-track="es" role="menuitem">🇪🇸 Spanish</button>
            <button type="button" class="track-opt" data-track="de" role="menuitem">🇩🇪 German</button>
            <button type="button" class="track-opt" data-track="it" role="menuitem">🇮🇹 Italian</button>
            <button type="button" class="track-opt" data-track="pt-BR" role="menuitem">🇧🇷 Portuguese (Brazil)</button>
            <button type="button" class="track-opt" data-track="pt" role="menuitem">🇵🇹 Portuguese</button>
            <button type="button" class="track-opt" data-track="ru" role="menuitem">🇷🇺 Russian</button>
            <button type="button" class="track-opt" data-track="zh-Hans" role="menuitem">🇨🇳 Chinese (Simplified)</button>
            <button type="button" class="track-opt" data-track="zh-Hant" role="menuitem">🇹🇼 Chinese (Traditional)</button>
            <button type="button" class="track-opt" data-track="vi" role="menuitem">🇻🇳 Vietnamese</button>
            <button type="button" class="track-opt" data-track="th" role="menuitem">🇹🇭 Thai</button>
            <button type="button" class="track-opt" data-track="id" role="menuitem">🇮🇩 Indonesian</button>
            <button type="button" class="track-opt" data-track="tl" role="menuitem">🇵🇭 Filipino</button>
            <button type="button" class="track-opt" data-track="tr" role="menuitem">🇹🇷 Turkish</button>
            <button type="button" class="track-opt" data-track="pl" role="menuitem">🇵🇱 Polish</button>
            <button type="button" class="track-opt" data-track="nl" role="menuitem">🇳🇱 Dutch</button>
            <button type="button" class="track-opt" data-track="sv" role="menuitem">🇸🇪 Swedish</button>
            <button type="button" class="track-opt" data-track="no" role="menuitem">🇳🇴 Norwegian</button>
            <button type="button" class="track-opt" data-track="da" role="menuitem">🇩🇰 Danish</button>
            <button type="button" class="track-opt" data-track="fi" role="menuitem">🇫🇮 Finnish</button>
            <button type="button" class="track-opt" data-track="el" role="menuitem">🇬🇷 Greek</button>
            <button type="button" class="track-opt" data-track="cs" role="menuitem">🇨🇿 Czech</button>
            <button type="button" class="track-opt" data-track="hu" role="menuitem">🇭🇺 Hungarian</button>
            <button type="button" class="track-opt" data-track="ro" role="menuitem">🇷🇴 Romanian</button>
            <button type="button" class="track-opt" data-track="bg" role="menuitem">🇧🇬 Bulgarian</button>
            <button type="button" class="track-opt" data-track="uk" role="menuitem">🇺🇦 Ukrainian</button>
            <button type="button" class="track-opt" data-track="he" role="menuitem">🇮🇱 Hebrew</button>
            <button type="button" class="track-opt" data-track="ms" role="menuitem">🇲🇾 Malay</button>
            <button type="button" class="track-opt" data-track="bn" role="menuitem">🇧🇩 Bengali</button>
            <button type="button" class="track-opt" data-track="ur" role="menuitem">🇵🇰 Urdu</button>
            <button type="button" class="track-opt" data-track="fa" role="menuitem">🇮🇷 Persian</button>
          </div>
        </div>
      </details>
      <div class="spacer"></div>
      <button id="convert-btn" type="submit">Convert</button>
    </div>
    <div id="status" class="status hidden" aria-live="polite"></div>
  </form>
</div>`;
}


function getRelatedLinks(slug) {
  const related = {
    "youtube-to-mp3-320kbps-converter": [
      { url: "/wav-converter/", title: "WAV Converter (Lossless)" },
      { url: "/m4a-converter/", title: "M4A Converter" },
      { url: "/youtube-to-mp4-converter/", title: "MP4 Converter" }
    ],
    "wav-converter": [
      { url: "/youtube-to-mp3-320kbps-converter/", title: "320kbps MP3" },
      { url: "/m4a-converter/", title: "M4A Converter" }
    ],
    "m4a-converter": [
      { url: "/youtube-to-mp3-320kbps-converter/", title: "320kbps MP3" },
      { url: "/wav-converter/", title: "WAV Converter" }
    ],
    "youtube-to-mp4-converter": [
      { url: "/youtube-shorts-downloader/", title: "Shorts Downloader" },
      { url: "/youtube-playlist-downloader/", title: "Playlist Downloader" }
    ],
    "youtube-shorts-downloader": [
      { url: "/youtube-to-mp4-converter/", title: "MP4 Converter" },
      { url: "/youtube-playlist-downloader/", title: "Playlist Downloader" }
    ],
    "youtube-playlist-downloader": [
      { url: "/youtube-multi-downloader/", title: "Multi Downloader" },
      { url: "/youtube-shorts-downloader/", title: "Shorts Downloader" }
    ]
  };
  
  if (!related[slug]) return "";
  
  return `<section class="section"><div class="container"><h2>Related Tools</h2><nav style="display:flex;gap:12px;flex-wrap:wrap;">${related[slug].map(r => 
    '<a href="' + r.url + '" style="padding:12px 20px;background:var(--card);border:1px solid var(--border);border-radius:12px;font-weight:600;display:inline-block;">' + r.title + '</a>'
  ).join('')}</nav></div></section>`;
}


function renderLandingPage(p) {
  const sectionsHtml = p.sections.map((s, i) =>
    `<section class="section${i % 2 ? " alt" : ""}"><div class="container"><h2>${esc(s[0])}</h2><p>${esc(s[1])}</p></div></section>`
  ).join("\n");
  const faqsHtml = p.faqs && p.faqs.length
    ? `<section class="section"><div class="container"><h2>FAQ</h2>${p.faqs.map(f => `<details><summary>${esc(f[0])}</summary><p>${esc(f[1])}</p></details>`).join("")}</div></section>`
    : "";
  const faqLd = p.faqs && p.faqs.length
    ? `<script type="application/ld+json">${JSON.stringify({ "@context": "https://schema.org", "@type": "FAQPage", mainEntity: p.faqs.map(f => ({ "@type": "Question", name: f[0], acceptedAnswer: { "@type": "Answer", text: f[1] } })) })}</script>`
    : "";
  const howToLd = ["faq", "about", "contact", "copyright-claims", "privacy-policy", "terms-of-use"].includes(p.slug) ? "" :
    `<script type="application/ld+json">${JSON.stringify({
      "@context": "https://schema.org",
      "@type": "HowTo",
      name: "How to convert using " + BRAND,
      step: [
        { "@type": "HowToStep", name: "Copy link", text: "Copy the video URL from your browser or app." },
        { "@type": "HowToStep", name: "Paste and select format", text: "Paste the link and choose your preferred format and quality." },
        { "@type": "HowToStep", name: "Download", text: "Click Convert and download the file." }
      ]
    })}</script>`;

  // Conditionally include canonical tag (omit for Vercel to allow independent indexing)
  const canonicalTag = IS_VERCEL_BUILD ? '' : `<link rel="canonical" href="${SITE}/${p.slug}/">`;
  
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
${canonicalTag}
<meta property="og:title" content="${esc(p.title)}">
<meta property="og:description" content="${esc(p.kicker)}">
<meta property="og:type" content="website">
<meta property="og:url" content="${SITE}/${p.slug}">
<meta name="robots" content="index,follow,max-image-preview:large">\n${generateHreflang()}
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="stylesheet" href="/assets/style.css?v=2">
<script>(function(){try{var t=localStorage.getItem("tr-theme");if(t)document.documentElement.setAttribute("data-theme",t);}catch(e){}})();</script>
${faqLd}
${howToLd}
</head>
<body>
<a href="#converter" class="skip">Skip to converter</a>
${header()}
<main>
<section class="hero">
  <div class="container">
    <p style="margin:0 0 12px;font-size:14px;color:#9aa0b4"><a href="/">&larr; Home</a></p>
    <h1 style="text-align:center;margin:0 0 8px;font-size:clamp(24px,4vw,34px);letter-spacing:-.02em">${esc(p.h1)}</h1>
    <p style="text-align:center;color:#a3a8b8;max-width:620px;margin:0 auto 24px">${esc(p.kicker)}</p>
    ${converterCard(p)}
  </div>
</section>
${sectionsHtml}
${faqsHtml}
${getRelatedLinks(p.slug)}
</main>
${footer()}
<script>window.__DEFAULT_FORMAT__=${JSON.stringify(p.defaultFormat)};window.__DEFAULT_QUALITY__=${JSON.stringify(p.defaultQuality)};</script>
<script src="/assets/app.js?v=2" defer></script>
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

// Emit a sitemap.xml covering all SEO-visible URLs.
const urls = [
  { loc: "/", pri: "1.0", freq: "daily" },
  ...PAGES.filter(p => !["privacy-policy", "terms-of-use", "copyright-claims", "contact"].includes(p.slug))
    .map(p => ({ loc: "/" + p.slug, pri: ["youtube-to-mp4-converter", "youtube-shorts-downloader", "youtube-to-mp3-320kbps-converter"].includes(p.slug) ? "0.9" : "0.8", freq: "weekly" })),
  ...PAGES.filter(p => ["privacy-policy", "terms-of-use", "copyright-claims", "contact"].includes(p.slug))
    .map(p => ({ loc: "/" + p.slug, pri: "0.4", freq: "yearly" })),
];
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map(u => `  <url><loc>${SITE}${u.loc}</loc><priority>${u.pri}</priority><changefreq>${u.freq}</changefreq></url>`).join("\n")}
</urlset>
`;
fs.writeFileSync(path.join(WEB, "sitemap.xml"), sitemap);
console.log("wrote sitemap.xml (" + urls.length + " URLs)");

// Post-process: Remove canonical tags from index.html if building for Vercel
if (IS_VERCEL_BUILD) {
  const indexPath = path.join(WEB, "index.html");
  if (fs.existsSync(indexPath)) {
    let indexHtml = fs.readFileSync(indexPath, "utf8");
    // Remove canonical tag
    indexHtml = indexHtml.replace(/<link rel="canonical"[^>]*>/gi, '');
    fs.writeFileSync(indexPath, indexHtml);
    console.log("removed canonical tag from index.html (Vercel build)");
  }
  
  // Also remove from other static HTML pages if they exist
  const staticPages = ['youtube-mp3', 'ytmp3', 'youtube-audio-download-mp3', 'download-lagu-youtube'];
  for (const page of staticPages) {
    const pagePath = path.join(WEB, page, "index.html");
    if (fs.existsSync(pagePath)) {
      let pageHtml = fs.readFileSync(pagePath, "utf8");
      pageHtml = pageHtml.replace(/<link rel="canonical"[^>]*>/gi, '');
      fs.writeFileSync(pagePath, pageHtml);
      console.log(`removed canonical tag from ${page}/index.html (Vercel build)`);
    }
  }
}
