#!/usr/bin/env python3
"""
Script to add ad integration to all HTML pages
Adds: ad provider script, CSS, ad containers, and initialization
"""

import os
import re
from pathlib import Path

# Ad components to inject
AD_PROVIDER_SCRIPT = '''<link rel="stylesheet" href="/assets/ads.css">

<!-- Ad Provider Script -->
<script async type="application/javascript" src="https://a.magsrv.com/ad-provider.js"></script>

'''

AD_TOP_BANNER = '''
<!-- Ad: Top Banner -->
<div class="ad-container ad-top-banner ad-lazy" data-ad-type="banner-top">
  <div class="ad-label">Advertisement</div>
</div>

'''

AD_BELOW_CONVERTER = '''
<!-- Ad: Below Converter -->
<div class="ad-container ad-below-converter ad-lazy" data-ad-type="banner-bottom">
  <div class="ad-label">Advertisement</div>
</div>

'''

AD_IN_CONTENT = '''
<!-- Ad: In-Content -->
<div class="ad-container ad-native ad-lazy" data-ad-type="in-content">
  <div class="ad-label">Sponsored</div>
</div>

'''

AD_SIDEBAR = '''
  <!-- Ad: Sidebar (Desktop Only) -->
  <aside class="sidebar">
    <div class="ad-container ad-sidebar ad-lazy" data-ad-type="sidebar">
      <div class="ad-label">Advertisement</div>
    </div>
  </aside>

</div>

'''

AD_STICKY_BOTTOM = '''
<!-- Ad: Mobile Sticky Bottom -->
<div class="ad-sticky-bottom ad-lazy" data-ad-type="sticky">
  <button class="ad-close-btn" aria-label="Close ad">
    <svg width="12" height="12" viewBox="0 0 24 24" fill="none">
      <path d="M18 6L6 18M6 6l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    </svg>
  </button>
  <div class="ad-label">Advertisement</div>
</div>

'''

AD_SCRIPTS = '''<script src="/assets/ads.js"></script>

<!-- Initialize Ad Provider -->
<script>
(AdProvider = window.AdProvider || []).push({"serve": {}});
</script>

'''


def process_html_file(filepath):
    """Add ad components to an HTML file"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has ads
    if 'ads.css' in content or 'ad-provider.js' in content:
        print(f"  ✓ Already has ads, skipping")
        return False
    
    original_content = content
    modified = False
    
    # 1. Add ad CSS and provider script in <head> after style.css
    if '<link rel="stylesheet" href="/assets/style.css?v=2">' in content:
        content = content.replace(
            '<link rel="stylesheet" href="/assets/style.css?v=2">',
            '<link rel="stylesheet" href="/assets/style.css?v=2">\n' + AD_PROVIDER_SCRIPT
        )
        modified = True
        print("  ✓ Added ad provider script and CSS")
    
    # 2. Add has-sticky-ad class to body
    content = re.sub(r'<body>', '<body class="has-sticky-ad">', content)
    
    # 3. Add top banner after </header> and before <main>
    if '</header>' in content and '<main>' in content:
        content = content.replace(
            '</header>\n\n<main>',
            '</header>\n\n<main>\n' + AD_TOP_BANNER
        )
        print("  ✓ Added top banner")
    
    # 4. Add below-converter ad (after hero/converter section)
    # Look for the end of hero section or converter card
    patterns = [
        (r'(</section>\n\n)(<section class="section">)', r'\1' + AD_BELOW_CONVERTER + r'\2'),
        (r'(  </div>\n</section>\n\n)(<section class="section">)', r'\1' + AD_BELOW_CONVERTER + r'\2'),
    ]
    
    for pattern, replacement in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content, count=1)
            print("  ✓ Added below-converter ad")
            break
    
    # 5. Wrap content sections in content-with-sidebar div
    # Find first <section class="section"> after hero
    if '<div class="content-with-sidebar">' not in content:
        # Find the first section after the converter
        match = re.search(r'(</section>\n\n)(<!-- Ad: Below Converter -->.*?</div>\n\n)?(<section class="section">)', content, re.DOTALL)
        if match:
            before = match.group(1)
            ad = match.group(2) or ''
            section = match.group(3)
            content = content.replace(
                before + ad + section,
                before + ad + '<div class="content-with-sidebar">\n  <div class="main-content">\n\n' + section
            )
            print("  ✓ Added content-with-sidebar wrapper")
    
    # 6. Add in-content ad (between sections, before FAQ or last section)
    # Find a good spot - typically before "Why" or "FAQ" section
    patterns_for_incontent = [
        r'(</section>\n\n)(<section class="section alt">[\s\S]*?<h2>[^<]*(?:Why|Por qué|Pourquoi|Warum)[^<]*</h2>)',
        r'(</section>\n\n)(<section[^>]*class="[^"]*faq[^"]*")',
    ]
    
    for pattern in patterns_for_incontent:
        if re.search(pattern, content):
            content = re.sub(pattern, r'\1' + AD_IN_CONTENT + r'\2', content, count=1)
            print("  ✓ Added in-content ad")
            break
    
    # 7. Add sidebar and close content-with-sidebar div before footer
    if '<footer class="site-footer">' in content and '<aside class="sidebar">' not in content:
        content = content.replace(
            '\n\n<footer class="site-footer">',
            '\n\n  </div>\n\n' + AD_SIDEBAR + '<footer class="site-footer">'
        )
        print("  ✓ Added sidebar ad")
    
    # 8. Add sticky bottom ad before closing </body>
    if '<div class="ad-sticky-bottom' not in content:
        content = content.replace(
            '\n</body>',
            '\n' + AD_STICKY_BOTTOM + '</body>'
        )
        print("  ✓ Added sticky bottom ad")
    
    # 9. Add ad scripts before closing </body>
    if '/assets/ads.js' not in content:
        # Find the app.js script and add ads.js after it
        content = re.sub(
            r'(<script src="/assets/app\.js\?v=2"[^>]*></script>)',
            r'\1\n' + AD_SCRIPTS,
            content
        )
        print("  ✓ Added ad scripts")
    
    # Only write if modified
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Successfully updated {filepath}")
        return True
    else:
        print(f"  ⚠️  No changes made to {filepath}")
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
        result = process_html_file(html_file)
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
