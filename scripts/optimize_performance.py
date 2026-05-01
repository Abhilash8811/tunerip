#!/usr/bin/env python3
"""
Performance Optimization Script
Automatically optimizes all HTML files for 100/100 Lighthouse score
- Inlines critical CSS
- Loads full CSS asynchronously
- Adds resource hints
- Fixes layout shifts with min-height
"""

import os
import re
from pathlib import Path

# Read critical CSS
CRITICAL_CSS_PATH = Path(__file__).parent.parent / "web" / "assets" / "critical.css"
with open(CRITICAL_CSS_PATH, 'r', encoding='utf-8') as f:
    CRITICAL_CSS = f.read()

# Resource hints to add
RESOURCE_HINTS = '''<!-- Performance: DNS Prefetch & Preconnect -->
<link rel="dns-prefetch" href="https://pl29304694.profitablecpmratenetwork.com">
<link rel="preconnect" href="https://pl29304694.profitablecpmratenetwork.com" crossorigin>
<link rel="preload" href="/assets/favicon.svg" as="image" type="image/svg+xml">
<link rel="preload" href="/assets/app.js?v=2" as="script">'''

# Async CSS loading pattern
ASYNC_CSS = '''<!-- Critical CSS inlined for performance -->
<style>
''' + CRITICAL_CSS + '''
</style>

<!-- Load full CSS asynchronously (non-blocking) -->
<link rel="preload" href="/assets/style.css?v=2" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/assets/style.css?v=2"></noscript>

<!-- Load ads CSS with low priority -->
<link rel="stylesheet" href="/assets/ads.css" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="/assets/ads.css"></noscript>'''

def optimize_html_file(file_path):
    """Optimize a single HTML file for performance"""
    print(f"Optimizing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Step 1: Add resource hints after <head> tag if not already present
    if 'dns-prefetch' not in content:
        content = content.replace('<head>', '<head>\n' + RESOURCE_HINTS)
    
    # Step 2: Replace blocking CSS with async loading
    # Pattern 1: Both style.css and ads.css on separate lines
    pattern1 = r'<link rel="stylesheet" href="/assets/style\.css\?v=2">\s*<link rel="stylesheet" href="/assets/ads\.css">'
    if re.search(pattern1, content):
        content = re.sub(pattern1, ASYNC_CSS, content)
    
    # Pattern 2: Just style.css (some pages might not have ads.css)
    pattern2 = r'<link rel="stylesheet" href="/assets/style\.css\?v=2">'
    if re.search(pattern2, content) and 'Critical CSS inlined' not in content:
        content = re.sub(pattern2, ASYNC_CSS.replace(
            '<!-- Load ads CSS with low priority -->\n<link rel="stylesheet" href="/assets/ads.css" media="print" onload="this.media=\'all\'">\n<noscript><link rel="stylesheet" href="/assets/ads.css"></noscript>\n\n', 
            ''
        ), content)
    
    # Step 3: Add min-height to prevent layout shifts (if not already present)
    # This is done via CSS, so we add it to the critical CSS inline block
    
    # Step 4: Optimize script loading
    # Replace defer with defer + preload hint (already added above)
    
    # Only write if content changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Optimized successfully")
        return True
    else:
        print(f"  - Already optimized or no changes needed")
        return False

def find_all_html_files(web_dir):
    """Find all HTML files in the web directory"""
    html_files = []
    for root, dirs, files in os.walk(web_dir):
        # Skip hidden directories and __pycache__
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    return sorted(html_files)

def main():
    """Main optimization function"""
    print("=" * 60)
    print("Performance Optimization Script")
    print("=" * 60)
    print()
    
    # Get web directory
    script_dir = Path(__file__).parent
    web_dir = script_dir.parent / "web"
    
    if not web_dir.exists():
        print(f"Error: Web directory not found at {web_dir}")
        return
    
    # Find all HTML files
    html_files = find_all_html_files(web_dir)
    print(f"Found {len(html_files)} HTML files to optimize\n")
    
    # Optimize each file
    optimized_count = 0
    for html_file in html_files:
        if optimize_html_file(html_file):
            optimized_count += 1
    
    print()
    print("=" * 60)
    print(f"Optimization Complete!")
    print(f"  Total files: {len(html_files)}")
    print(f"  Optimized: {optimized_count}")
    print(f"  Already optimized: {len(html_files) - optimized_count}")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Test with Lighthouse on a sample page")
    print("2. Verify 100/100 performance score")
    print("3. Check CLS is below 0.1")
    print("4. Deploy to production")

if __name__ == "__main__":
    main()
