import os
from pathlib import Path

# Configuration
BASE_DIR = Path("web")
TEMPLATE_FILE = BASE_DIR / "index.html"

# Master Dictionary for 100% Translation & Targeted SEO
LANGS = {
    "es": {
        "name": "Español",
        "title": "Convertidor de YouTube a MP3 - Rápido y Gratuito",
        "desc": "El mejor convertidor de YouTube a MP3. Descarga audio en 320kbps y videos MP4 gratis.",
        "keywords": "youtube a mp3, convertidor youtube, descargar musica youtube, ytmp3 español",
        "h2": "Convertidor de YouTube a MP3",
        "placeholder": "Pegue la URL de YouTube aquí...",
        "convert": "Convertir",
        "q1": "¿Cómo convertir?", "a1": "Copie el enlace, péguelo y haga clic en Convertir.",
        "q2": "¿Es seguro?", "a2": "Sí, 100% seguro y sin anuncios.",
        "q3": "¿Calidad?", "a3": "Soportamos hasta 320kbps y formatos WAV/FLAC.",
        "q4": "¿Móvil?", "a4": "Funciona perfectamente en iPhone y Android.",
    },
    "hi": {
        "name": "हिन्दी",
        "title": "यूट्यूब से एमपी3 कनवर्टर - फ्री और फास्ट",
        "desc": "यूट्यूब वीडियो को एमपी3 में बदलें। 320kbps हाई क्वालिटी ऑडियो मुफ्त डाउनलोड करें।",
        "keywords": "यूट्यूब से एमपी3, यूट्यूब कनवर्टर, यूट्यूब डाउनलोडर, ytmp3 हिंदी",
        "h2": "यूट्यूब से एमपी3 कनवर्टर",
        "placeholder": "यूट्यूब लिंक यहाँ पेस्ट करें...",
        "convert": "कन्वर्ट करें",
        "q1": "कैसे बदलें?", "a1": "लिंक कॉपी करें, पेस्ट करें और कन्वर्ट पर क्लिक करें।",
        "q2": "क्या यह सुरक्षित है?", "a2": "हाँ, यह 100% सुरक्षित और विज्ञापन-मुक्त है।",
        "q3": "क्वालिटी?", "a3": "हम 320kbps और WAV/FLAC का समर्थन करते हैं।",
        "q4": "मोबाइल?", "a4": "यह iPhone और Android पर बहुत अच्छा काम करता है।",
    },
    "de": {
        "name": "Deutsch",
        "title": "YouTube zu MP3 Konverter - Schnell & Kostenlos",
        "desc": "Der schnellste YouTube zu MP3 Konverter. Laden Sie 320kbps Audio kostenlos herunter.",
        "keywords": "youtube zu mp3, youtube konverter, ytmp3 deutsch",
        "h2": "YouTube zu MP3 Konverter",
        "placeholder": "YouTube URL hier einfügen...",
        "convert": "Konvertieren",
        "q1": "Wie konvertieren?", "a1": "Link kopieren, einfügen und auf Konvertieren klicken.",
        "q2": "Ist es sicher?", "a2": "Ja, 100% sicher und ohne Werbung.",
        "q3": "Qualität?", "a3": "Wir unterstützen 320kbps und WAV/FLAC.",
        "q4": "Mobil?", "a4": "Funktioniert auf iPhone und Android.",
    },
    "fr": {
        "name": "Français",
        "title": "Convertisseur YouTube en MP3 - Rapide & Gratuit",
        "desc": "Convertissez YouTube en MP3 gratuitement. Qualité 320kbps et téléchargement rapide.",
        "keywords": "youtube en mp3, convertisseur youtube, ytmp3 français",
        "h2": "Convertisseur YouTube en MP3",
        "placeholder": "Collez le lien YouTube ici...",
        "convert": "Convertir",
        "q1": "Comment convertir ?", "a1": "Copiez le lien, collez-le et cliquez sur Convertir.",
        "q2": "Est-ce sûr ?", "a2": "Oui, 100% sûr et sans pub.",
        "q3": "Qualité ?", "a3": "Supporte le 320kbps et WAV/FLAC.",
        "q4": "Mobile ?", "a4": "Compatible iPhone et Android.",
    },
    "pt": {
        "name": "Português",
        "title": "Conversor de YouTube para MP3 - Rápido e Grátis",
        "desc": "Converta vídeos do YouTube para MP3 em alta qualidade 320kbps gratuitamente.",
        "keywords": "youtube para mp3, conversor youtube, ytmp3 portugal",
        "h2": "Conversor de YouTube para MP3",
        "placeholder": "Cole o link do YouTube aqui...",
        "convert": "Converter",
        "q1": "Como converter?", "a1": "Copie o link, cole e clique em Converter.",
        "q2": "É seguro?", "a2": "Sim, 100% seguro e sem anúncios.",
        "q3": "Qualidade?", "a3": "Suporta 320kbps e WAV/FLAC.",
        "q4": "Telemóvel?", "a4": "Funciona no iPhone e Android.",
    },
    "ru": {
        "name": "Русский",
        "title": "YouTube в MP3 конвертер - Быстро и Бесплатно",
        "desc": "Конвертируйте YouTube в MP3 бесплатно. Высокое качество 320kbps.",
        "keywords": "youtube в mp3, ютуб конвертер, скачать музыку",
        "h2": "YouTube в MP3 конвертер",
        "placeholder": "Вставьте ссылку YouTube...",
        "convert": "Скачать",
        "q1": "Как скачать?", "a1": "Скопируйте ссылку, вставьте и нажмите Скачать.",
        "q2": "Это безопасно?", "a2": "Да, 100% безопасно и без рекламы.",
        "q3": "Качество?", "a3": "Поддерживаем 320kbps и WAV/FLAC.",
        "q4": "Телефон?", "a4": "Отлично работает на iPhone и Android.",
    },
    "ar": {
        "name": "العربية",
        "title": "محول يوتيوب إلى MP3 - سريع ومجاني",
        "desc": "أفضل محول يوتيوب إلى MP3. تحميل صوت عالي الجودة 320kbps.",
        "keywords": "يوتيوب إلى mp3, محول يوتيوب, تحميل من اليوتيوب",
        "h2": "محول يوتيوب إلى MP3",
        "placeholder": "الصق رابط يوتيوب هنا...",
        "convert": "تحويل",
        "q1": "كيفية التحويل؟", "a1": "انسخ الرابط، الصقه، واضغط تحويل.",
        "q2": "هل هو آمن؟", "a2": "نعم، آمن 100٪ وبدون إعلانات.",
        "q3": "الجودة؟", "a3": "ندعم 320kbps و WAV/FLAC.",
        "q4": "الجوال؟", "a4": "يعمل على الأيفون والأندرويد.",
    },
    "id": {
        "name": "Bahasa Indonesia",
        "title": "YouTube ke MP3 Converter - Cepat & Gratis",
        "desc": "Konversi YouTube ke MP3 dengan kualitas 320kbps secara gratis.",
        "keywords": "youtube ke mp3, download lagu youtube, ytmp3 indonesia",
        "h2": "YouTube ke MP3 Converter",
        "placeholder": "Tempel link YouTube di sini...",
        "convert": "Konversi",
        "q1": "Cara konversi?", "a1": "Salin link, tempel, dan klik Konversi.",
        "q2": "Aman?", "a2": "Ya, 100% aman dan tanpa iklan.",
        "q3": "Kualitas?", "a3": "Mendukung 320kbps dan WAV/FLAC.",
        "q4": "HP?", "a4": "Berjalan lancar di iPhone dan Android.",
    },
    "tr": {
        "name": "Türkçe",
        "title": "YouTube MP3 Dönüştürücü - Hızlı & Ücretsiz",
        "desc": "YouTube videolarını MP3'e dönüştürün. 320kbps yüksek kalite desteği.",
        "keywords": "youtube mp3 dönüştürücü, youtube indir, ytmp3 türkçe",
        "h2": "YouTube MP3 Dönüştürücü",
        "placeholder": "YouTube linkini buraya yapıştırın...",
        "convert": "Dönüştür",
        "q1": "Nasıl yapılır?", "a1": "Linki kopyalayın, yapıştırın ve Dönüştür'e basın.",
        "q2": "Güvenli mi?", "a2": "Evet, %100 güvenli ve reklamsız.",
        "q3": "Kalite?", "a3": "320kbps ve WAV/FLAC desteği var.",
        "q4": "Mobil?", "a4": "iPhone ve Android'de çalışır.",
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
        
        # FAQ Master Merge
        content = content.replace("How to convert YouTube to MP3?", data['q1'])
        content = content.replace("Simply copy the URL of the YouTube video, paste it into the search box above, select your desired format/quality, and click 'Convert'. Your file will be ready for download in seconds.", data['a1'])
        
        content = content.replace("Is yt2mp3.lol free and safe?", data['q2'])
        content = content.replace("Yes! YT2MP3 is 100% free and safe. We don't have annoying pop-up ads, we don't require registration, and we don't store your data. It's a clean, high-performance YouTube downloader.", data['a2'])
        
        content = content.replace("What is the highest MP3 quality available?", data['q3'])
        content = content.replace("We support true 320kbps MP3 exports. You can also choose lossless formats like WAV and FLAC for professional-grade audio quality.", data['a3'])
        
        content = content.replace("Can I use this on Android or iPhone?", data['q4'])
        content = content.replace("Absolutely. Our site is mobile-first and works perfectly in any browser on Android, iOS (iPhone/iPad), and Tablets without installing any apps.", data['a4'])

        # Language Menu Logic
        content = content.replace('class="l-label">English', f'class="l-label">{data["name"]}')
        content = content.replace('href="/" class="lang-active">English', 'href="/">English')
        content = content.replace(f'href="/{code}/">', f'href="/{code}/" class="lang-active">')

        with open(lang_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {code} version.")

if __name__ == "__main__":
    generate()
