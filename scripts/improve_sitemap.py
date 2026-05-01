#!/usr/bin/env python3
"""Improve sitemap with lastmod dates and proper formatting"""

from datetime import datetime
import xml.etree.ElementTree as ET

def create_improved_sitemap():
    """Create an improved sitemap with lastmod dates"""
    
    # Current date for lastmod
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Create root element with proper namespace
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    urlset.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    urlset.set('xsi:schemaLocation', 'http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd')
    
    # Define all URLs with their priorities
    urls = [
        # Main Homepage
        ('https://yt2mp3.lol/', '1.0', 'daily'),
        
        # Language Homepages
        ('https://yt2mp3.lol/ar/', '0.9', 'daily'),
        ('https://yt2mp3.lol/bn/', '0.9', 'daily'),
        ('https://yt2mp3.lol/de/', '0.9', 'daily'),
        ('https://yt2mp3.lol/es/', '0.9', 'daily'),
        ('https://yt2mp3.lol/fil/', '0.9', 'daily'),
        ('https://yt2mp3.lol/fr/', '0.9', 'daily'),
        ('https://yt2mp3.lol/hi/', '0.9', 'daily'),
        ('https://yt2mp3.lol/id/', '0.9', 'daily'),
        ('https://yt2mp3.lol/it/', '0.9', 'daily'),
        ('https://yt2mp3.lol/ja/', '0.9', 'daily'),
        ('https://yt2mp3.lol/ko/', '0.9', 'daily'),
        ('https://yt2mp3.lol/pt/', '0.9', 'daily'),
        ('https://yt2mp3.lol/ru/', '0.9', 'daily'),
        ('https://yt2mp3.lol/th/', '0.9', 'daily'),
        ('https://yt2mp3.lol/tr/', '0.9', 'daily'),
        ('https://yt2mp3.lol/ur/', '0.9', 'daily'),
        ('https://yt2mp3.lol/vi/', '0.9', 'daily'),
        
        # SEO Pages (High Priority)
        ('https://yt2mp3.lol/youtube-mp3/', '1.0', 'weekly'),
        ('https://yt2mp3.lol/ytmp3/', '1.0', 'weekly'),
        ('https://yt2mp3.lol/youtube-audio-download-mp3/', '1.0', 'weekly'),
        ('https://yt2mp3.lol/download-lagu-youtube/', '0.95', 'weekly'),
        
        # YouTube MP3 Language Pages
        ('https://yt2mp3.lol/es/youtube-mp3/', '0.95', 'weekly'),
        ('https://yt2mp3.lol/hi/youtube-mp3/', '0.95', 'weekly'),
        ('https://yt2mp3.lol/pt/youtube-mp3/', '0.95', 'weekly'),
        ('https://yt2mp3.lol/id/youtube-mp3/', '0.95', 'weekly'),
    ]
    
    # Add tool pages for all languages
    tools = ['youtube-shorts-downloader', 'youtube-playlist-downloader', 'youtube-multi-downloader']
    languages = ['', 'ar', 'bn', 'de', 'es', 'fil', 'fr', 'hi', 'id', 'it', 'ja', 'ko', 'pt', 'ru', 'th', 'tr', 'ur', 'vi']
    
    for tool in tools:
        for lang in languages:
            if lang:
                url = f'https://yt2mp3.lol/{lang}/{tool}/'
                priority = '0.85' if tool == 'youtube-shorts-downloader' else '0.75'
            else:
                url = f'https://yt2mp3.lol/{tool}/'
                priority = '0.9' if tool == 'youtube-shorts-downloader' else '0.8'
            
            urls.append((url, priority, 'weekly'))
    
    # Other converter pages
    other_pages = [
        ('https://yt2mp3.lol/youtube-to-mp4-converter/', '0.9', 'weekly'),
        ('https://yt2mp3.lol/youtube-to-mp3-320kbps-converter/', '0.9', 'weekly'),
        ('https://yt2mp3.lol/wav-converter/', '0.8', 'weekly'),
        ('https://yt2mp3.lol/m4a-converter/', '0.8', 'weekly'),
        ('https://yt2mp3.lol/iphone-converter/', '0.8', 'weekly'),
        ('https://yt2mp3.lol/android-converter/', '0.8', 'weekly'),
        
        # Info pages
        ('https://yt2mp3.lol/how-to-install/', '0.8', 'weekly'),
        ('https://yt2mp3.lol/faq/', '0.8', 'weekly'),
        ('https://yt2mp3.lol/about/', '0.8', 'weekly'),
        ('https://yt2mp3.lol/contact/', '0.4', 'yearly'),
        
        # Legal pages
        ('https://yt2mp3.lol/copyright-claims/', '0.4', 'yearly'),
        ('https://yt2mp3.lol/privacy-policy/', '0.4', 'yearly'),
        ('https://yt2mp3.lol/terms-of-use/', '0.4', 'yearly'),
    ]
    
    urls.extend(other_pages)
    
    # Create URL entries
    for loc, priority, changefreq in urls:
        url_elem = ET.SubElement(urlset, 'url')
        
        loc_elem = ET.SubElement(url_elem, 'loc')
        loc_elem.text = loc
        
        lastmod_elem = ET.SubElement(url_elem, 'lastmod')
        lastmod_elem.text = today
        
        changefreq_elem = ET.SubElement(url_elem, 'changefreq')
        changefreq_elem.text = changefreq
        
        priority_elem = ET.SubElement(url_elem, 'priority')
        priority_elem.text = priority
    
    # Create tree and write to file
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space='  ')
    
    # Write with XML declaration
    with open('web/sitemap.xml', 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding='utf-8', xml_declaration=False)
    
    print(f"✓ Created improved sitemap with {len(urls)} URLs")
    print(f"✓ Added lastmod date: {today}")
    print(f"✓ Added proper XML schema declaration")
    print(f"✓ Formatted with proper indentation")
    
    return len(urls)

if __name__ == '__main__':
    print("Creating improved sitemap...\n")
    print("=" * 60)
    
    url_count = create_improved_sitemap()
    
    print("=" * 60)
    print(f"\n✓ Sitemap ready with {url_count} URLs")
    print("\nImprovements:")
    print("  • Added lastmod dates (helps Google prioritize crawling)")
    print("  • Added XML schema declaration (validates properly)")
    print("  • Proper formatting and indentation")
    print("  • All URLs have trailing slashes")
    print("\nNext steps:")
    print("  1. Resubmit sitemap in Google Search Console")
    print("  2. Wait 24-48 hours for processing")
    print("  3. Check Coverage report for indexed pages")
