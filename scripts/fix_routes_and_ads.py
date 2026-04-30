#!/usr/bin/env python3
"""
Fix language routes and ensure perfect ad implementation for all downloader pages.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent / "web"

LANGS = {
    'ar': 'العربية',
    'bn': 'বাংলা',
    'de': 'Deutsch',
    'es': 'Español',
    'fil': 'Filipino',
    'fr': 'Français',
    'hi': 'हिन्दी',
    'id': 'Bahasa Indonesia',
    'it': 'Italiano',
    'ja': '日本語',
    'ko': '한국어',
    'pt': 'Português',
    'ru': 'Русский',
    'th': 'ภาษาไทย',
    'tr': 'Türkçe',
    'ur': 'اردو',
    'vi': 'Tiếng Việt',
}

PAGES = ['youtube-multi-downloader', 'youtube-shorts-downloader', 'youtube-playlist-downloader']

def build_language_menu(current_lang, page_type):
    """Build proper language menu with correct routes."""
    menu_items = []
    
    # English (never active for non-English pages)
    menu_items.append(f'<a role="menuitem" href="/{page_type}">English</a>')
    
    # Other languages
    for lang_code, lang_name in LANGS.items():
        active_class = ' class="lang-active"' if lang_code == current_lang else ''
        menu_items.append(f'<a role="menuitem" href="/{lang_code}/{page_type}"{active_class}>{lang_name}</a>')
    
    return '\n          '.join(menu_items)

def fix_page(lang_code, page_type):
    """Fix a single page: routes, canonical URLs, and language menu."""
    file_path = BASE_DIR / lang_code / page_type / "index.html"
    
    if not file_path.exists():
        print(f"  ❌ File not found: {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix canonical URL
    content = re.sub(
        r'<link rel="canonical" href="https://yt2mp3\.lol/[^"]*">',
        f'<link rel="canonical" href="https://yt2mp3.lol/{lang_code}/{page_type}">',
        content
    )
    
    # Fix og:url
    content = re.sub(
        r'<meta property="og:url" content="https://yt2mp3\.lol/[^"]*">',
        f'<meta property="og:url" content="https://yt2mp3.lol/{lang_code}/{page_type}">',
        content
    )
    
    # Fix language label in header
    lang_name = LANGS[lang_code]
    content = re.sub(
        r'<span class="l-label">English</span>',
        f'<span class="l-label">{lang_name}</span>',
        content
    )
    
    # Fix language menu - replace the entire lang-list div content
    old_menu_pattern = r'<div class="lang-list" role="menu">.*?</div></details>'
    new_menu = f'''<div class="lang-list" role="menu">
          {build_language_menu(lang_code, page_type)}
        </div></details>'''
    
    content = re.sub(old_menu_pattern, new_menu, content, flags=re.DOTALL)
    
    # Ensure footer links point to correct language versions
    footer_links = {
        'youtube-to-mp4-converter': f'/{lang_code}/youtube-to-mp4-converter' if (BASE_DIR / lang_code / 'youtube-to-mp4-converter').exists() else '/youtube-to-mp4-converter',
        'youtube-playlist-downloader': f'/{lang_code}/youtube-playlist-downloader',
        'youtube-shorts-downloader': f'/{lang_code}/youtube-shorts-downloader',
        'youtube-multi-downloader': f'/{lang_code}/youtube-multi-downloader',
    }
    
    for page, url in footer_links.items():
        content = re.sub(
            f'href="/{page}"',
            f'href="{url}"',
            content
        )
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Fix all pages."""
    print("🔧 Fixing routes and language menus for all 51 pages...\n")
    
    fixed = 0
    failed = 0
    
    for lang_code in LANGS:
        print(f"📝 Fixing {lang_code} ({LANGS[lang_code]})...")
        for page_type in PAGES:
            if fix_page(lang_code, page_type):
                fixed += 1
                print(f"  ✅ {page_type}")
            else:
                failed += 1
                print(f"  ❌ {page_type}")
    
    print(f"\n✨ Complete!")
    print(f"   Fixed: {fixed}")
    print(f"   Failed: {failed}")

if __name__ == "__main__":
    main()
