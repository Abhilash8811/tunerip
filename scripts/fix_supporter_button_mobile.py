#!/usr/bin/env python3
"""Fix Supporter button for mobile by adding touch-action and other mobile-friendly CSS"""

import os
import re

# Old CSS pattern
old_pattern = r'\.btn-supporter\{display:inline-flex;align-items:center;gap:8px;background:var\(--accent\);color:var\(--accent-text\);border:0;border-radius:var\(--radius-sm\);padding:10px 16px;font-weight:700;font-size:14px;cursor:pointer;min-height:var\(--tap\)\}'

# New CSS with mobile fixes
new_css = '.btn-supporter{display:inline-flex;align-items:center;gap:8px;background:var(--accent);color:var(--accent-text);border:0;border-radius:var(--radius-sm);padding:10px 16px;font-weight:700;font-size:14px;cursor:pointer;min-height:var(--tap);touch-action:manipulation;-webkit-tap-highlight-color:transparent;user-select:none;-webkit-user-select:none}'

def fix_html_file(filepath):
    """Fix supporter button CSS in HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file contains the old pattern
        if re.search(old_pattern, content):
            # Replace the pattern
            new_content = re.sub(old_pattern, new_css, content)
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Fixed: {filepath}")
            return True
        return False
    except Exception as e:
        print(f"✗ Error fixing {filepath}: {e}")
        return False

def main():
    """Find and fix all HTML files"""
    web_dir = 'web'
    fixed_count = 0
    
    print("Fixing Supporter button for mobile in all HTML files...\n")
    
    # Walk through all HTML files
    for root, dirs, files in os.walk(web_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                if fix_html_file(filepath):
                    fixed_count += 1
    
    print(f"\n✓ Fixed {fixed_count} HTML files")
    print("Supporter button now has better mobile touch support!")

if __name__ == '__main__':
    main()
