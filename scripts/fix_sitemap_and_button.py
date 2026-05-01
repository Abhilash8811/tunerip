#!/usr/bin/env python3
"""Fix sitemap URLs and ensure supporter button has proper attributes"""

import os
import re

def fix_sitemap():
    """Add trailing slashes to all URLs in sitemap"""
    sitemap_path = 'web/sitemap.xml'
    
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix URLs without trailing slashes (but not the ones that already have them)
    # Match URLs that don't end with / before </loc>
    content = re.sub(
        r'<loc>(https://yt2mp3\.lol/[^<]+)(?<!/)(<\/loc>)',
        r'<loc>\1/\2',
        content
    )
    
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Fixed sitemap.xml - added trailing slashes to all URLs")

def fix_supporter_button_html():
    """Ensure supporter button has type='button' attribute in all HTML files"""
    web_dir = 'web'
    fixed_count = 0
    
    # Pattern to find supporter buttons without explicit type or with wrong type
    pattern = r'<button\s+([^>]*?)class="btn-supporter"([^>]*?)>'
    
    for root, dirs, files in os.walk(web_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    original_content = content
                    
                    # Find all supporter buttons
                    def fix_button(match):
                        before = match.group(1)
                        after = match.group(2)
                        
                        # Check if type="button" already exists
                        if 'type="button"' in before or 'type="button"' in after:
                            return match.group(0)  # Already has type="button"
                        
                        # Add type="button" at the beginning
                        return f'<button type="button" {before}class="btn-supporter"{after}>'
                    
                    content = re.sub(pattern, fix_button, content)
                    
                    if content != original_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        fixed_count += 1
                        print(f"✓ Fixed: {filepath}")
                
                except Exception as e:
                    print(f"✗ Error fixing {filepath}: {e}")
    
    if fixed_count > 0:
        print(f"\n✓ Fixed {fixed_count} HTML files")
    else:
        print("\n✓ All HTML files already have correct button attributes")

def main():
    print("Fixing sitemap and supporter button issues...\n")
    print("=" * 60)
    print("ISSUE 1: Sitemap URLs")
    print("=" * 60)
    fix_sitemap()
    
    print("\n" + "=" * 60)
    print("ISSUE 2: Supporter Button Attributes")
    print("=" * 60)
    fix_supporter_button_html()
    
    print("\n" + "=" * 60)
    print("✓ All fixes complete!")
    print("=" * 60)

if __name__ == '__main__':
    main()
