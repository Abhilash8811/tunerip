import os
from pathlib import Path

# Configuration
BASE_DIR = Path("web")
TEMPLATE_FILE = BASE_DIR / "index.html"

LANGS = {
    "ar": {"name": "العربية", "title": "يوتيوب إلى MP3", "desc": "تحويل يوتيوب إلى MP3 مجانًا"},
    "bn": {"name": "বাংলা", "title": "ইউটিউব থেকে এমপি৩", "desc": "ইউটিউব থেকে এমপি৩ রূপান্তর করুন"},
    "de": {"name": "Deutsch", "title": "YouTube zu MP3", "desc": "Kostenloser YouTube zu MP3 Konverter"},
    "es": {"name": "Español", "title": "YouTube a MP3", "desc": "Convertidor gratuito de YouTube a MP3"},
    "fil": {"name": "Filipino", "title": "YouTube sa MP3", "desc": "Libreng YouTube sa MP3 converter"},
    "fr": {"name": "Français", "title": "YouTube en MP3", "desc": "Convertisseur YouTube en MP3 gratuit"},
    "hi": {"name": "हिन्दी", "title": "यूट्यूब से एमपी3", "desc": "मुफ्त यूट्यूब से एमपी3 कनवर्टर"},
    "id": {"name": "Bahasa Indonesia", "title": "YouTube ke MP3", "desc": "Konverter YouTube ke MP3 gratis"},
    "it": {"name": "Italiano", "title": "YouTube in MP3", "desc": "Convertitore YouTube in MP3 gratuito"},
    "ja": {"name": "日本語", "title": "YouTube MP3 変換", "desc": "無料のYouTube MP3変換ツール"},
    "ko": {"name": "한국어", "title": "유튜브 MP3 변환", "desc": "무료 유튜브 MP3 변환기"},
    "pt": {"name": "Português", "title": "YouTube para MP3", "desc": "Conversor gratuito de YouTube para MP3"},
    "ru": {"name": "Русский", "title": "YouTube в MP3", "desc": "Бесплатный конвертер YouTube في MP3"},
    "th": {"name": "ภาษาไทย", "title": "ยูทูบเป็น MP3", "desc": "เครื่องมือแปลงยูทูบเป็น MP3 ฟรี"},
    "tr": {"name": "Türkçe", "title": "YouTube'dan MP3'e", "desc": "Ücretsiz YouTube'dan MP3'e dönüştürücü"},
    "ur": {"name": "اردو", "title": "یوٹیوب سے MP3", "desc": "مفت یوٹیوب سے MP3 کنورٹر"},
    "vi": {"name": "Tiếng Việt", "title": "YouTube sang MP3", "desc": "Trình chuyển đổi YouTube sang MP3 miễn phí"},
}

def generate():
    if not TEMPLATE_FILE.exists():
        print("Template index.html not found!")
        return

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    for code, data in LANGS.items():
        lang_dir = BASE_DIR / code
        lang_dir.mkdir(parents=True, exist_ok=True)
        
        # Simple translation of main elements
        content = template
        content = content.replace('lang="en"', f'lang="{code}"')
        content = content.replace("YT2MP3 - YouTube to MP3", f"YT2MP3 - {data['title']}")
        content = content.replace("YouTube to MP3 Converter", f"{data['title']} Converter")
        content = content.replace('class="l-label">English', f'class="l-label">{data["name"]}')
        
        # Update active state in menu
        content = content.replace('href="/" class="lang-active">English', 'href="/">English')
        content = content.replace(f'href="/{code}/">', f'href="/{code}/" class="lang-active">')

        output_file = lang_dir / "index.html"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {code} version.")

if __name__ == "__main__":
    generate()
