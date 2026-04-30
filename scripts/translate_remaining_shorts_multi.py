#!/usr/bin/env python3
"""
Translate shorts and multi pages for remaining languages: bn, de, es, fr, fil, ar, pt
"""

from pathlib import Path

# Shorts translations for remaining languages
shorts_translations = {
    'bn': {
        'YouTube Shorts Downloader': 'YouTube Shorts ডাউনলোডার',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'YouTube Shorts ভিডিও MP3 বা MP4 ফরম্যাটে ডাউনলোড করুন। দ্রুত, বিনামূল্যে এবং ব্যবহার করা সহজ।',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, ইউটিউব শর্টস ডাউনলোড, শর্টস থেকে mp3',
    },
    'de': {
        'YouTube Shorts Downloader': 'YouTube Shorts Downloader',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'Laden Sie YouTube Shorts-Videos im MP3- oder MP4-Format herunter. Schnell, kostenlos und einfach zu bedienen.',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, youtube shorts herunterladen, shorts zu mp3',
    },
    'es': {
        'YouTube Shorts Downloader': 'Descargador de YouTube Shorts',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'Descarga videos de YouTube Shorts en formato MP3 o MP4. Rápido, gratis y fácil de usar.',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, descargar youtube shorts, shorts a mp3',
    },
    'fr': {
        'YouTube Shorts Downloader': 'Téléchargeur YouTube Shorts',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'Téléchargez des vidéos YouTube Shorts au format MP3 ou MP4. Rapide, gratuit et facile à utiliser.',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, télécharger youtube shorts, shorts en mp3',
    },
    'fil': {
        'YouTube Shorts Downloader': 'YouTube Shorts Downloader',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'I-download ang mga YouTube Shorts video sa MP3 o MP4 format. Mabilis, libre, at madaling gamitin.',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, i-download youtube shorts, shorts sa mp3',
    },
    'ar': {
        'YouTube Shorts Downloader': 'تنزيل YouTube Shorts',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'قم بتنزيل مقاطع فيديو YouTube Shorts بتنسيق MP3 أو MP4. سريع ومجاني وسهل الاستخدام.',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, تنزيل يوتيوب شورتس, شورتس إلى mp3',
    },
    'pt': {
        'YouTube Shorts Downloader': 'Baixador de YouTube Shorts',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'Baixe vídeos do YouTube Shorts em formato MP3 ou MP4. Rápido, gratuito e fácil de usar.',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, baixar youtube shorts, shorts para mp3',
    },
}

# Multi translations for remaining languages
multi_translations = {
    'bn': {
        'YouTube Multi Downloader': 'YouTube মাল্টি ডাউনলোডার',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'একসাথে একাধিক YouTube ভিডিও ডাউনলোড করুন। একাধিক URL পেস্ট করুন এবং সবগুলি একবারে রূপান্তর করুন।',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, একাধিক ইউটিউব ডাউনলোড, বাল্ক ডাউনলোড',
    },
    'de': {
        'YouTube Multi Downloader': 'YouTube Multi Downloader',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'Laden Sie mehrere YouTube-Videos gleichzeitig herunter. Fügen Sie mehrere URLs ein und konvertieren Sie alle auf einmal.',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, mehrere youtube herunterladen, massendownload',
    },
    'es': {
        'YouTube Multi Downloader': 'Descargador Múltiple de YouTube',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'Descarga múltiples videos de YouTube a la vez. Pega múltiples URLs y conviértelos todos de una vez.',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, descargar múltiples youtube, descarga masiva',
    },
    'fr': {
        'YouTube Multi Downloader': 'Téléchargeur Multiple YouTube',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'Téléchargez plusieurs vidéos YouTube à la fois. Collez plusieurs URLs et convertissez-les toutes en une seule fois.',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, télécharger plusieurs youtube, téléchargement en masse',
    },
    'fil': {
        'YouTube Multi Downloader': 'YouTube Multi Downloader',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'I-download ang maraming YouTube videos nang sabay-sabay. I-paste ang maraming URLs at i-convert silang lahat nang sabay.',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, i-download maraming youtube, bulk download',
    },
    'ar': {
        'YouTube Multi Downloader': 'تنزيل متعدد من YouTube',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'قم بتنزيل مقاطع فيديو YouTube متعددة دفعة واحدة. الصق عدة عناوين URL وقم بتحويلها جميعًا دفعة واحدة.',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, تنزيل متعدد يوتيوب, تنزيل جماعي',
    },
    'pt': {
        'YouTube Multi Downloader': 'Baixador Múltiplo do YouTube',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'Baixe vários vídeos do YouTube de uma vez. Cole vários URLs e converta todos de uma só vez.',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, baixar vários youtube, download em massa',
    },
}

def translate_file(file_path, translations):
    """Apply translations to a file"""
    if not Path(file_path).exists():
        print(f"✗ File not found: {file_path}")
        return
        
    content = Path(file_path).read_text(encoding='utf-8')
    
    for en, translated in translations.items():
        content = content.replace(en, translated)
    
    Path(file_path).write_text(content, encoding='utf-8')
    print(f"✓ {file_path}")

# Translate shorts pages
print("Translating Shorts pages for remaining languages...")
for lang in ['bn', 'de', 'es', 'fr', 'fil', 'ar', 'pt']:
    file_path = f'web/{lang}/youtube-shorts-downloader/index.html'
    translate_file(file_path, shorts_translations.get(lang, {}))

# Translate multi pages
print("\nTranslating Multi-downloader pages for remaining languages...")
for lang in ['bn', 'de', 'es', 'fr', 'fil', 'ar', 'pt']:
    file_path = f'web/{lang}/youtube-multi-downloader/index.html'
    translate_file(file_path, multi_translations.get(lang, {}))

print("\n✅ All remaining shorts and multi pages translated!")
