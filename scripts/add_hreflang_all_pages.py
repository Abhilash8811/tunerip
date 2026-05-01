#!/usr/bin/env python3
"""Add comprehensive hreflang tags to all pages with language variants"""

import os
import re
from pathlib import Path

# All supported languages
LANGUAGES = {
    'en': 'https://yt2mp3.lol',
    'ar': 'https://yt2mp3.lol/ar',
    'bn': 'https://yt2mp3.lol/bn',
    'de': 'https://yt2mp3.lol/de',
    'es': 'https://yt2mp3.lol/es',
    'fil': 'https://yt2mp3.lol/fil',
    'fr': 'https://yt2mp3.lol/fr',
    'hi': 'https://yt2mp3.lol/hi',
    'id': 'https://yt2mp3.lol/id',
    'it': 'https://yt2mp3.lol/it',
    'ja': 'https://yt2mp3.lol/ja',
    'ko': 'https://yt2mp3.lol/ko',
    'pt': 'https://yt2mp3.lol/pt',
    'ru': 'https://yt2mp3.lol/ru',
    'th': 'https://yt2mp3.lol/th',
    'tr': 'https://yt2mp3.lol/tr',
    'ur': 'https://yt2mp3.lol/ur',
    'vi': 'https://yt2mp3.lol/vi',
}

# Pages that have language variants
MULTI_LANG_PAGES = [
    '',  # Homepage
    'youtube-shorts-downloader',
    'youtube-playlist-downloader',
    'youtube-multi-downloader',
]

# Pages with limited language support
LIMITED_LANG_PAGES = {
    'youtube-mp3': ['en', 'es', 'hi', 'pt', 'id'],
}

def get_page_path(filepath):
    """Extract page path from filepath"""
    # Remove web/ prefix and index.html suffix
    path = filepath.replace('web/', '').replace('/index.html', '').replace('index.html', '')
    return path

def get_page_type(page_path):
    """Determine what type of page this is"""
    if not page_path or page_path in LANGUAGES.values():
        return 'homepage'
    
    # Remove language prefix
    for lang_code in LANGUAGES.keys():
        if page_path.startswith(f'{lang_code}/'):
            page_path = page_path[len(lang_code)+1:]
            break
    
    if page_path in MULTI_LANG_PAGES:
        return 'multi_lang'
    
    if page_path in LIMITED_LANG_PAGES:
        return 'limited_lang'
    
    return 'single_lang'

def generate_hreflang_tags(page_path):
    """Generate hreflang tags for a page"""
    page_type = get_page_type(page_path)
    
    # Determine current language
    current_lang = 'en'
    page_slug = page_path
    
    for lang_code in LANGUAGES.keys():
        if page_path.startswith(f'{lang_code}/'):
            current_lang = lang_code
            page_slug = page_path[len(lang_code)+1:]
            break
    
    tags = []
    
    if page_type == 'homepage':
        # Homepage - all languages
        tags.append('<link rel="alternate" hreflang="x-default" href="https://yt2mp3.lol/">')
        for lang_code, base_url in LANGUAGES.items():
            url = f"{base_url}/" if lang_code != 'en' else "https://yt2mp3.lol/"
            tags.append(f'<link rel="alternate" hreflang="{lang_code}" href="{url}">')
    
    elif page_type == 'multi_lang':
        # Tool pages - all languages
        default_url = f"https://yt2mp3.lol/{page_slug}/" if page_slug else "https://yt2mp3.lol/"
        tags.append(f'<link rel="alternate" hreflang="x-default" href="{default_url}">')
        
        for lang_code, base_url in LANGUAGES.items():
            if lang_code == 'en':
                url = f"https://yt2mp3.lol/{page_slug}/"
            else:
                url = f"{base_url}/{page_slug}/"
            tags.append(f'<link rel="alternate" hreflang="{lang_code}" href="{url}">')
    
    elif page_type == 'limited_lang':
        # Limited language pages (e.g., youtube-mp3)
        supported_langs = LIMITED_LANG_PAGES.get(page_slug, ['en'])
        
        default_url = f"https://yt2mp3.lol/{page_slug}/"
        tags.append(f'<link rel="alternate" hreflang="x-default" href="{default_url}">')
        
        for lang_code in supported_langs:
            if lang_code == 'en':
                url = f"https://yt2mp3.lol/{page_slug}/"
            else:
                url = f"https://yt2mp3.lol/{lang_code}/{page_slug}/"
            tags.append(f'<link rel="alternate" hreflang="{lang_code}" href="{url}">')
    
    else:
        # Single language pages (e.g., ytmp3, youtube-audio-download-mp3)
        url = f"https://yt2mp3.lol/{page_path}/"
        tags.append(f'<link rel="alternate" hreflang="x-default" href="{url}">')
        tags.append(f'<link rel="alternate" hreflang="en" href="{url}">')
    
    return '\n'.join(tags)

def add_hreflang_to_page(filepath):
    """Add or update hreflang tags in a page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        page_path = get_page_path(filepath)
        
        # Remove existing hreflang tags
        content = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n?', '', content)
        
        # Generate new hreflang tags
        hreflang_tags = generate_hreflang_tags(page_path)
        
        # Insert before <meta name="robots"
        if '<meta name="robots"' in content:
            content = content.replace('<meta name="robots"', f'{hreflang_tags}\n<meta name="robots"')
        elif '</head>' in content:
            content = content.replace('</head>', f'{hreflang_tags}\n</head>')
        else:
            return False
        
        # Write back if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    """Process all HTML files"""
    web_dir = 'web'
    processed = 0
    updated = 0
    
    print("Adding comprehensive hreflang tags to all pages...\n")
    print("=" * 70)
    
    # Process specific page types
    pages_to_process = []
    
    # Homepage and language homepages
    pages_to_process.append('web/index.html')
    for lang in LANGUAGES.keys():
        if lang != 'en':
            pages_to_process.append(f'web/{lang}/index.html')
    
    # Tool pages (all languages)
    for tool in MULTI_LANG_PAGES:
        if tool:  # Skip empty string (homepage)
            pages_to_process.append(f'web/{tool}/index.html')
            for lang in LANGUAGES.keys():
                if lang != 'en':
                    pages_to_process.append(f'web/{lang}/{tool}/index.html')
    
    # Limited language pages
    for page, langs in LIMITED_LANG_PAGES.items():
        pages_to_process.append(f'web/{page}/index.html')
        for lang in langs:
            if lang != 'en':
                pages_to_process.append(f'web/{lang}/{page}/index.html')
    
    # Single language SEO pages
    single_lang_pages = ['ytmp3', 'youtube-audio-download-mp3', 'download-lagu-youtube']
    for page in single_lang_pages:
        pages_to_process.append(f'web/{page}/index.html')
    
    # Process all pages
    for filepath in pages_to_process:
        if os.path.exists(filepath):
            processed += 1
            if add_hreflang_to_page(filepath):
                updated += 1
                print(f"✓ {filepath}")
    
    print("=" * 70)
    print(f"\n✓ Processed {processed} HTML files")
    print(f"✓ Updated {updated} files with hreflang tags")
    print("\nAll pages now have proper hreflang tags for:")
    print("  • Language variants")
    print("  • x-default fallback")
    print("  • Proper international SEO")

if __name__ == '__main__':
    main()
