import os
from pathlib import Path

# Configuration
BASE_DIR = Path("web")
TEMPLATE_FILE = BASE_DIR / "index.html"

# Master Dictionary for 100% Translation
LANGS = {
    "es": {
        "name": "Español",
        "title": "Convertidor de YouTube a MP3 - Rápido y Gratuito",
        "desc": "El convertidor de YouTube a MP3 más rápido. Descarga audio de alta calidad (320kbps) y videos de YouTube gratis.",
        "keywords": "youtube a mp3, convertidor youtube, descargar musica youtube, ytmp3 español",
        "h2": "Convertidor de YouTube a MP3",
        "placeholder": "Pegue la URL de YouTube o busque palabras clave",
        "convert": "Convertir",
        "hero_p": "La forma más rápida de guardar audio y video de YouTube de forma segura.",
        "faq_h2": "Preguntas Frecuentes",
        "q1": "¿Cómo convertir YouTube a MP3?",
        "a1": "Copie el enlace de YouTube, péguelo arriba y haga clic en Convertir.",
        "q2": "¿Es seguro?",
        "a2": "Sí, es 100% seguro y sin anuncios molestos.",
    },
    "hi": {
        "name": "हिन्दी",
        "title": "यूट्यूब से एमपी3 कनवर्टर - फ्री और फास्ट",
        "desc": "यूट्यूब से एमपी3 में बदलने का सबसे तेज़ तरीका। 320kbps हाई क्वालिटी ऑडियो मुफ्त में डाउनलोड करें।",
        "keywords": "यूट्यूब से एमपी3, यूट्यूब कनवर्टर, यूट्यूब डाउनलोडर, ytmp3 हिंदी",
        "h2": "यूट्यूब से एमपी3 कनवर्टर",
        "placeholder": "यूट्यूब URL पेस्ट करें या कीवर्ड खोजें",
        "convert": "कन्वर्ट करें",
        "hero_p": "यूट्यूब ऑडियो और वीडियो को सुरक्षित रूप से सहेजने का सबसे तेज़ तरीका।",
        "faq_h2": "अक्सर पूछे जाने वाले प्रश्न",
        "q1": "यूट्यूब को एमपी3 में कैसे बदलें?",
        "a1": "यूट्यूब लिंक कॉपी करें, ऊपर पेस्ट करें और कन्वर्ट पर क्लिक करें।",
        "q2": "क्या यह सुरक्षित है?",
        "a2": "हाँ, यह 100% सुरक्षित है और इसमें कोई विज्ञापन नहीं है।",
    },
    "de": {
        "name": "Deutsch",
        "title": "YouTube zu MP3 Konverter - Schnell & Kostenlos",
        "desc": "Der schnellste YouTube zu MP3 Konverter. Laden Sie hochwertige Audio- (320kbps) und Videodateien kostenlos herunter.",
        "keywords": "youtube zu mp3, youtube konverter, youtube downloader, ytmp3 deutsch",
        "h2": "YouTube zu MP3 Konverter",
        "placeholder": "YouTube URL einfügen oder Suchbegriffe eingeben",
        "convert": "Konvertieren",
        "hero_p": "Der schnellste Weg, YouTube-Audio und -Video sicher zu speichern.",
        "faq_h2": "Häufig gestellte Fragen (FAQ)",
        "q1": "Wie konvertiere ich YouTube in MP3?",
        "a1": "Kopieren Sie den YouTube-Link, fügen Sie ihn oben ein und klicken Sie auf Konvertieren.",
        "q2": "Ist es sicher?",
        "a2": "Ja, es ist 100% sicher und ohne nervige Werbung.",
    },
    "fr": {
        "name": "Français",
        "title": "Convertisseur YouTube en MP3 - Rapide & Gratuit",
        "desc": "Le convertisseur YouTube en MP3 le plus rapide. Téléchargez gratuitement de l'audio haute qualité (320kbps) et des vidéos.",
        "keywords": "youtube en mp3, convertisseur youtube, telecharger musique youtube, ytmp3 français",
        "h2": "Convertisseur YouTube en MP3",
        "placeholder": "Collez l'URL YouTube ou recherchez des mots-clés",
        "convert": "Convertir",
        "hero_p": "Le moyen le plus rapide d'enregistrer l'audio et la vidéo YouTube en toute sécurité.",
        "faq_h2": "Questions Fréquentes",
        "q1": "Comment convertir YouTube en MP3 ?",
        "a1": "Copiez le lien YouTube, collez-le ci-dessus et cliquez sur Convertir.",
        "q2": "Est-ce sûr ?",
        "a2": "Oui, c'est 100% sûr et sans publicités intrusives.",
    },
    "ar": {
        "name": "العربية",
        "title": "يوتيوب إلى MP3 - محول سريع ومجاني",
        "desc": "أسرع محول يوتيوب إلى MP3. قم بتنزيل مقاطع فيديو وصوت عالية الجودة (320kbps) مجانًا.",
        "keywords": "يوتيوب إلى mp3, محول يوتيوب, تحميل موسيقى من يوتيوب",
        "h2": "محول يوتيوب إلى MP3",
        "placeholder": "انسخ رابط يوتيوب أو ابحث عن كلمات رئيسية",
        "convert": "تحويل",
        "hero_p": "أسرع طريقة لحفظ صوت وفيديو يوتيوب بأمان.",
        "faq_h2": "الأسئلة الشائعة",
        "q1": "كيفية تحويل يوتيوب إلى MP3؟",
        "a1": "انسخ رابط يوتيوب، ثم الصقه أعلاه وانقر على تحويل.",
        "q2": "هل الموقع آمن؟",
        "a2": "نعم، الموقع آمن 100% ولا يحتوي على إعلانات مزعجة.",
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
        
        # SEO & Head
        content = content.replace("<title>YT to MP3 - YouTube MP3 Converter & Downloader (Fast & Free)</title>", f"<title>{data['title']}</title>")
        content = content.replace('content="The fastest YT to MP3 converter. Download high-quality audio (320kbps) and videos from YouTube with our free YouTube MP3 Downloader. Safe, ad-free, and reliable."', f'content="{data["desc"]}"')
        content = content.replace('content="yt to mp3, youtube to mp3, youtube mp3, youtube converter, youtube downloader, yt mp3 converter, 320kbps mp3, wav converter, flac converter, youtube to mp4, ytmp3"', f'content="{data["keywords"]}"')

        # UI Strings
        content = content.replace("YT2MP3 - YouTube to MP3", f"YT2MP3 - {data['h2']}")
        content = content.replace('placeholder="Paste YouTube URL or search keywords"', f'placeholder="{data["placeholder"]}"')
        content = content.replace(">Convert</button>", f">{data['convert']}</button>")
        content = content.replace("The quickest way to save YouTube audio and video", data['hero_p'])
        
        # FAQ Section
        content = content.replace("YouTube to MP3 Converter FAQ", data['faq_h2'])
        content = content.replace("How to use the YouTube to MP3 Converter?", data['q1'])
        content = content.replace("Simply copy the URL of the YouTube video you want to convert", data['a1'])
        content = content.replace("Is this YouTube MP3 Downloader safe?", data['q2'])
        content = content.replace("Yes, YT2MP3 is 100% safe. We don't have annoying pop-up ads", data['a2'])
        
        # Menu
        content = content.replace('class="l-label">English', f'class="l-label">{data["name"]}')
        content = content.replace('href="/" class="lang-active">English', 'href="/">English')
        content = content.replace(f'href="/{code}/">', f'href="/{code}/" class="lang-active">')

        with open(lang_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {code} version.")

if __name__ == "__main__":
    generate()
