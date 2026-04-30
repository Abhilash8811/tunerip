#!/usr/bin/env python3
"""
Script to fix ad initialization in all HTML files
Removes the inline AdProvider initialization and adds defer to ads.js
"""

import os
import re
from pathlib import Path


def fix_html_file(filepath):
    """Fix ad initialization in an HTML file"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modified = False
    
    # 1. Remove the inline AdProvider initialization block
    pattern = r'\n<!-- Initialize Ad Provider -->\n<script>\n\(AdProvider = window\.AdProvider \|\| \[\]\)\.push\(\{"serve": \{\}\}\);\n</script>\n'
    if re.search(pattern, content):
        content = re.sub(pattern, '\n', content)
        modified = True
        print("  ✓ Removed inline AdProvider initialization")
    
    # 2. Add defer to ads.js if not present
    if '<script src="/assets/ads.js"></script>' in content:
        content = content.replace(
            '<script src="/assets/ads.js"></script>',
            '<script src="/assets/ads.js" defer></script>'
        )
        modified = True
        print("  ✓ Added defer to ads.js")
    
    # Only write if modified
    if modified and content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Successfully updated {filepath}")
        return True
    else:
        print(f"  ⚠️  No changes needed for {filepath}")
        return False


def main():
    """Process all HTML files in the web directory"""
    web_dir = Path('web')
    
    if not web_dir.exists():
        print("Error: web directory not found")
        return
    
    # Find all HTML files
    html_files = list(web_dir.rglob('*.html'))
    
    print(f"Found {len(html_files)} HTML files\n")
    
    updated_count = 0
    skipped_count = 0
    
    for html_file in html_files:
        result = fix_html_file(html_file)
        if result:
            updated_count += 1
        else:
            skipped_count += 1
        print()
    
    print("=" * 60)
    print(f"✅ Updated: {updated_count} files")
    print(f"⏭️  Skipped: {skipped_count} files")
    print(f"📊 Total: {len(html_files)} files")
    print("=" * 60)


if __name__ == '__main__':
    main()
