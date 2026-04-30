import os
from pathlib import Path

# Configuration
BASE_DIR = Path("web")
TEMPLATE_FILE = BASE_DIR / "index.html"

# FULL 17-LANGUAGE MASTER DICTIONARY
LANGS = {
    "es": {"name": "Español", "title": "YouTube a MP3", "desc": "Descarga YouTube a MP3 gratis.", "keywords": "youtube a mp3, ytmp3", "h2": "YouTube a MP3", "placeholder": "Enlace aquí...", "convert": "Convertir", "q1": "¿Cómo?", "a1": "Copia el link y pega.", "q2": "¿Seguro?", "a2": "Sí, seguro.", "q3": "Calidad", "a3": "320kbps.", "q4": "Móvil", "a4": "Sí."},
    "hi": {"name": "हिन्दी", "title": "यूट्यूब से एमपी3", "desc": "यूट्यूब वीडियो एमपी3 डाउनलोड।", "keywords": "यूट्यूब से एमपी3, ytmp3", "h2": "यूट्यूब से एमपी3", "placeholder": "लिंक यहाँ डालें...", "convert": "कन्वर्ट", "q1": "कैसे?", "a1": "लिंक पेस्ट करें।", "q2": "सुरक्षित?", "a2": "हाँ।", "q3": "क्वालिटी", "a3": "320kbps.", "q4": "मोबाइल", "a4": "हाँ।"},
    "de": {"name": "Deutsch", "title": "YouTube zu MP3", "desc": "YouTube zu MP3 Konverter.", "keywords": "youtube zu mp3, ytmp3", "h2": "YouTube zu MP3", "placeholder": "Link hierher...", "convert": "Konvertieren", "q1": "Wie?", "a1": "Link einfügen.", "q2": "Sicher?", "a2": "Ja.", "q3": "Qualität", "a3": "320kbps.", "q4": "Mobil", "a4": "Ja."},
    "fr": {"name": "Français", "title": "YouTube en MP3", "desc": "Convertisseur YouTube MP3.", "keywords": "youtube en mp3, ytmp3", "h2": "YouTube en MP3", "placeholder": "Lien ici...", "convert": "Convertir", "q1": "Comment?", "a1": "Collez le lien.", "q2": "Sûr?", "a2": "Oui.", "q3": "Qualité", "a3": "320kbps.", "q4": "Mobile", "a4": "Oui."},
    "pt": {"name": "Português", "title": "YouTube para MP3", "desc": "Conversor YouTube MP3.", "keywords": "youtube para mp3, ytmp3", "h2": "YouTube para MP3", "placeholder": "Link aqui...", "convert": "Converter", "q1": "Como?", "a1": "Cole o link.", "q2": "Seguro?", "a2": "Sim.", "q3": "Qualidade", "a3": "320kbps.", "q4": "Telemóvel", "a4": "Sim."},
    "ru": {"name": "Русский", "title": "YouTube в MP3", "desc": "Ютуб в МП3 конвертер.", "keywords": "youtube в mp3, ютуб скачать", "h2": "YouTube в MP3", "placeholder": "Ссылка здесь...", "convert": "Скачать", "q1": "Как?", "a1": "Вставьте ссылку.", "q2": "Безопасно?", "a2": "Да.", "q3": "Качество", "a3": "320kbps.", "q4": "Телефон", "a4": "Да."},
    "ar": {"name": "العربية", "title": "يوتيوب إلى MP3", "desc": "محول يوتيوب MP3.", "keywords": "يوتيوب إلى mp3, تحميل يوتيوب", "h2": "يوتيوب إلى MP3", "placeholder": "الرابط هنا...", "convert": "تحويل", "q1": "كيف؟", "a1": "الصق الرابط.", "q2": "آمن؟", "a2": "نعم.", "q3": "الجودة", "a3": "320kbps.", "q4": "جوال", "a4": "نعم."},
    "id": {"name": "Indonesia", "title": "YouTube ke MP3", "desc": "Download YouTube ke MP3.", "keywords": "youtube ke mp3, download lagu", "h2": "YouTube ke MP3", "placeholder": "Tempel link...", "convert": "Konversi", "q1": "Cara?", "a1": "Tempel link.", "q2": "Aman?", "a2": "Ya.", "q3": "Kualitas", "a3": "320kbps.", "q4": "HP", "a4": "Ya."},
    "tr": {"name": "Türkçe", "title": "YouTube MP3 İndir", "desc": "YouTube MP3 dönüştürücü.", "keywords": "youtube mp3, ytmp3", "h2": "YouTube MP3", "placeholder": "Linki yapıştır...", "convert": "Dönüştür", "q1": "Nasıl?", "a1": "Linki yapıştırın.", "q2": "Güvenli?", "a2": "Evet.", "q3": "Kalite", "a3": "320kbps.", "q4": "Mobil", "a4": "Evet."},
    "bn": {"name": "বাংলা", "title": "ইউটিউব থেকে এমপি৩", "desc": "ইউটিউব এমপি৩ কনভার্টার।", "keywords": "ইউটিউব এমপি৩, ytmp3", "h2": "ইউটিউব এমপি৩", "placeholder": "লিঙ্ক এখানে দিন...", "convert": "কনভার্ট", "q1": "কিভাবে?", "a1": "লিঙ্ক পেস্ট করুন।", "q2": "নিরাপদ?", "a2": "হ্যাঁ।", "q3": "কোয়ালিটি", "a3": "320kbps.", "q4": "মোবাইল", "a4": "হ্যাঁ।"},
    "it": {"name": "Italiano", "title": "YouTube in MP3", "desc": "Convertitore YouTube MP3.", "keywords": "youtube in mp3, ytmp3", "h2": "YouTube in MP3", "placeholder": "Link qui...", "convert": "Converti", "q1": "Come?", "a1": "Incolla il link.", "q2": "Sicuro?", "a2": "Sì.", "q3": "Qualità", "a3": "320kbps.", "q4": "Mobile", "a4": "Sì."},
    "ja": {"name": "日本語", "title": "YouTube MP3 変換", "desc": "YouTubeをMP3に変換。", "keywords": "youtube 変換, youtube ダウンロード", "h2": "YouTube MP3 変換", "placeholder": "ここにリンクを...", "convert": "変換", "q1": "方法は？", "a1": "リンクを貼るだけ。", "q2": "安全？", "a2": "はい。", "q3": "音質", "a3": "320kbps対応。", "q4": "スマホ", "a4": "はい。"},
    "ko": {"name": "한국어", "title": "유튜브 MP3 변환기", "desc": "유튜브 MP3 다운로드.", "keywords": "유튜브 변환기, 유튜브 다운로드", "h2": "유튜브 MP3 변환기", "placeholder": "링크를 입력하세요...", "convert": "변환", "q1": "방법은?", "a1": "링크를 붙여넣으세요.", "q2": "안전한가요?", "a2": "네.", "q3": "음질", "a3": "320kbps 지원.", "q4": "모바일", "a4": "네."},
    "th": {"name": "ไทย", "title": "โหลด YouTube เป็น MP3", "desc": "แปลง YouTube เป็น MP3 ฟรี.", "keywords": "โหลด youtube, แปลงไฟล์ youtube", "h2": "YouTube เป็น MP3", "placeholder": "วางลิงก์ที่นี่...", "convert": "แปลงไฟล์", "q1": "ทำอย่างไร?", "a1": "วางลิงก์แล้วกดแปลง।", "q2": "ปลอดภัยไหม?", "a2": "ใช่।", "q3": "คุณภาพ", "a3": "320kbps.", "q4": "มือถือ", "a4": "ใช่।"},
    "ur": {"name": "اردو", "title": "یوٹیوب سے MP3", "desc": "یوٹیوب ویڈیو ڈاؤن لوڈر۔", "keywords": "یوٹیوب ڈاؤن لوڈر, ytmp3", "h2": "یوٹیوب سے MP3", "placeholder": "لنک یہاں ڈالیں...", "convert": "تبدیل کریں", "q1": "کیسے؟", "a1": "لنک پیسٹ کریں۔", "q2": "محفوظ ہے؟", "a2": "جی ہاں۔", "q3": "کوالٹی", "a3": "320kbps.", "q4": "موبائل", "a4": "جی ہاں۔"},
    "vi": {"name": "Tiếng Việt", "title": "Tải YouTube MP3", "desc": "Chuyển YouTube sang MP3.", "keywords": "tải youtube, ytmp Vietnamese", "h2": "YouTube sang MP3", "placeholder": "Dán link vào đây...", "convert": "Chuyển đổi", "q1": "Cách làm?", "a1": "Dán link và nhấn nút।", "q2": "An toàn?", "a2": "Có।", "q3": "Chất lượng", "a3": "320kbps.", "q4": "Điện thoại", "a4": "Có।"},
    "fil": {"name": "Filipino", "title": "YouTube sa MP3", "desc": "Convert YouTube to MP3 free.", "keywords": "youtube downloader, ytmp3 tagalog", "h2": "YouTube sa MP3", "placeholder": "I-paste ang link...", "convert": "I-convert", "q1": "Paano?", "a1": "I-paste ang link.", "q2": "Ligtas ba?", "a2": "Oo.", "q3": "Quality", "a3": "320kbps.", "q4": "Mobile", "a4": "Oo."}
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
        content = content.replace("<title>YT to MP3 - YouTube MP3 Converter & Downloader (Fast & Free)</title>", f"<title>{data['title']} - yt2mp3.lol</title>")
        content = content.replace('content="The fastest YT to MP3 converter. Download high-quality audio (320kbps) and videos from YouTube with our free YouTube MP3 Downloader. Safe, ad-free, and reliable."', f'content="{data["desc"]}"')
        content = content.replace('content="yt to mp3, youtube to mp3, youtube mp3, youtube converter, youtube downloader, yt mp3 converter, 320kbps mp3, wav converter, flac converter, youtube to mp4, ytmp3"', f'content="{data["keywords"]}"')

        # UI
        content = content.replace("YT2MP3 - YouTube to MP3", f"YT2MP3 - {data['h2']}")
        content = content.replace('placeholder="Paste YouTube URL or search keywords"', f'placeholder="{data["placeholder"]}"')
        content = content.replace(">Convert</button>", f">{data['convert']}</button>")
        
        # FAQ Master Merge (Simplified for space)
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
        print(f"Generated {code} version.")

if __name__ == "__main__":
    generate()
