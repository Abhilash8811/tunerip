#!/usr/bin/env python3
"""
Fix critical SEO issues:
1. Add trailing slashes to canonicals in build.js generated pages
2. Add hreflang tags to build.js generated pages
3. Fix broken hreflang on locale pages (x-default should point to /)
4. Add complete hreflang matrix to all locale pages
"""

import os
import re
from pathlib import Path

# Configuration
SITE = "https://yt2mp3.lol"
LANGUAGES = [
    ("en", "/"),
    ("ar", "/ar/"),
    ("bn", "/bn/"),
    ("de", "/de/"),
    ("es", "/es/"),
    ("fil", "/fil/"),
    ("fr", "/fr/"),
    ("hi", "/hi/"),
    ("id", "/id/"),
    ("it", "/it/"),
    ("ja", "/ja/"),
    ("ko", "/ko/"),
    ("pt", "/pt/"),
    ("ru", "/ru/"),
    ("th", "/th/"),
    ("tr", "/tr/"),
    ("ur", "/ur/"),
    ("vi", "/vi/"),
]

def generate_hreflang_tags(include_x_default=True):
    """Generate complete hreflang tag set"""
    tags = []
    if include_x_default:
        tags.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}/">')
    for lang_code, lang_path in LANGUAGES:
        tags.append(f'<link rel="alternate" hreflang="{lang_code}" href="{SITE}{lang_path}">')
    return "\n".join(tags)

def fix_locale_homepage(file_path, lang_code):
    """Fix hreflang tags on a locale homepage"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove existing broken hreflang tags
    content = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n?', '', content)
    
    # Find the canonical tag and insert hreflang tags after it
    canonical_pattern = r'(<link rel="canonical" href="[^"]*">)'
    
    if re.search(canonical_pattern, content):
        hreflang_tags = generate_hreflang_tags(include_x_default=True)
        content = re.sub(
            canonical_pattern,
            r'\1\n' + hreflang_tags,
            content,
            count=1
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def fix_generated_page(file_path):
    """Fix canonical trailing slash and add hreflang to build.js generated pages"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Fix canonical trailing slash (if missing)
    # Match canonical without trailing slash before closing >
    canonical_pattern = r'<link rel="canonical" href="(https://yt2mp3\.lol/[^/"]+)">'
    if re.search(canonical_pattern, content):
        content = re.sub(
            canonical_pattern,
            r'<link rel="canonical" href="\1/">',
            content
        )
        modified = True
    
    # Add hreflang tags if missing
    if 'hreflang="x-default"' not in content:
        canonical_pattern = r'(<link rel="canonical" href="[^"]*">)'
        if re.search(canonical_pattern, content):
            hreflang_tags = generate_hreflang_tags(include_x_default=True)
            content = re.sub(
                canonical_pattern,
                r'\1\n' + hreflang_tags,
                content,
                count=1
            )
            modified = True
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return modified

def main():
    web_dir = Path("web")
    
    print("=" * 70)
    print("Fixing critical SEO issues...")
    print("=" * 70)
    
    # Fix locale homepages
    print("\n1. Fixing locale homepage hreflang tags...")
    locale_count = 0
    for lang_code, lang_path in LANGUAGES:
        if lang_code == "en":
            continue  # Skip English (main homepage)
        
        locale_file = web_dir / lang_path.strip('/') / "index.html"
        if locale_file.exists():
            if fix_locale_homepage(locale_file, lang_code):
                print(f"   ✓ Fixed {lang_path}")
                locale_count += 1
    
    print(f"\n   Fixed {locale_count} locale homepages")
    
    # Fix build.js generated pages
    print("\n2. Fixing build.js generated pages (canonical + hreflang)...")
    generated_pages = [
        "youtube-to-mp4-converter",
        "youtube-to-mp3-320kbps-converter",
        "youtube-shorts-downloader",
        "youtube-playlist-downloader",
        "youtube-multi-downloader",
        "wav-converter",
        "m4a-converter",
        "iphone-converter",
        "android-converter",
        "how-to-install",
        "faq",
        "about",
        "contact",
        "copyright-claims",
        "privacy-policy",
        "terms-of-use",
    ]
    
    generated_count = 0
    for page_slug in generated_pages:
        page_file = web_dir / page_slug / "index.html"
        if page_file.exists():
            if fix_generated_page(page_file):
                print(f"   ✓ Fixed /{page_slug}/")
                generated_count += 1
    
    print(f"\n   Fixed {generated_count} generated pages")
    
    print("\n" + "=" * 70)
    print(f"✓ Complete! Fixed {locale_count + generated_count} pages total")
    print("=" * 70)
    print("\nFixed issues:")
    print("  • Canonical URLs now have trailing slashes")
    print("  • All pages have complete hreflang matrix (18 languages)")
    print("  • x-default points to / (not locale pages)")
    print("  • Build.js generated pages now have hreflang tags")

if __name__ == "__main__":
    main()
