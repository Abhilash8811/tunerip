#!/usr/bin/env python3
"""
Script to add Adsterra ads to all HTML pages
"""

import os
import re
from pathlib import Path

def update_html_file(filepath):
    """Add Adsterra ads to an HTML file"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has Adsterra
    if 'ads-adsterra.js' in content or 'highperformanceformat.com' in content:
        print(f"  ✓ Already has Adsterra ads")
        return False
    
    original_content = content
    modified = False
    
    # 1. Remove old ExoClick script if present
    if 'a.magsrv.com/ad-provider.js' in content:
        content = re.sub(
            r'<!-- (ExoClick )?Ad Provider Script -->\n<script async type="application/javascript" src="https://a\.magsrv\.com/ad-provider\.js"></script>\n\n',
            '',
            content
        )
        print("  ✓ Removed old ExoClick script")
        modified = True
    
    # 2. Replace ads.js with ads-adsterra.js
    if '<script src="/assets/ads.js"' in content:
        content = content.replace(
            '<script src="/assets/ads.js"',
            '<script src="/assets/ads-adsterra.js"'
        )
        print("  ✓ Switched to ads-adsterra.js")
        modified = True
    elif '</body>' in content and 'ads-adsterra.js' not in content:
        # Add ads-adsterra.js before </body> if not present
        content = content.replace(
            '</body>',
            '<script src="/assets/ads-adsterra.js" defer></script>\n\n</body>'
        )
        print("  ✓ Added ads-adsterra.js")
        modified = True
    
    # 3. Add native banner if it's a main page (has converter or main content)
    if 'class="converter-card"' in content or 'class="hero"' in content:
        # Check if native banner already exists
        if '2ccf98a24a20e1363cee99b6956d273e' not in content:
            # Find a good spot - after a section but before FAQ
            patterns = [
                (r'(</section>\n\n)(<section[^>]*class="[^"]*faq[^"]*")', 
                 r'\1<!-- Adsterra Native Banner -->\n<div style="text-align: center; margin: 40px auto; max-width: 1200px;">\n  <div style="font-size: 10px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 12px; opacity: 0.7;">Sponsored Content</div>\n  <script async="async" data-cfasync="false" src="https://pl29304694.profitablecpmratenetwork.com/2ccf98a24a20e1363cee99b6956d273e/invoke.js"></script>\n  <div id="container-2ccf98a24a20e1363cee99b6956d273e"></div>\n</div>\n\n\2'),
            ]
            
            for pattern, replacement in patterns:
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content, count=1)
                    print("  ✓ Added native banner")
                    modified = True
                    break
    
    # Only write if modified
    if modified and content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Successfully updated")
        return True
    else:
        print(f"  ⚠️  No changes needed")
        return False


def main():
    """Process all HTML files"""
    web_dir = Path('web')
    
    if not web_dir.exists():
        print("Error: web directory not found")
        return
    
    # Find all HTML files
    html_files = list(web_dir.rglob('*.html'))
    
    # Exclude test files
    html_files = [f for f in html_files if 'test' not in str(f).lower()]
    
    print(f"Found {len(html_files)} HTML files\n")
    
    updated_count = 0
    skipped_count = 0
    
    for html_file in html_files:
        result = update_html_file(html_file)
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
