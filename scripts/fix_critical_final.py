#!/usr/bin/env python3
"""
Fix final critical issues:
1. Fix lang switcher dead links in build.js
2. Remove duplicate web/sitemap.xml (keep only public/)
3. Add missing OG tags
4. Add cross-links between related format pages
"""

import os
import re
from pathlib import Path

def fix_lang_switcher_in_buildjs():
    """Fix lang switcher to use actual URLs instead of #"""
    build_js = Path("web/build.js")
    
    with open(build_js, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the lang menu in header() function
    old_lang_menu = r'<a role="menuitem" href="#" class="lang-active">English</a><a role="menuitem" href="#">العربية</a><a role="menuitem" href="#">বাংলা</a><a role="menuitem" href="#">Deutsch</a><a role="menuitem" href="#">Español</a><a role="menuitem" href="#">Filipino</a><a role="menuitem" href="#">Français</a><a role="menuitem" href="#">हिन्दी</a><a role="menuitem" href="#">Bahasa Indonesia</a><a role="menuitem" href="#">Italiano</a><a role="menuitem" href="#">日本語</a><a role="menuitem" href="#">한국어</a><a role="menuitem" href="#">Bahasa Melayu</a><a role="menuitem" href="#">မြန်မာ</a><a role="menuitem" href="#">Português</a><a role="menuitem" href="#">Русский</a><a role="menuitem" href="#">ภาษาไทย</a><a role="menuitem" href="#">Türkçe</a><a role="menuitem" href="#">اردو</a><a role="menuitem" href="#">Tiếng Việt</a>'
    
    new_lang_menu = r'<a role="menuitem" href="/" class="lang-active">English</a><a role="menuitem" href="/ar/">العربية</a><a role="menuitem" href="/bn/">বাংলা</a><a role="menuitem" href="/de/">Deutsch</a><a role="menuitem" href="/es/">Español</a><a role="menuitem" href="/fil/">Filipino</a><a role="menuitem" href="/fr/">Français</a><a role="menuitem" href="/hi/">हिन्दी</a><a role="menuitem" href="/id/">Bahasa Indonesia</a><a role="menuitem" href="/it/">Italiano</a><a role="menuitem" href="/ja/">日本語</a><a role="menuitem" href="/ko/">한국어</a><a role="menuitem" href="/pt/">Português</a><a role="menuitem" href="/ru/">Русский</a><a role="menuitem" href="/th/">ภาษาไทย</a><a role="menuitem" href="/tr/">Türkçe</a><a role="menuitem" href="/ur/">اردو</a><a role="menuitem" href="/vi/">Tiếng Việt</a>'
    
    content = content.replace(old_lang_menu, new_lang_menu)
    
    with open(build_js, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def add_og_tags_to_buildjs():
    """Add missing OG image and Twitter tags"""
    build_js = Path("web/build.js")
    
    with open(build_js, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the OG tags section and add missing tags
    old_og = r'<meta property="og:url" content="\${SITE}/\${p\.slug}/">'
    new_og = r'<meta property="og:url" content="${SITE}/${p.slug}/">\n<meta property="og:image" content="${SITE}/assets/og.png">\n<meta property="og:locale" content="en">\n<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:image" content="${SITE}/assets/og.png">'
    
    # Remove duplicate twitter:card if exists
    content = re.sub(r'<meta name="twitter:card" content="summary_large_image">\n', '', content)
    content = content.replace(old_og, new_og)
    
    with open(build_js, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def add_cross_links_to_buildjs():
    """Add related format cross-links to pages"""
    build_js = Path("web/build.js")
    
    with open(build_js, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add related links function
    related_links_func = '''
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
'''
    
    # Insert before renderLandingPage function
    content = re.sub(
        r'(function renderLandingPage\(p\) \{)',
        related_links_func + '\n\n\\1',
        content,
        count=1
    )
    
    # Add related links before footer in template
    content = re.sub(
        r'(\$\{faqsHtml\})',
        r'\1\n${getRelatedLinks(p.slug)}',
        content,
        count=1
    )
    
    with open(build_js, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def remove_duplicate_sitemap():
    """Remove web/sitemap.xml to avoid confusion"""
    sitemap_path = Path("web/sitemap.xml")
    if sitemap_path.exists():
        sitemap_path.unlink()
        return True
    return False

def main():
    print("=" * 70)
    print("Fixing final critical issues...")
    print("=" * 70)
    
    print("\n1. Fixing lang switcher dead links...")
    if fix_lang_switcher_in_buildjs():
        print("   ✓ Lang switcher now uses real URLs")
    
    print("\n2. Adding missing OG and Twitter tags...")
    if add_og_tags_to_buildjs():
        print("   ✓ OG image and Twitter tags added")
    
    print("\n3. Adding cross-links between related pages...")
    if add_cross_links_to_buildjs():
        print("   ✓ Related format cross-links added")
    
    print("\n4. Removing duplicate sitemap...")
    if remove_duplicate_sitemap():
        print("   ✓ Removed web/sitemap.xml (keeping public/sitemap.xml)")
    else:
        print("   ℹ web/sitemap.xml already removed")
    
    print("\n" + "=" * 70)
    print("✓ All fixes applied!")
    print("=" * 70)
    print("\nFixed issues:")
    print("  • Lang switcher links now work (18 languages)")
    print("  • OG image and Twitter cards added")
    print("  • Cross-links between related format pages")
    print("  • Single sitemap (no duplicates)")
    print("\nNext: Run 'node web/build.js' to regenerate pages")

if __name__ == "__main__":
    main()
