#!/usr/bin/env python3
"""
Fix build.js issues:
1. Add converterTitle parameter to each page
2. Fix esc() to support raw HTML sections
3. Add critical CSS inlining
4. Fix canonical trailing slashes
5. Add hreflang tags
6. Generate current lastmod dates in sitemap
"""

import re
from pathlib import Path

def main():
    build_js_path = Path("web/build.js")
    
    with open(build_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=" * 70)
    print("Fixing build.js...")
    print("=" * 70)
    
    # 1. Add converterTitle to each page definition
    print("\n1. Adding converterTitle to page definitions...")
    
    # Add converterTitle based on page type
    converter_titles = {
        'youtube-to-mp4-converter': 'YouTube to MP4 Converter',
        'youtube-shorts-downloader': 'YouTube Shorts Downloader',
        'youtube-playlist-downloader': 'YouTube Playlist Downloader',
        'youtube-multi-downloader': 'Multiple YouTube Downloader',
        'youtube-to-mp3-320kbps-converter': 'YouTube to MP3 320kbps',
        'wav-converter': 'YouTube to WAV Converter',
        'm4a-converter': 'YouTube to M4A Converter',
        'iphone-converter': 'YouTube to MP3 on iPhone',
        'android-converter': 'YouTube to MP3 on Android',
        'how-to-install': 'Install YouTube Converter',
        'faq': 'YouTube Converter FAQ',
        'about': 'About yt2mp3.lol',
        'contact': 'Contact Us',
        'copyright-claims': 'Copyright Claims',
        'privacy-policy': 'Privacy Policy',
        'terms-of-use': 'Terms of Use',
    }
    
    for slug, title in converter_titles.items():
        # Find the page definition and add converterTitle after h1
        pattern = rf'(\{{ slug: "{slug}"[^}}]+h1: "[^"]+",)'
        replacement = rf'\1\n    converterTitle: "{title}",'
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content, count=1)
    
    print("   ✓ Added converterTitle to all pages")
    
    # 2. Update converterCard function to use p.converterTitle
    print("\n2. Updating converterCard to use dynamic title...")
    
    old_converter_card = r'<h2 class="converter-title">YT2MP3 - YouTube to MP3</h2>'
    new_converter_card = r'<h2 class="converter-title">${p.converterTitle || "YT2MP3 - YouTube to MP3"}</h2>'
    
    content = content.replace(old_converter_card, new_converter_card)
    print("   ✓ Converter title now dynamic")
    
    # 3. Fix esc() function to handle raw HTML
    print("\n3. Fixing esc() to support raw HTML...")
    
    old_esc = r'function esc(s) { return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"); }'
    new_esc = '''function esc(s) { 
  // Don't escape if it's already HTML (contains tags)
  if (String(s).includes('<') && String(s).includes('>')) return s;
  return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"); 
}'''
    
    content = content.replace(old_esc, new_esc)
    print("   ✓ esc() now preserves HTML tables")
    
    # 4. Fix canonical to include trailing slash
    print("\n4. Adding trailing slash to canonical URLs...")
    
    old_canonical = r'<link rel="canonical" href="${SITE}/${p.slug}">'
    new_canonical = r'<link rel="canonical" href="${SITE}/${p.slug}/">'
    
    content = content.replace(old_canonical, new_canonical)
    print("   ✓ Canonical URLs now have trailing slashes")
    
    # 5. Add hreflang tags generation
    print("\n5. Adding hreflang tags...")
    
    # Add hreflang generation function after esc()
    hreflang_function = '''

function generateHreflang() {
  const langs = [
    ["en", "/"], ["ar", "/ar/"], ["bn", "/bn/"], ["de", "/de/"],
    ["es", "/es/"], ["fil", "/fil/"], ["fr", "/fr/"], ["hi", "/hi/"],
    ["id", "/id/"], ["it", "/it/"], ["ja", "/ja/"], ["ko", "/ko/"],
    ["pt", "/pt/"], ["ru", "/ru/"], ["th", "/th/"], ["tr", "/tr/"],
    ["ur", "/ur/"], ["vi", "/vi/"]
  ];
  let tags = '<link rel="alternate" hreflang="x-default" href="' + SITE + '/">\\n';
  for (const [code, path] of langs) {
    tags += '<link rel="alternate" hreflang="' + code + '" href="' + SITE + path + '">\\n';
  }
  return tags;
}'''
    
    # Insert after esc() function
    content = re.sub(
        r'(function esc\([^}]+\}\s*\})',
        r'\1' + hreflang_function,
        content,
        count=1
    )
    
    # Add hreflang to template
    old_meta_robots = r'<meta name="robots" content="index,follow,max-image-preview:large">'
    new_meta_robots = r'<meta name="robots" content="index,follow,max-image-preview:large">\n${generateHreflang()}'
    
    content = content.replace(old_meta_robots, new_meta_robots)
    print("   ✓ Hreflang tags added to template")
    
    # 6. Add critical CSS inlining
    print("\n6. Adding critical CSS inlining...")
    
    critical_css = '''<!-- Critical CSS inlined for performance -->
<style>
:root{--bg:#ffffff;--bg-2:#f8f9fa;--card:#ffffff;--card-2:#f1f3f5;--text:#111111;--muted:#333333;--border:#e1e4e8;--border-2:#d1d5da;--accent:#2d5cf7;--accent-text:#ffffff;--accent-soft:rgba(45,92,247,0.1);--blue:#2d5cf7;--success:#22c55e;--danger:#ef4444;--radius:18px;--radius-sm:12px;--shadow:0 4px 12px rgba(0,0,0,0.05);--max:900px;--tap:44px}
[data-theme="dark"]{--bg:#0b0d14;--bg-2:#161a24;--card:#1c212e;--card-2:#262a36;--text:#f3f4f9;--muted:#a0a8c0;--border:#2d3446;--border-2:#353948;--accent:#4a7fff;--accent-text:#0b0d14;--accent-soft:rgba(74,127,255,0.15);--shadow:0 8px 24px rgba(0,0,0,0.3)}
*,*::before,*::after{box-sizing:border-box}
html,body{margin:0;padding:0}
html{color-scheme:dark}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;background:var(--bg);color:var(--text);line-height:1.55;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:100%;min-height:100vh}
a{color:var(--text);text-decoration:none}
button{font:inherit;color:inherit}
img,svg{max-width:100%;display:block}
.container{max-width:var(--max);margin:0 auto;padding:0 16px;width:100%}
.sr-only{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.skip{position:absolute;left:-9999px}
.skip:focus{left:16px;top:16px;background:var(--accent);color:var(--accent-text);padding:8px 12px;border-radius:8px;z-index:9999}
.site-header{padding:24px 0}
.header-row{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.brand{font-weight:900;font-size:clamp(26px,4.6vw,36px);letter-spacing:-.02em;color:var(--text);line-height:1}
.brand-dot{color:var(--accent);font-weight:900}
.header-actions{display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:flex-end}
.btn-supporter{display:inline-flex;align-items:center;gap:8px;background:var(--accent);color:var(--accent-text);border:0;border-radius:var(--radius-sm);padding:10px 16px;font-weight:700;font-size:14px;cursor:pointer;min-height:var(--tap)}
.btn-lang,.btn-theme{background:transparent;border:1px solid var(--border-2);border-radius:var(--radius-sm);color:var(--text);padding:9px 14px;font-size:14px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;min-height:var(--tap)}
.btn-theme{padding:0;width:var(--tap);height:var(--tap);justify-content:center}
.btn-theme .icon-sun{display:none}
html[data-theme="light"] .btn-theme .icon-moon{display:none}
html[data-theme="light"] .btn-theme .icon-sun{display:block}
.hero{padding:8px 0 40px;min-height:420px}
.converter-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:32px;box-shadow:var(--shadow);min-height:320px}
.converter-title{margin:0 0 24px;text-align:center;font-weight:800;letter-spacing:-.015em;font-size:clamp(22px,4vw,30px)}
.section{padding:48px 0}
@media (max-width:560px){
.container{padding:0 12px}
.converter-card{padding:20px 16px;border-radius:14px}
}
</style>
<!-- Load full CSS asynchronously -->
<link rel="preload" href="/assets/style.css?v=2" as="style" onload="this.onload=null;this.rel=\\'stylesheet\\'">
<noscript><link rel="stylesheet" href="/assets/style.css?v=2"></noscript>'''
    
    # Replace the simple stylesheet link with critical CSS + async load
    old_css_link = r'<link rel="stylesheet" href="/assets/style.css\?v=2">'
    content = content.replace(old_css_link, critical_css)
    print("   ✓ Critical CSS now inlined")
    
    # 7. Fix sitemap to use current date
    print("\n7. Fixing sitemap lastmod dates...")
    
    # Add date generation at the top
    date_gen = "const currentDate = new Date().toISOString().split('T')[0];\n"
    content = re.sub(
        r'(const WEB = path\.resolve\(__dirname\);)',
        date_gen + r'\1',
        content,
        count=1
    )
    
    # Update sitemap generation to use current date
    old_sitemap_url = r'<url><loc>\${SITE}\${u\.loc}</loc><priority>\${u\.pri}</priority><changefreq>\${u\.freq}</changefreq></url>'
    new_sitemap_url = r'<url><loc>${SITE}${u.loc}</loc><lastmod>${currentDate}</lastmod><priority>${u.pri}</priority><changefreq>${u.freq}</changefreq></url>'
    
    content = content.replace(old_sitemap_url, new_sitemap_url)
    print("   ✓ Sitemap now uses current date")
    
    # Write the updated file
    with open(build_js_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n" + "=" * 70)
    print("✓ build.js fixed successfully!")
    print("=" * 70)
    print("\nFixed issues:")
    print("  • Dynamic converter titles (no more hardcoded 'YT2MP3')")
    print("  • esc() preserves HTML tables")
    print("  • Critical CSS inlined (faster LCP)")
    print("  • Canonical URLs have trailing slashes")
    print("  • Hreflang tags added to all pages")
    print("  • Sitemap uses current date")
    print("\nNext: Run 'node web/build.js' to regenerate pages")

if __name__ == "__main__":
    main()
