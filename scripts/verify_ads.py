#!/usr/bin/env python3
"""
Verify that all downloader pages have perfect ad implementation.
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent / "web"

LANGS = ['ar', 'bn', 'de', 'es', 'fil', 'fr', 'hi', 'id', 'it', 'ja', 'ko', 'pt', 'ru', 'th', 'tr', 'ur', 'vi']
PAGES = ['youtube-multi-downloader', 'youtube-shorts-downloader', 'youtube-playlist-downloader']

# Required ad placements
REQUIRED_ADS = [
    'ad-top-banner',
    'ad-below-converter',
    'ad-native',
    'ad-sidebar',
    'ad-sticky-bottom',
    'ads-adsterra.js',
    'container-2ccf98a24a20e1363cee99b6956d273e',  # Adsterra native banner
]

def verify_page(lang, page):
    """Verify a single page has all required ads."""
    file_path = BASE_DIR / lang / page / "index.html"
    
    if not file_path.exists():
        return False, "File not found"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    missing = []
    for ad in REQUIRED_ADS:
        if ad not in content:
            missing.append(ad)
    
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    
    return True, "✅ All ads present"

def main():
    """Verify all pages."""
    print("🔍 Verifying ad implementation in all 51 pages...\n")
    
    total = 0
    passed = 0
    failed = 0
    
    for lang in LANGS:
        print(f"📄 {lang}:")
        for page in PAGES:
            total += 1
            success, message = verify_page(lang, page)
            
            if success:
                passed += 1
                print(f"  ✅ {page}")
            else:
                failed += 1
                print(f"  ❌ {page}: {message}")
    
    print(f"\n📊 Results:")
    print(f"   Total: {total}")
    print(f"   Passed: {passed}")
    print(f"   Failed: {failed}")
    
    if failed == 0:
        print("\n🎉 Perfect! All pages have complete ad implementation!")
    else:
        print(f"\n⚠️  {failed} pages need attention")

if __name__ == "__main__":
    main()
