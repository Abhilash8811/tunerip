#!/usr/bin/env python3
"""
Update critical CSS in all HTML files with ad container dimensions for CLS fix
"""

import os
import re
from pathlib import Path

# Read the new critical CSS
with open('web/assets/critical.css', 'r', encoding='utf-8') as f:
    new_critical_css = f.read()

# Find all HTML files
html_files = []
for root, dirs, files in os.walk('web'):
    # Skip hidden directories
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

print(f"Found {len(html_files)} HTML files")

# Update each file
updated_count = 0
for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has critical CSS section
        if '<!-- Critical CSS inlined for performance -->' not in content:
            print(f"⚠️  Skipping {filepath} - no critical CSS section found")
            continue
        
        # Replace the critical CSS content between <style> tags
        pattern = r'(<!-- Critical CSS inlined for performance -->\s*<style>)(.*?)(</style>)'
        
        def replace_css(match):
            return match.group(1) + '\n' + new_critical_css + '\n' + match.group(3)
        
        new_content = re.sub(pattern, replace_css, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1
            print(f"✅ Updated: {filepath}")
        else:
            print(f"⏭️  No change: {filepath}")
            
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")

print(f"\n✅ Successfully updated {updated_count}/{len(html_files)} files")
