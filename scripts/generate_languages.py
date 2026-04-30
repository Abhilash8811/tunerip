import os
from pathlib import Path

# Configuration
BASE_DIR = Path("web")
TEMPLATE_FILE = BASE_DIR / "index.html"

# GOD-LEVEL SEO CONTENT (AI-WRITTEN FOR MAXIMUM RANKING)
LANGS = {
    "es": {
        "name": "Español",
        "title": "Convertidor de YouTube a MP3 - Descargar Música Gratis 320kbps",
        "desc": "El mejor convertidor de YouTube a MP3 en español. Descarga música de alta calidad (320kbps) y videos MP4 de forma segura, rápida y sin anuncios molestos. Compatible con iPhone y Android.",
        "keywords": "descargar musica de youtube, youtube a mp3, convertidor youtube, ytmp3 gratis, bajar musica youtube",
        "h2": "Convertidor de YouTube a MP3 Líder en el Mercado",
        "placeholder": "Pega el enlace de YouTube o busca aquí...",
        "convert": "Convertir Gratis",
        "q1": "¿Cuál es la mejor forma de descargar música de YouTube a MP3?",
        "a1": "La forma más fiable es utilizar yt2mp3.lol. Nuestra herramienta utiliza procesamiento de alta velocidad para extraer el audio directamente de los servidores de YouTube, garantizando una calidad de 320kbps sin pérdida de fidelidad. Simplemente pega el enlace y obtén tu archivo en segundos.",
        "q2": "¿Es legal y seguro usar este convertidor?",
        "a2": "YT2MP3 es 100% seguro. A diferencia de otros sitios, no tenemos anuncios maliciosos ni pop-ups. En cuanto a la legalidad, permitimos la descarga de contenido para uso personal y educativo, respetando siempre los derechos de los creadores.",
        "q3": "¿Puedo descargar listas de reproducción completas?",
        "a3": "¡Sí! Somos uno de los pocos convertidores que soporta la descarga por lotes. Pega el enlace de la 'Playlist' y nuestro sistema procesará cada video individualmente, permitiéndote bajar álbumes completos de una sola vez.",
        "q4": "¿Funciona en dispositivos móviles?",
        "a4": "Totalmente. Hemos optimizado la interfaz para que funcione como una aplicación nativa en iOS y Android. No necesitas instalar nada; solo abre tu navegador y descarga música directamente a tu carpeta de archivos.",
    },
    "hi": {
        "name": "हिन्दी",
        "title": "यूट्यूब से एमपी3 कनवर्टर - फ्री गाना डाउनलोड करें (320kbps)",
        "desc": "सबसे तेज़ यूट्यूब से एमपी3 कनवर्टर। यूट्यूब वीडियो को हाई क्वालिटी (320kbps) ऑडियो में बदलें। बिना विज्ञापन और बिना किसी ऐप के, सुरक्षित रूप से गाने डाउनलोड करें।",
        "keywords": "यूट्यूब से एमपी3, यूट्यूब गाना डाउनलोडर, फ्री म्यूजिक डाउनलोड, ytmp3 हिंदी, यूट्यूब वीडियो कनवर्टर",
        "h2": "भारत का नंबर 1 यूट्यूब से एमपी3 कनवर्टर",
        "placeholder": "यूट्यूब लिंक यहाँ डालें या गाना सर्च करें...",
        "convert": "मुफ्त डाउनलोड",
        "q1": "यूट्यूब वीडियो को एमपी3 गाने में कैसे बदलें?",
        "a1": "यूट्यूब से गाना डाउनलोड करना अब बहुत आसान है। बस अपने पसंदीदा वीडियो का URL कॉपी करें, उसे ऊपर दिए गए बॉक्स में पेस्ट करें, और 'कन्वर्ट' बटन दबाएं। हमारा सर्वर तुरंत वीडियो को 320kbps MP3 में बदल देगा जिसे आप सीधे अपने फोन में सेव कर सकते हैं।",
        "q2": "क्या यह सुरक्षित और विज्ञापन-मुक्त है?",
        "a2": "हाँ, YT2MP3 पूरी तरह से सुरक्षित है। हमने इसे इस तरह से बनाया है कि आपको कोई भी खराब विज्ञापन या पॉप-अप न दिखे। हम आपकी गोपनीयता का सम्मान करते हैं और कोई भी व्यक्तिगत डेटा स्टोर नहीं करते हैं।",
        "q3": "क्या मैं पूरी प्लेलिस्ट एक साथ डाउनलोड कर सकता हूँ?",
        "a3": "बिल्कुल! अगर आपके पास गानों की पूरी प्लेलिस्ट है, तो बस प्लेलिस्ट का लिंक पेस्ट करें। हमारा टूल हर वीडियो को अलग-अलग प्रोसेस करेगा, जिससे आप एक ही बार में कई गाने डाउनलोड कर पाएंगे।",
        "q4": "क्या यह एंड्रॉइड और आईफोन पर काम करता है?",
        "a4": "हाँ, यह वेबसाइट मोबाइल के लिए ही बनाई गई है। चाहे आपके पास सैमसंग हो या आईफोन, यह हर ब्राउज़र पर मक्खन की तरह काम करता है। आपको किसी भी बाहरी ऐप को इंस्टॉल करने की जरूरत नहीं है।",
    },
    "ar": {
        "name": "العربية",
        "title": "محول يوتيوب إلى MP3 - تحميل موسيقى يوتيوب بجودة عالية",
        "desc": "أسرع محول يوتيوب إلى MP3. قم بتحميل مقاطع فيديو يوتيوب وتحويلها إلى صوت عالي الجودة (320kbps) مجانًا وبدون إعلانات. يدعم تحميل القوائم والشورتس.",
        "keywords": "تحميل من اليوتيوب, يوتيوب إلى mp3, محول يوتيوب, تحميل موسيقى, ytmp3 بالعربي",
        "h2": "أفضل أداة لتحويل يوتيوب إلى MP3 في العالم العربي",
        "placeholder": "الصق رابط الفيديو أو ابحث عن الأغنية...",
        "convert": "تحميل مجاني",
        "q1": "كيف يمكنني تحويل فيديوهات يوتيوب إلى ملفات صوتية؟",
        "a1": "كل ما عليك فعله هو نسخ رابط الفيديو من يوتيوب، ولصقه في مربع البحث أعلاه، ثم اختيار الجودة التي تفضلها. نظامنا المتطور سيقوم بمعالجة الفيديو وتحويله إلى ملف MP3 نقي في غضون ثوانٍ قليلة.",
        "q2": "هل الموقع آمن للاستخدام الشخصي؟",
        "a2": "نعم، أمن المستخدم هو أولويتنا القصوى. موقعنا خالٍ تمامًا من الفيروسات والإعلانات المنبثقة المزعجة التي تجدها في المواقع الأخرى. يمكنك التحميل بكل ثقة وأمان.",
        "q3": "هل يدعم الموقع تحميل قوائم التشغيل (Playlists)؟",
        "a3": "بالتأكيد. يمكنك وضع رابط قائمة تشغيل كاملة، وسيقوم المحول باستخراج جميع الفيديوهات منها لتتمكن من تحميلها كملفات منفصلة بجودة عالية.",
        "q4": "هل يمكنني التحميل مباشرة على هاتفي؟",
        "a4": "نعم، الموقع مصمم ليعمل بامتياز على جميع الهواتف الذكية (آيفون وأندرويد). لن تحتاج إلى تثبيت أي برامج إضافية، العملية تتم بالكامل داخل متصفحك.",
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
        
        # SEO RICH CONTENT INJECTION
        content = content.replace("<title>YT to MP3 - YouTube MP3 Converter & Downloader (Fast & Free)</title>", f"<title>{data['title']}</title>")
        content = content.replace('content="The fastest YT to MP3 converter. Download high-quality audio (320kbps) and videos from YouTube with our free YouTube MP3 Downloader. Safe, ad-free, and reliable."', f'content="{data["desc"]}"')
        content = content.replace('content="yt to mp3, youtube to mp3, youtube mp3, youtube converter, youtube downloader, yt mp3 converter, 320kbps mp3, wav converter, flac converter, youtube to mp4, ytmp3"', f'content="{data["keywords"]}"')

        # UI RICH CONTENT
        content = content.replace("YT2MP3 - YouTube to MP3", f"YT2MP3 - {data['h2']}")
        content = content.replace('placeholder="Paste YouTube URL or search keywords"', f'placeholder="{data["placeholder"]}"')
        content = content.replace(">Convert</button>", f">{data['convert']}</button>")
        
        # FAQ MASTER RICH CONTENT
        content = content.replace("How to convert YouTube to MP3?", data['q1'])
        content = content.replace("Simply copy the URL of the YouTube video, paste it into the search box above, select your desired format/quality, and click 'Convert'. Your file will be ready for download in seconds.", data['a1'])
        
        content = content.replace("Is yt2mp3.lol free and safe?", data['q2'])
        content = content.replace("Yes! YT2MP3 is 100% free and safe. We don't have annoying pop-up ads, we don't require registration, and we don't store your data. It's a clean, high-performance YouTube downloader.", data['a2'])
        
        content = content.replace("What is the highest MP3 quality available?", data['q3'])
        content = content.replace("We support true 320kbps MP3 exports. You can also choose lossless formats like WAV and FLAC for professional-grade audio quality.", data['a3'])
        
        content = content.replace("Can I use this on Android or iPhone?", data['q4'])
        content = content.replace("Absolutely. Our site is mobile-first and works perfectly in any browser on Android, iOS (iPhone/iPad), and Tablets without installing any apps.", data['a4'])

        # Language Menu
        content = content.replace('class="l-label">English', f'class="l-label">{data["name"]}')
        content = content.replace('href="/" class="lang-active">English', 'href="/">English')
        content = content.replace(f'href="/{code}/">', f'href="/{code}/" class="lang-active">')

        with open(lang_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {code} version with God-Level SEO.")

if __name__ == "__main__":
    generate()
