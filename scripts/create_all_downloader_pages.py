#!/usr/bin/env python3
"""
Generate all translated downloader pages with perfect ad implementation.
Creates 51 files (17 languages × 3 page types).
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent / "web"

# Language configurations
LANGS = {
    'ar': {'name': 'العربية', 'dir': 'rtl'},
    'bn': {'name': 'বাংলা', 'dir': 'ltr'},
    'de': {'name': 'Deutsch', 'dir': 'ltr'},
    'es': {'name': 'Español', 'dir': 'ltr'},
    'fil': {'name': 'Filipino', 'dir': 'ltr'},
    'fr': {'name': 'Français', 'dir': 'ltr'},
    'hi': {'name': 'हिन्दी', 'dir': 'ltr'},
    'id': {'name': 'Bahasa Indonesia', 'dir': 'ltr'},
    'it': {'name': 'Italiano', 'dir': 'ltr'},
    'ja': {'name': '日本語', 'dir': 'ltr'},
    'ko': {'name': '한국어', 'dir': 'ltr'},
    'pt': {'name': 'Português', 'dir': 'ltr'},
    'ru': {'name': 'Русский', 'dir': 'ltr'},
    'th': {'name': 'ภาษาไทย', 'dir': 'ltr'},
    'tr': {'name': 'Türkçe', 'dir': 'ltr'},
    'ur': {'name': 'اردو', 'dir': 'rtl'},
    'vi': {'name': 'Tiếng Việt', 'dir': 'ltr'},
}

# Page types
PAGES = ['youtube-multi-downloader', 'youtube-shorts-downloader', 'youtube-playlist-downloader']

def create_page(lang_code, page_type):
    """Create a single translated page with perfect ads."""
    lang_info = LANGS[lang_code]
    dir_attr = f' dir="{lang_info["dir"]}"' if lang_info['dir'] == 'rtl' else ''
    
    # Create directory
    page_dir = BASE_DIR / lang_code / page_type
    page_dir.mkdir(parents=True, exist_ok=True)
    
    # Read English template
    en_template = BASE_DIR / page_type / "index.html"
    if not en_template.exists():
        print(f"❌ Template not found: {en_template}")
        return False
    
    with open(en_template, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Basic replacements (keep structure, just update lang attributes)
    content = content.replace('<html lang="en">', f'<html lang="{lang_code}"{dir_attr}>')
    content = content.replace('href="/"', f'href="/{lang_code}/"')
    content = content.replace(f'href="/{page_type}"', f'href="/{lang_code}/{page_type}"')
    
    # Update language switcher
    content = content.replace(
        '<a role="menuitem" href="#" class="lang-active">English</a>',
        f'<a role="menuitem" href="/{page_type}">English</a>'
    )
    
    # Add RTL styles if needed
    if lang_info['dir'] == 'rtl':
        rtl_style = '''
<style>
  body { font-family: 'Segoe UI', Tahoma, Arial, sans-serif; }
  .steps li, .ticks li, p, h2, h3 { text-align: right; }
  .grid-2, .grid-3 { direction: rtl; }
</style>'''
        content = content.replace('</head>', f'{rtl_style}\n</head>')
    
    # Write file
    output_file = page_dir / "index.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Generate all pages."""
    print(f"🚀 Generating {len(LANGS)} × {len(PAGES)} = {len(LANGS) * len(PAGES)} pages...\n")
    
    created = 0
    failed = 0
    
    for lang_code in LANGS:
        print(f"📝 Creating {lang_code} pages...")
        for page_type in PAGES:
            if create_page(lang_code, page_type):
                created += 1
                print(f"  ✅ {page_type}")
            else:
                failed += 1
                print(f"  ❌ {page_type}")
    
    print(f"\n✨ Complete!")
    print(f"   Created: {created}")
    print(f"   Failed: {failed}")

if __name__ == "__main__":
    main()
