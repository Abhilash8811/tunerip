import os
from pathlib import Path

# Configuration
BASE_DIR = Path("web")
TEMPLATE_FILE = BASE_DIR / "index.html"

# GOD-LEVEL SEO CONTENT (MASTER REPOSITORY)
LANGS = {
    "es": {
        "name": "Español",
        "title": "Convertidor de YouTube a MP3 - Descargar Música Gratis 320kbps",
        "desc": "El mejor convertidor de YouTube a MP3 en español. Descarga música de alta calidad (320kbps) y videos MP4 de forma segura.",
        "keywords": "descargar musica de youtube, youtube a mp3, convertidor youtube, ytmp3 gratis",
        "h2": "Convertidor de YouTube a MP3 Líder",
        "placeholder": "Pega el enlace de YouTube...",
        "convert": "Convertir Gratis",
        "q1": "¿Cómo descargar música de YouTube?", "a1": "Copia el link, pégalo arriba y presiona Convertir para obtener un MP3 de 320kbps en segundos.",
        "q2": "¿Es seguro?", "a2": "Sí, es 100% seguro, sin virus y sin anuncios molestos.",
        "q3": "¿Puedo bajar playlists?", "a3": "Sí, pega el link de la lista y descarga todos los temas individualmente.",
        "q4": "¿Funciona en móviles?", "a4": "Perfectamente en iPhone y Android sin instalar ninguna app.",
    },
    "hi": {
        "name": "हिन्दी",
        "title": "यूट्यूब से एमपी3 कनवर्टर - फ्री गाना डाउनलोड करें (320kbps)",
        "desc": "सबसे तेज़ यूट्यूब से एमपी3 कनवर्टर। यूट्यूब वीडियो को हाई क्वालिटी (320kbps) ऑडियो में बदलें।",
        "keywords": "यूट्यूब से एमपी3, यूट्यूब गाना डाउनलोडर, ytmp3 हिंदी",
        "h2": "भारत का नंबर 1 यूट्यूब से एमपी3 कनवर्टर",
        "placeholder": "यूट्यूब लिंक यहाँ डालें...",
        "convert": "मुफ्त डाउनलोड",
        "q1": "यूट्यूब वीडियो को गाने में कैसे बदलें?", "a1": "वीडियो लिंक पेस्ट करें और कन्वर्ट बटन दबाएं। गाना तुरंत 320kbps क्वालिटी में डाउनलोड हो जाएगा।",
        "q2": "क्या यह सुरक्षित है?", "a2": "हाँ, यह 100% सुरक्षित और विज्ञापन-मुक्त है।",
        "q3": "प्लेलिस्ट डाउनलोड?", "a3": "हाँ, पूरी प्लेलिस्ट का लिंक डालें और हर गाना अलग से डाउनलोड करें।",
        "q4": "मोबाइल पर काम?", "a4": "हाँ, यह हर स्मार्टफोन और ब्राउज़र पर मक्खन की तरह चलता है।",
    },
    "de": {
        "name": "Deutsch",
        "title": "YouTube zu MP3 Konverter - Gratis Musik Download (320kbps)",
        "desc": "Der schnellste YouTube zu MP3 Konverter für Deutschland. Sicher und ohne Werbung Musik laden.",
        "keywords": "youtube zu mp3, youtube konverter, ytmp3 deutschland",
        "h2": "Deutschlands Nr. 1 YouTube zu MP3 Konverter",
        "placeholder": "Link hier einfügen...",
        "convert": "Gratis Download",
        "q1": "Wie konvertiere ich Videos?", "a1": "Link kopieren, einfügen und auf 'Konvertieren' klicken. Fertig!",
        "q2": "Ist es sicher?", "a2": "Ja, absolut sicher, anonym und ohne nervige Pop-ups.",
        "q3": "Ganze Playlists?", "a3": "Ja, Batch-Downloads werden voll unterstützt.",
        "q4": "Smartphone?", "a4": "Ja, läuft perfekt auf iPhone und Android.",
    },
    "fr": {
        "name": "Français",
        "title": "Convertisseur YouTube en MP3 - Télécharger Musique Haute Qualité",
        "desc": "Le convertisseur YouTube en MP3 le plus rapide. Téléchargez de la musique gratuitement et sans pub.",
        "keywords": "youtube en mp3, convertisseur youtube, ytmp3 france",
        "h2": "Le Meilleur Convertisseur YouTube en MP3",
        "placeholder": "Collez le lien YouTube ici...",
        "convert": "Télécharger",
        "q1": "Comment convertir ?", "a1": "Copiez l'URL, collez-la et cliquez sur 'Convertir' pour obtenir votre MP3.",
        "q2": "Gratuit et sûr ?", "a2": "Oui, 100% gratuit, sans limites et sans publicités intrusives.",
        "q3": "Playlists ?", "a3": "Oui, collez le lien de la playlist pour tout télécharger d'un coup.",
        "q4": "Mobile ?", "a4": "Entièrement optimisé pour Android et iPhone.",
    },
    "ru": {
        "name": "Русский",
        "title": "YouTube в MP3 конвертер - Скачать музыку бесплатно 320kbps",
        "desc": "Самый быстрый конвертер YouTube в MP3 на русском языке. Безопасно и без рекламы.",
        "keywords": "youtube в mp3, ютуб конвертер, ytmp3 русский",
        "h2": "Лучший YouTube в MP3 конвертер на русском",
        "placeholder": "Вставьте ссылку на YouTube...",
        "convert": "Скачать бесплатно",
        "q1": "Как конвертировать?", "a1": "Вставьте ссылку и нажмите 'Скачать'. MP3 320kbps будет готов через секунды.",
        "q2": "Безопасно?", "a2": "Да, полная анонимность и отсутствие вирусов.",
        "q3": "Плейлисты?", "a3": "Да, можно скачивать целые альбомы одним кликом.",
        "q4": "На телефоне?", "a4": "Работает на любом смартфоне без установки приложений.",
    }
}

def generate():
    if not TEMPLATE_FILE.exists(): return
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    for code, data in LANGS.items():
        lang_dir = BASE_DIR / code
        lang_dir.mkdir(parents=True, exist_ok=True)
        
        content = template
        content = content.replace('lang="en"', f'lang="{code}"')
        
        # SEO
        content = content.replace("<title>YT to MP3 - YouTube MP3 Converter & Downloader (Fast & Free)</title>", f"<title>{data['title']}</title>")
        content = content.replace('content="The fastest YT to MP3 converter. Download high-quality audio (320kbps) and videos from YouTube with our free YouTube MP3 Downloader. Safe, ad-free, and reliable."', f'content="{data["desc"]}"')
        content = content.replace('content="yt to mp3, youtube to mp3, youtube mp3, youtube converter, youtube downloader, yt mp3 converter, 320kbps mp3, wav converter, flac converter, youtube to mp4, ytmp3"', f'content="{data["keywords"]}"')

        # UI
        content = content.replace("YT2MP3 - YouTube to MP3", f"YT2MP3 - {data['h2']}")
        content = content.replace('placeholder="Paste YouTube URL or search keywords"', f'placeholder="{data["placeholder"]}"')
        content = content.replace(">Convert</button>", f">{data['convert']}</button>")
        
        # FAQ
        content = content.replace("How to convert YouTube to MP3?", data['q1'])
        content = content.replace("Simply copy the URL of the YouTube video, paste it into the search box above, select your desired format/quality, and click 'Convert'. Your file will be ready for download in seconds.", data['a1'])
        content = content.replace("Is yt2mp3.lol free and safe?", data['q2'])
        content = content.replace("Yes! YT2MP3 is 100% free and safe. We don't have annoying pop-up ads, we don't require registration, and we don't store your data. It's a clean, high-performance YouTube downloader.", data['a2'])
        content = content.replace("What is the highest MP3 quality available?", data['q3'])
        content = content.replace("We support true 320kbps MP3 exports. You can also choose lossless formats like WAV and FLAC for professional-grade audio quality.", data['a3'])
        content = content.replace("Can I use this on Android or iPhone?", data['q4'])
        content = content.replace("Absolutely. Our site is mobile-first and works perfectly in any browser on Android, iOS (iPhone/iPad), and Tablets without installing any apps.", data['a4'])

        # Menu
        content = content.replace('class="l-label">English', f'class="l-label">{data["name"]}')
        content = content.replace('href="/" class="lang-active">English', 'href="/">English')
        content = content.replace(f'href="/{code}/">', f'href="/{code}/" class="lang-active">')

        with open(lang_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {code} with God-Level SEO.")

if __name__ == "__main__":
    generate()
