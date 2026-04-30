#!/usr/bin/env python3
"""
Verify all 6 ad placements on all 51 translated downloader pages
"""

from pathlib import Path
import re

# All languages
languages = ['ar', 'bn', 'de', 'es', 'fil', 'fr', 'hi', 'id', 'it', 'ja', 'ko', 'pt', 'ru', 'th', 'tr', 'ur', 'vi']

# All page types
page_types = [
    'youtube-playlist-downloader',
    'youtube-shorts-downloader',
    'youtube-multi-downloader'
]

# Required ad placements (6 total)
required_ads = [
    'ad-top-banner',           # 1. Top banner
    'ad-below-converter',      # 2. Below converter
    'ad-native',               # 3. In-content native
    '2ccf98a24a20e1363cee99b6956d273e',  # 4. Adsterra native banner script
    'ad-sidebar',              # 5. Sidebar (desktop)
    'ad-sticky-bottom'         # 6. Mobile sticky bottom
]

def verify_ads_in_file(file_path):
    """Check if all 6 ad placements exist in a file"""
    if not Path(file_path).exists():
        return False, f"File not found: {file_path}"
    
    content = Path(file_path).read_text(encoding='utf-8')
    
    missing_ads = []
    for ad in required_ads:
        if ad not in content:
            missing_ads.append(ad)
    
    if missing_ads:
        return False, f"Missing ads: {', '.join(missing_ads)}"
    
    return True, "All 6 ads present"

# Verify all pages
print("=" * 80)
print("VERIFYING ADS ON ALL 51 TRANSLATED PAGES")
print("=" * 80)

total_pages = 0
pages_with_all_ads = 0
pages_with_issues = []

for lang in languages:
    print(f"\n📍 Language: {lang.upper()}")
    print("-" * 80)
    
    for page_type in page_types:
        file_path = f'web/{lang}/{page_type}/index.html'
        total_pages += 1
        
        success, message = verify_ads_in_file(file_path)
        
        if success:
            pages_with_all_ads += 1
            print(f"  ✅ {page_type}: {message}")
        else:
            pages_with_issues.append((lang, page_type, message))
            print(f"  ❌ {page_type}: {message}")

# Summary
print("\n" + "=" * 80)
print("VERIFICATION SUMMARY")
print("=" * 80)
print(f"Total pages checked: {total_pages}")
print(f"Pages with all 6 ads: {pages_with_all_ads}")
print(f"Pages with issues: {len(pages_with_issues)}")

if pages_with_issues:
    print("\n⚠️  PAGES WITH MISSING ADS:")
    for lang, page_type, message in pages_with_issues:
        print(f"  - {lang}/{page_type}: {message}")
else:
    print("\n🎉 ALL 51 PAGES HAVE ALL 6 AD PLACEMENTS!")
    print("\nAd Placements Verified:")
    print("  1. ✅ Top Banner (ad-top-banner)")
    print("  2. ✅ Below Converter (ad-below-converter)")
    print("  3. ✅ In-Content Native (ad-native)")
    print("  4. ✅ Adsterra Native Banner (inline script)")
    print("  5. ✅ Sidebar Desktop (ad-sidebar)")
    print("  6. ✅ Mobile Sticky Bottom (ad-sticky-bottom)")

print("=" * 80)
