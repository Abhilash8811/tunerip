#!/usr/bin/env python3
"""
Translate remaining playlist pages
"""

import re
from pathlib import Path

# Translation dictionaries for each language
translations = {
    'id': {  # Indonesian
        'Home': 'Beranda',
        'YouTube Playlist Downloader': 'YouTube Playlist Downloader',
        'Convert an entire YouTube playlist to MP3 or MP4 in one click. Each video downloads as its own file.': 'Konversi seluruh playlist YouTube ke MP3 atau MP4 dalam satu klik. Setiap video diunduh sebagai file terpisah.',
        'YT2MP3 - YouTube to MP3': 'YT2MP3 - YouTube ke MP3',
        'Paste YouTube URL or search keywords': 'Tempel URL YouTube atau cari kata kunci',
        'Paste a YouTube link': 'Tempel link YouTube',
        'Paste from clipboard': 'Tempel dari clipboard',
        'Paste': 'Tempel',
        'Output format': 'Format output',
        'Quality': 'Kualitas',
        'Audio track': 'Trek audio',
        'Origin': 'Asli',
        'Search languages...': 'Cari bahasa...',
        'Origin (default)': 'Asli (default)',
        'Convert': 'Konversi',
        'Bulk-convert every video in a playlist': 'Konversi massal setiap video dalam playlist',
        'Supports mixes and topic playlists': 'Mendukung mix dan playlist topik',
        'Picking the right format': 'Memilih format yang tepat',
        'Format Comparison Table': 'Tabel Perbandingan Format',
        'Format': 'Format',
        'Best For': 'Terbaik Untuk',
        'Quality Options': 'Opsi Kualitas',
        'File Size': 'Ukuran File',
        'Universal audio playback': 'Pemutaran audio universal',
        'Small': 'Kecil',
        'Video playback everywhere': 'Pemutaran video di mana saja',
        'Large': 'Besar',
        'Lossless audio editing': 'Pengeditan audio lossless',
        'Very Large': 'Sangat Besar',
        'Apple devices': 'Perangkat Apple',
        'Medium': 'Sedang',
        'Batch Conversion Masterclass': 'Kelas Master Konversi Batch',
        'Preserve Original Order and Titles': 'Pertahankan Urutan dan Judul Asli',
        'Flexible Format Selection for Playlists': 'Pemilihan Format Fleksibel untuk Playlist',
        'High-Concurrency Processing': 'Pemrosesan Konkurensi Tinggi',
        'Support for Massive Playlists': 'Dukungan untuk Playlist Besar',
        'Download Auto-Generated Mixes': 'Unduh Mix yang Dibuat Otomatis',
        'Ideal for Educators and Students': 'Ideal untuk Pendidik dan Siswa',
        'Handling Unavailable or Private Videos': 'Menangani Video yang Tidak Tersedia atau Pribadi',
        'How to Download a Full Playlist': 'Cara Mengunduh Playlist Lengkap',
        'FAQ': 'FAQ',
        'youtube playlist downloader, playlist to mp3, youtube playlist to mp4, batch youtube converter': 'youtube playlist downloader, playlist to mp3, youtube playlist to mp4, batch youtube converter, unduh playlist youtube, playlist ke mp3',
    },
    'it': {  # Italian
        'Home': 'Home',
        'YouTube Playlist Downloader': 'YouTube Playlist Downloader',
        'Convert an entire YouTube playlist to MP3 or MP4 in one click. Each video downloads as its own file.': 'Converti un\'intera playlist di YouTube in MP3 o MP4 con un clic. Ogni video viene scaricato come file separato.',
        'YT2MP3 - YouTube to MP3': 'YT2MP3 - YouTube a MP3',
        'Paste YouTube URL or search keywords': 'Incolla URL YouTube o cerca parole chiave',
        'Paste a YouTube link': 'Incolla un link YouTube',
        'Paste from clipboard': 'Incolla dagli appunti',
        'Paste': 'Incolla',
        'Output format': 'Formato di output',
        'Quality': 'Qualità',
        'Audio track': 'Traccia audio',
        'Origin': 'Originale',
        'Search languages...': 'Cerca lingue...',
        'Origin (default)': 'Originale (predefinito)',
        'Convert': 'Converti',
        'Bulk-convert every video in a playlist': 'Converti in massa ogni video in una playlist',
        'Supports mixes and topic playlists': 'Supporta mix e playlist tematiche',
        'Picking the right format': 'Scegliere il formato giusto',
        'Format Comparison Table': 'Tabella di Confronto Formati',
        'Format': 'Formato',
        'Best For': 'Migliore Per',
        'Quality Options': 'Opzioni di Qualità',
        'File Size': 'Dimensione File',
        'Universal audio playback': 'Riproduzione audio universale',
        'Small': 'Piccolo',
        'Video playback everywhere': 'Riproduzione video ovunque',
        'Large': 'Grande',
        'Lossless audio editing': 'Editing audio lossless',
        'Very Large': 'Molto Grande',
        'Apple devices': 'Dispositivi Apple',
        'Medium': 'Medio',
        'Batch Conversion Masterclass': 'Masterclass di Conversione Batch',
        'Preserve Original Order and Titles': 'Preserva Ordine e Titoli Originali',
        'Flexible Format Selection for Playlists': 'Selezione Formato Flessibile per Playlist',
        'High-Concurrency Processing': 'Elaborazione ad Alta Concorrenza',
        'Support for Massive Playlists': 'Supporto per Playlist Massive',
        'Download Auto-Generated Mixes': 'Scarica Mix Generati Automaticamente',
        'Ideal for Educators and Students': 'Ideale per Educatori e Studenti',
        'Handling Unavailable or Private Videos': 'Gestione Video Non Disponibili o Privati',
        'How to Download a Full Playlist': 'Come Scaricare una Playlist Completa',
        'FAQ': 'FAQ',
        'youtube playlist downloader, playlist to mp3, youtube playlist to mp4, batch youtube converter': 'youtube playlist downloader, playlist to mp3, youtube playlist to mp4, batch youtube converter, scarica playlist youtube, playlist a mp3',
    },
}

def translate_file(lang_code, file_path):
    """Translate a single file"""
    trans = translations.get(lang_code, {})
    if not trans:
        print(f"No translations for {lang_code}")
        return
    
    content = Path(file_path).read_text(encoding='utf-8')
    
    # Apply translations
    for en, translated in trans.items():
        content = content.replace(en, translated)
    
    # Write back
    Path(file_path).write_text(content, encoding='utf-8')
    print(f"✓ Translated {file_path}")

# Translate Indonesian
translate_file('id', 'web/id/youtube-playlist-downloader/index.html')

# Translate Italian  
translate_file('it', 'web/it/youtube-playlist-downloader/index.html')

print("\nDone!")
