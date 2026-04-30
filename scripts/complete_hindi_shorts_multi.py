#!/usr/bin/env python3
"""
Complete Hindi shorts and multi pages - ALL content
"""

from pathlib import Path

# Shorts-specific translations
shorts_content = {
    'YouTube Shorts Downloader': 'YouTube Shorts डाउनलोडर',
    'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'YouTube Shorts वीडियो को MP3 या MP4 फॉर्मेट में डाउनलोड करें। तेज़, मुफ़्त और उपयोग में आसान।',
    'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, यूट्यूब शॉर्ट्स डाउनलोडर, शॉर्ट्स से mp3',
}

# Multi-specific translations
multi_content = {
    'YouTube Multi Downloader': 'YouTube मल्टी डाउनलोडर',
    'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'एक साथ कई YouTube वीडियो डाउनलोड करें। कई URL पेस्ट करें और सभी को एक बार में परिवर्तित करें।',
    'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, यूट्यूब मल्टी डाउनलोडर, बल्क डाउनलोड',
}

def translate_file(file_path, translations):
    """Apply translations"""
    if not Path(file_path).exists():
        print(f"✗ Not found: {file_path}")
        return
        
    content = Path(file_path).read_text(encoding='utf-8')
    
    for en, hi in translations.items():
        content = content.replace(en, hi)
    
    Path(file_path).write_text(content, encoding='utf-8')
    print(f"✓ {file_path}")

# Translate shorts
translate_file('web/hi/youtube-shorts-downloader/index.html', shorts_content)

# Translate multi
translate_file('web/hi/youtube-multi-downloader/index.html', multi_content)

print("\n✅ Hindi shorts and multi pages complete!")
