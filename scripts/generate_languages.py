import os
from pathlib import Path

# Configuration
BASE_DIR = Path("web")
TEMPLATE_FILE = BASE_DIR / "index.html"

LANGS = {
    "es": {
        "name": "Español",
        "title": "YouTube a MP3",
        "hero_h2": "YouTube a MP3",
        "hero_p": "La forma más rápida de guardar audio y video de YouTube.",
        "btn_convert": "Convertir",
        "faq_h2": "Preguntas frecuentes sobre el convertidor de YouTube a MP3",
        "q1": "¿Cómo convertir YouTube a MP3?",
        "a1": "Simplemente copie la URL del video de YouTube, péguela en el cuadro de búsqueda de arriba, seleccione la calidad deseada y haga clic en 'Convertir'.",
        "q2": "¿Es seguro este descargador de MP3 de YouTube?",
        "a2": "Sí, YT2MP3 es 100% seguro. No tenemos anuncios emergentes molestos y no recopilamos sus datos personales.",
    },
    "de": {
        "name": "Deutsch",
        "title": "YouTube zu MP3",
        "hero_h2": "YouTube zu MP3",
        "hero_p": "Der schnellste Weg, YouTube-Audio und -Video zu speichern.",
        "btn_convert": "Konvertieren",
        "faq_h2": "YouTube zu MP3 Konverter FAQ",
        "q1": "Wie konvertiert man YouTube in MP3?",
        "a1": "Kopieren Sie einfach die URL des YouTube-Videos, fügen Sie sie oben in das Suchfeld ein, wählen Sie die gewünschte Qualität und klicken Sie auf 'Konvertieren'.",
        "q2": "Ist dieser YouTube MP3 Downloader sicher?",
        "a2": "Ja, YT2MP3 ist 100% sicher. Wir haben keine nervigen Pop-up-Anzeigen und sammeln keine persönlichen Daten.",
    },
    "fr": {
        "name": "Français",
        "title": "YouTube en MP3",
        "hero_h2": "YouTube en MP3",
        "hero_p": "Le moyen le plus rapide d'enregistrer de l'audio et de la vidéo YouTube.",
        "btn_convert": "Convertir",
        "faq_h2": "FAQ sur le convertisseur YouTube en MP3",
        "q1": "Comment convertir YouTube en MP3 ?",
        "a1": "Copiez simplement l'URL de la vidéo YouTube, collez-la dans la zone de recherche ci-dessus, sélectionnez la qualité souhaitée et cliquez sur 'Convertir'.",
        "q2": "Ce téléchargeur MP3 YouTube est-il sûr ?",
        "a2": "Oui, YT2MP3 est 100% sûr. Nous n'avons pas de publicités pop-up ennuyeuses et nous ne collectons pas vos données personnelles.",
    },
    "hi": {
        "name": "हिन्दी",
        "title": "यूट्यूब से एमपी3",
        "hero_h2": "यूट्यूब से एमपी3",
        "hero_p": "यूट्यूब ऑडियो और वीडियो को सहेजने का सबसे तेज़ तरीका।",
        "btn_convert": "कन्वर्ट करें",
        "faq_h2": "यूट्यूब से एमपी3 कनवर्टर FAQ",
        "q1": "यूट्यूब को एमपी3 में कैसे बदलें?",
        "a1": "बस यूट्यूब वीडियो का URL कॉपी करें, उसे ऊपर सर्च बॉक्स में पेस्ट करें, अपनी पसंद की क्वालिटी चुनें और 'कन्वर्ट' पर क्लिक करें।",
        "q2": "क्या यह यूट्यूब एमपी3 डाउनलोडर सुरक्षित है?",
        "a2": "हाँ, YT2MP3 100% सुरक्षित है। हमारे पास कोई कष्टप्रद पॉप-up विज्ञापन नहीं हैं और हम आपका व्यक्तिगत डेटा एकत्र नहीं करते हैं।",
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
        
        # UI Elements
        content = content.replace("YT2MP3 - YouTube to MP3", f"YT2MP3 - {data['hero_h2']}")
        content = content.replace("The quickest way to save YouTube audio and video", data['hero_p'])
        content = content.replace(">Convert</button>", f">{data['btn_convert']}</button>")
        
        # FAQ Section
        content = content.replace("YouTube to MP3 Converter FAQ", data['faq_h2'])
        content = content.replace("How to use the YouTube to MP3 Converter?", data['q1'])
        content = content.replace("Simply copy the URL of the YouTube video you want to convert", data['a1'])
        content = content.replace("Is this YouTube MP3 Downloader safe?", data['q2'])
        content = content.replace("Yes, YT2MP3 is 100% safe. We don't have annoying pop-up ads", data['a2'])
        
        # Meta
        content = content.replace('class="l-label">English', f'class="l-label">{data["name"]}')
        content = content.replace('href="/" class="lang-active">English', 'href="/">English')
        content = content.replace(f'href="/{code}/">', f'href="/{code}/" class="lang-active">')

        with open(lang_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {code} version.")

if __name__ == "__main__":
    generate()
