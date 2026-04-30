#!/usr/bin/env python3
"""
Add missing Adsterra Native Banner to all language version index pages
"""

import os
import re

# Native banner HTML to insert
NATIVE_BANNER = '''
<!-- Adsterra Native Banner -->
<div style="text-align: center; margin: 40px auto; max-width: 1200px;">
  <div style="font-size: 10px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 12px; opacity: 0.7;">Sponsored Content</div>
  <script async="async" data-cfasync="false" src="https://pl29304694.profitablecpmratenetwork.com/2ccf98a24a20e1363cee99b6956d273e/invoke.js"></script>
  <div id="container-2ccf98a24a20e1363cee99b6956d273e"></div>
</div>
'''

# Language directories
LANG_DIRS = [
    'web/ar', 'web/bn', 'web/de', 'web/es', 'web/fil', 'web/fr',
    'web/hi', 'web/id', 'web/it', 'web/ja', 'web/ko', 'web/pt',
    'web/ru', 'web/th', 'web/tr', 'web/ur', 'web/vi'
]

def add_native_banner(file_path):
    """Add native banner before FAQ section if not already present"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if native banner already exists
    if 'container-2ccf98a24a20e1363cee99b6956d273e' in content:
        print(f"✓ {file_path} - Native banner already exists")
        return False
    
    # Find the FAQ section
    faq_pattern = r'(<section id="faq")'
    
    if re.search(faq_pattern, content):
        # Insert native banner before FAQ section
        content = re.sub(faq_pattern, NATIVE_BANNER + r'\n\1', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file_path} - Added native banner")
        return True
    else:
        print(f"✗ {file_path} - FAQ section not found")
        return False

def main():
    updated_count = 0
    
    for lang_dir in LANG_DIRS:
        index_file = os.path.join(lang_dir, 'index.html')
        
        if os.path.exists(index_file):
            if add_native_banner(index_file):
                updated_count += 1
        else:
            print(f"✗ {index_file} - File not found")
    
    print(f"\n✅ Updated {updated_count} language version(s)")

if __name__ == '__main__':
    main()
