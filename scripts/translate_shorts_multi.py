#!/usr/bin/env python3
"""
Translate shorts-downloader and multi-downloader pages for all 17 languages
"""

from pathlib import Path

# Shorts-specific translations
shorts_translations = {
    'id': {
        'YouTube Shorts Downloader': 'YouTube Shorts Downloader',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'Unduh video YouTube Shorts dalam format MP3 atau MP4. Cepat, gratis, dan mudah digunakan.',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, unduh youtube shorts, shorts ke mp3',
    },
    'it': {
        'YouTube Shorts Downloader': 'YouTube Shorts Downloader',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'Scarica video YouTube Shorts in formato MP3 o MP4. Veloce, gratuito e facile da usare.',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, scarica youtube shorts, shorts a mp3',
    },
    'ja': {
        'YouTube Shorts Downloader': 'YouTube Shorts ダウンローダー',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'YouTube Shorts動画をMP3またはMP4形式でダウンロード。高速、無料、使いやすい。',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, youtubeショーツダウンロード, ショーツをmp3に',
    },
    'ko': {
        'YouTube Shorts Downloader': 'YouTube Shorts 다운로더',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'YouTube Shorts 동영상을 MP3 또는 MP4 형식으로 다운로드하세요. 빠르고 무료이며 사용하기 쉽습니다.',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, 유튜브 쇼츠 다운로드, 쇼츠를 mp3로',
    },
    'ru': {
        'YouTube Shorts Downloader': 'YouTube Shorts Загрузчик',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'Загружайте видео YouTube Shorts в формате MP3 или MP4. Быстро, бесплатно и просто в использовании.',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, скачать youtube shorts, shorts в mp3',
    },
    'th': {
        'YouTube Shorts Downloader': 'YouTube Shorts Downloader',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'ดาวน์โหลดวิดีโอ YouTube Shorts ในรูปแบบ MP3 หรือ MP4 รวดเร็ว ฟรี และใช้งานง่าย',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, ดาวน์โหลด youtube shorts, shorts เป็น mp3',
    },
    'tr': {
        'YouTube Shorts Downloader': 'YouTube Shorts İndirici',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'YouTube Shorts videolarını MP3 veya MP4 formatında indirin. Hızlı, ücretsiz ve kullanımı kolay.',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, youtube shorts indir, shorts mp3\'e',
    },
    'ur': {
        'YouTube Shorts Downloader': 'YouTube Shorts ڈاؤن لوڈر',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'YouTube Shorts ویڈیوز کو MP3 یا MP4 فارمیٹ میں ڈاؤن لوڈ کریں۔ تیز، مفت، اور استعمال میں آسان۔',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, یوٹیوب شارٹس ڈاؤن لوڈ, شارٹس کو mp3 میں',
    },
    'vi': {
        'YouTube Shorts Downloader': 'Trình tải xuống YouTube Shorts',
        'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'Tải xuống video YouTube Shorts ở định dạng MP3 hoặc MP4. Nhanh, miễn phí và dễ sử dụng.',
        'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, tải youtube shorts, shorts sang mp3',
    },
}

# Multi-downloader translations
multi_translations = {
    'id': {
        'YouTube Multi Downloader': 'YouTube Multi Downloader',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'Unduh beberapa video YouTube sekaligus. Tempel beberapa URL dan konversi semuanya sekaligus.',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, unduh banyak youtube, unduh massal',
    },
    'it': {
        'YouTube Multi Downloader': 'YouTube Multi Downloader',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'Scarica più video YouTube contemporaneamente. Incolla più URL e convertili tutti in una volta.',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, scarica multipli youtube, download in blocco',
    },
    'ja': {
        'YouTube Multi Downloader': 'YouTube マルチダウンローダー',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': '複数のYouTube動画を一度にダウンロード。複数のURLを貼り付けて、すべてを一度に変換します。',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, 複数youtubeダウンロード, 一括ダウンロード',
    },
    'ko': {
        'YouTube Multi Downloader': 'YouTube 멀티 다운로더',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': '여러 YouTube 동영상을 한 번에 다운로드하세요. 여러 URL을 붙여넣고 한 번에 모두 변환하세요.',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, 여러 유튜브 다운로드, 대량 다운로드',
    },
    'ru': {
        'YouTube Multi Downloader': 'YouTube Мульти Загрузчик',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'Загружайте несколько видео YouTube одновременно. Вставьте несколько URL и конвертируйте их все за один раз.',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, скачать несколько youtube, массовая загрузка',
    },
    'th': {
        'YouTube Multi Downloader': 'YouTube Multi Downloader',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'ดาวน์โหลดวิดีโอ YouTube หลายรายการพร้อมกัน วาง URL หลายรายการและแปลงทั้งหมดในคราวเดียว',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, ดาวน์โหลดหลาย youtube, ดาวน์โหลดจำนวนมาก',
    },
    'tr': {
        'YouTube Multi Downloader': 'YouTube Çoklu İndirici',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'Birden fazla YouTube videosunu aynı anda indirin. Birden fazla URL yapıştırın ve hepsini tek seferde dönüştürün.',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, çoklu youtube indir, toplu indirme',
    },
    'ur': {
        'YouTube Multi Downloader': 'YouTube ملٹی ڈاؤن لوڈر',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'ایک ساتھ متعدد YouTube ویڈیوز ڈاؤن لوڈ کریں۔ متعدد URLs پیسٹ کریں اور سب کو ایک ہی بار میں تبدیل کریں۔',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, متعدد یوٹیوب ڈاؤن لوڈ, بلک ڈاؤن لوڈ',
    },
    'vi': {
        'YouTube Multi Downloader': 'Trình tải xuống YouTube đa',
        'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'Tải xuống nhiều video YouTube cùng một lúc. Dán nhiều URL và chuyển đổi tất cả chỉ trong một lần.',
        'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, tải nhiều youtube, tải hàng loạt',
    },
}

def translate_file(file_path, translations):
    """Apply translations to a file"""
    content = Path(file_path).read_text(encoding='utf-8')
    
    for en, translated in translations.items():
        content = content.replace(en, translated)
    
    Path(file_path).write_text(content, encoding='utf-8')
    print(f"✓ {file_path}")

# Translate shorts pages
print("Translating Shorts pages...")
for lang in ['id', 'it', 'ja', 'ko', 'ru', 'th', 'tr', 'ur', 'vi']:
    file_path = f'web/{lang}/youtube-shorts-downloader/index.html'
    if Path(file_path).exists():
        translate_file(file_path, shorts_translations.get(lang, {}))

# Translate multi pages
print("\nTranslating Multi-downloader pages...")
for lang in ['id', 'it', 'ja', 'ko', 'ru', 'th', 'tr', 'ur', 'vi']:
    file_path = f'web/{lang}/youtube-multi-downloader/index.html'
    if Path(file_path).exists():
        translate_file(file_path, multi_translations.get(lang, {}))

print("\n✅ All shorts and multi pages translated!")
