#!/usr/bin/env python3
"""
Fix additional critical SEO issues (Part 1):
1. Remove fake aggregateRating from all pages
2. Fix Windows path leak in BreadcrumbList
3. Fix sitemap lastmod dates (use current date, not future)
"""

import os
import re
from pathlib import Path
from datetime import datetime

def remove_fake_ratings(file_path):
    """Remove fake aggregateRating from structured data"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove aggregateRating from WebApplication schema
    pattern = r',"aggregateRating":\{"@type":"AggregateRating","ratingValue":"[^"]*","ratingCount":"[^"]*"\}'
    if re.search(pattern, content):
        content = re.sub(pattern, '', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def fix_breadcrumb_paths(file_path):
    """Fix Windows path leaks in BreadcrumbList"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix backslashes in URLs
    pattern = r'(https://yt2mp3\.lol/[^"]*?)\\+'
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1/', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def fix_sitemap_dates():
    """Fix sitemap lastmod dates to current date"""
    sitemap_path = Path("public/sitemap.xml")
    
    if not sitemap_path.exists():
        return False
    
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Replace all future dates with current date
    content = re.sub(r'<lastmod>2026-05-01</lastmod>', f'<lastmod>{current_date}</lastmod>', content)
    
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    web_dir = Path("web")
    
    print("=" * 70)
    print("Fixing critical SEO issues (Part 1)...")
    print("=" * 70)
    
    # 1. Remove fake ratings
    print("\n1. Removing fake aggregateRating from all pages...")
    rating_count = 0
    
    for html_file in web_dir.rglob("index.html"):
        if remove_fake_ratings(html_file):
            print(f"   ✓ Removed from {html_file.relative_to(web_dir)}")
            rating_count += 1
    
    print(f"\n   Removed fake ratings from {rating_count} pages")
    
    # 2. Fix breadcrumb paths
    print("\n2. Fixing Windows path leaks in BreadcrumbList...")
    breadcrumb_count = 0
    
    for html_file in web_dir.rglob("index.html"):
        if fix_breadcrumb_paths(html_file):
            print(f"   ✓ Fixed {html_file.relative_to(web_dir)}")
            breadcrumb_count += 1
    
    print(f"\n   Fixed {breadcrumb_count} breadcrumb paths")
    
    # 3. Fix sitemap dates
    print("\n3. Fixing sitemap lastmod dates...")
    if fix_sitemap_dates():
        current_date = datetime.now().strftime("%Y-%m-%d")
        print(f"   ✓ Updated all dates to {current_date}")
    else:
        print("   ✗ Sitemap not found")
    
    print("\n" + "=" * 70)
    print(f"✓ Complete!")
    print("=" * 70)
    print("\nFixed issues:")
    print("  • Removed fake aggregateRating (prevents manual penalty)")
    print("  • Fixed Windows path leaks in BreadcrumbList")
    print("  • Updated sitemap dates to current date")

if __name__ == "__main__":
    main()
