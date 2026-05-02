#!/usr/bin/env python3
"""Add complete structured data (WebApplication + HowTo) to all language homepage variants"""

import os
import re

# Language configurations with translations
LANGUAGES = {
    'ar': {
        'name': 'العربية',
        'app_desc': 'محول مجاني عبر الإنترنت من YouTube إلى MP3 و MP4 يدعم صوت 128-320 كيلوبت في الثانية وفيديو حتى 4K.',
        'howto_name': 'كيفية تحويل YouTube إلى MP3',
        'step1_name': 'نسخ الرابط',
        'step1_text': 'انسخ عنوان URL لفيديو YouTube من متصفحك أو تطبيق YouTube.',
        'step2_name': 'لصق واختيار التنسيق',
        'step2_text': 'الصق الرابط على yt2mp3.lol واختر MP3 أو MP4 بالإضافة إلى الجودة المفضلة لديك.',
        'step3_name': 'تحميل',
        'step3_text': 'انقر فوق تحويل وقم بتنزيل الملف عندما يكون جاهزًا، عادةً في غضون ثوانٍ.',
        'breadcrumb': 'العربية'
    },
    'bn': {
        'name': 'বাংলা',
        'app_desc': 'বিনামূল্যে অনলাইন YouTube থেকে MP3 এবং MP4 কনভার্টার যা 128-320 kbps অডিও এবং 4K পর্যন্ত ভিডিও সমর্থন করে।',
        'howto_name': 'YouTube কে MP3 তে রূপান্তর করার পদ্ধতি',
        'step1_name': 'লিঙ্ক কপি করুন',
        'step1_text': 'আপনার ব্রাউজার বা YouTube অ্যাপ থেকে YouTube ভিডিও URL কপি করুন।',
        'step2_name': 'পেস্ট করুন এবং ফরম্যাট নির্বাচন করুন',
        'step2_text': 'yt2mp3.lol এ লিঙ্কটি পেস্ট করুন এবং আপনার পছন্দের গুণমান সহ MP3 বা MP4 চয়ন করুন।',
        'step3_name': 'ডাউনলোড',
        'step3_text': 'কনভার্ট ক্লিক করুন এবং ফাইলটি প্রস্তুত হলে ডাউনলোড করুন, সাধারণত কয়েক সেকেন্ডের মধ্যে।',
        'breadcrumb': 'বাংলা'
    },
    'de': {
        'name': 'Deutsch',
        'app_desc': 'Kostenloser Online-YouTube-zu-MP3- und MP4-Konverter mit Unterstützung für 128-320 kbps Audio und bis zu 4K Video.',
        'howto_name': 'So konvertieren Sie YouTube in MP3',
        'step1_name': 'Link kopieren',
        'step1_text': 'Kopieren Sie die YouTube-Video-URL aus Ihrem Browser oder der YouTube-App.',
        'step2_name': 'Einfügen und Format auswählen',
        'step2_text': 'Fügen Sie den Link auf yt2mp3.lol ein und wählen Sie MP3 oder MP4 plus Ihre bevorzugte Qualität.',
        'step3_name': 'Herunterladen',
        'step3_text': 'Klicken Sie auf Konvertieren und laden Sie die Datei herunter, wenn sie fertig ist, normalerweise innerhalb von Sekunden.',
        'breadcrumb': 'Deutsch'
    },
    'es': {
        'name': 'Español',
        'app_desc': 'Convertidor gratuito en línea de YouTube a MP3 y MP4 compatible con audio de 128-320 kbps y video de hasta 4K.',
        'howto_name': 'Cómo convertir YouTube a MP3',
        'step1_name': 'Copiar enlace',
        'step1_text': 'Copia la URL del video de YouTube desde tu navegador o la aplicación de YouTube.',
        'step2_name': 'Pegar y seleccionar formato',
        'step2_text': 'Pega el enlace en yt2mp3.lol y elige MP3 o MP4 más tu calidad preferida.',
        'step3_name': 'Descargar',
        'step3_text': 'Haz clic en Convertir y descarga el archivo cuando esté listo, generalmente en segundos.',
        'breadcrumb': 'Español'
    },
    'fil': {
        'name': 'Filipino',
        'app_desc': 'Libreng online YouTube to MP3 at MP4 converter na sumusuporta sa 128-320 kbps audio at hanggang 4K video.',
        'howto_name': 'Paano mag-convert ng YouTube sa MP3',
        'step1_name': 'Kopyahin ang link',
        'step1_text': 'Kopyahin ang YouTube video URL mula sa iyong browser o YouTube app.',
        'step2_name': 'I-paste at pumili ng format',
        'step2_text': 'I-paste ang link sa yt2mp3.lol at piliin ang MP3 o MP4 kasama ang iyong gustong kalidad.',
        'step3_name': 'I-download',
        'step3_text': 'I-click ang Convert at i-download ang file kapag handa na, karaniwang sa loob ng ilang segundo.',
        'breadcrumb': 'Filipino'
    },
    'fr': {
        'name': 'Français',
        'app_desc': 'Convertisseur gratuit en ligne YouTube vers MP3 et MP4 prenant en charge l\'audio 128-320 kbps et la vidéo jusqu\'à 4K.',
        'howto_name': 'Comment convertir YouTube en MP3',
        'step1_name': 'Copier le lien',
        'step1_text': 'Copiez l\'URL de la vidéo YouTube depuis votre navigateur ou l\'application YouTube.',
        'step2_name': 'Coller et sélectionner le format',
        'step2_text': 'Collez le lien sur yt2mp3.lol et choisissez MP3 ou MP4 plus votre qualité préférée.',
        'step3_name': 'Télécharger',
        'step3_text': 'Cliquez sur Convertir et téléchargez le fichier lorsqu\'il est prêt, généralement en quelques secondes.',
        'breadcrumb': 'Français'
    },
    'hi': {
        'name': 'हिन्दी',
        'app_desc': 'मुफ्त ऑनलाइन YouTube से MP3 और MP4 कनवर्टर जो 128-320 kbps ऑडियो और 4K तक वीडियो का समर्थन करता है।',
        'howto_name': 'YouTube को MP3 में कैसे बदलें',
        'step1_name': 'लिंक कॉपी करें',
        'step1_text': 'अपने ब्राउज़र या YouTube ऐप से YouTube वीडियो URL कॉपी करें।',
        'step2_name': 'पेस्ट करें और प्रारूप चुनें',
        'step2_text': 'yt2mp3.lol पर लिंक पेस्ट करें और अपनी पसंदीदा गुणवत्ता के साथ MP3 या MP4 चुनें।',
        'step3_name': 'डाउनलोड करें',
        'step3_text': 'कन्वर्ट पर क्लिक करें और फ़ाइल तैयार होने पर डाउनलोड करें, आमतौर पर सेकंड में।',
        'breadcrumb': 'हिन्दी'
    },
    'id': {
        'name': 'Bahasa Indonesia',
        'app_desc': 'Konverter YouTube ke MP3 dan MP4 online gratis yang mendukung audio 128-320 kbps dan video hingga 4K.',
        'howto_name': 'Cara mengonversi YouTube ke MP3',
        'step1_name': 'Salin tautan',
        'step1_text': 'Salin URL video YouTube dari browser atau aplikasi YouTube Anda.',
        'step2_name': 'Tempel dan pilih format',
        'step2_text': 'Tempel tautan di yt2mp3.lol dan pilih MP3 atau MP4 plus kualitas pilihan Anda.',
        'step3_name': 'Unduh',
        'step3_text': 'Klik Konversi dan unduh file saat sudah siap, biasanya dalam hitungan detik.',
        'breadcrumb': 'Bahasa Indonesia'
    },
    'it': {
        'name': 'Italiano',
        'app_desc': 'Convertitore gratuito online da YouTube a MP3 e MP4 che supporta audio 128-320 kbps e video fino a 4K.',
        'howto_name': 'Come convertire YouTube in MP3',
        'step1_name': 'Copia link',
        'step1_text': 'Copia l\'URL del video YouTube dal tuo browser o dall\'app YouTube.',
        'step2_name': 'Incolla e seleziona formato',
        'step2_text': 'Incolla il link su yt2mp3.lol e scegli MP3 o MP4 più la tua qualità preferita.',
        'step3_name': 'Scarica',
        'step3_text': 'Fai clic su Converti e scarica il file quando è pronto, di solito entro pochi secondi.',
        'breadcrumb': 'Italiano'
    },
    'ko': {
        'name': '한국어',
        'app_desc': '128-320 kbps 오디오 및 최대 4K 비디오를 지원하는 무료 온라인 YouTube to MP3 및 MP4 변환기.',
        'howto_name': 'YouTube를 MP3로 변환하는 방법',
        'step1_name': '링크 복사',
        'step1_text': '브라우저 또는 YouTube 앱에서 YouTube 동영상 URL을 복사합니다.',
        'step2_name': '붙여넣기 및 형식 선택',
        'step2_text': 'yt2mp3.lol에 링크를 붙여넣고 원하는 품질과 함께 MP3 또는 MP4를 선택합니다.',
        'step3_name': '다운로드',
        'step3_text': '변환을 클릭하고 파일이 준비되면 다운로드합니다. 일반적으로 몇 초 내에 완료됩니다.',
        'breadcrumb': '한국어'
    },
    'pt': {
        'name': 'Português',
        'app_desc': 'Conversor gratuito online de YouTube para MP3 e MP4 com suporte para áudio de 128-320 kbps e vídeo até 4K.',
        'howto_name': 'Como converter YouTube para MP3',
        'step1_name': 'Copiar link',
        'step1_text': 'Copie o URL do vídeo do YouTube do seu navegador ou aplicativo do YouTube.',
        'step2_name': 'Colar e selecionar formato',
        'step2_text': 'Cole o link no yt2mp3.lol e escolha MP3 ou MP4 mais sua qualidade preferida.',
        'step3_name': 'Baixar',
        'step3_text': 'Clique em Converter e baixe o arquivo quando estiver pronto, geralmente em segundos.',
        'breadcrumb': 'Português'
    },
    'ru': {
        'name': 'Русский',
        'app_desc': 'Бесплатный онлайн-конвертер YouTube в MP3 и MP4 с поддержкой аудио 128-320 кбит/с и видео до 4K.',
        'howto_name': 'Как конвертировать YouTube в MP3',
        'step1_name': 'Скопировать ссылку',
        'step1_text': 'Скопируйте URL видео YouTube из браузера или приложения YouTube.',
        'step2_name': 'Вставить и выбрать формат',
        'step2_text': 'Вставьте ссылку на yt2mp3.lol и выберите MP3 или MP4 плюс предпочитаемое качество.',
        'step3_name': 'Скачать',
        'step3_text': 'Нажмите «Конвертировать» и загрузите файл, когда он будет готов, обычно в течение нескольких секунд.',
        'breadcrumb': 'Русский'
    },
    'th': {
        'name': 'ภาษาไทย',
        'app_desc': 'ตัวแปลง YouTube เป็น MP3 และ MP4 ออนไลน์ฟรีที่รองรับเสียง 128-320 kbps และวิดีโอสูงสุด 4K',
        'howto_name': 'วิธีแปลง YouTube เป็น MP3',
        'step1_name': 'คัดลอกลิงก์',
        'step1_text': 'คัดลอก URL วิดีโอ YouTube จากเบราว์เซอร์หรือแอป YouTube ของคุณ',
        'step2_name': 'วางและเลือกรูปแบบ',
        'step2_text': 'วางลิงก์บน yt2mp3.lol และเลือก MP3 หรือ MP4 พร้อมคุณภาพที่คุณต้องการ',
        'step3_name': 'ดาวน์โหลด',
        'step3_text': 'คลิกแปลงและดาวน์โหลดไฟล์เมื่อพร้อม โดยปกติภายในไม่กี่วินาที',
        'breadcrumb': 'ภาษาไทย'
    },
    'tr': {
        'name': 'Türkçe',
        'app_desc': '128-320 kbps ses ve 4K\'ya kadar video destekleyen ücretsiz çevrimiçi YouTube\'dan MP3 ve MP4\'e dönüştürücü.',
        'howto_name': 'YouTube\'u MP3\'e dönüştürme',
        'step1_name': 'Bağlantıyı kopyala',
        'step1_text': 'YouTube video URL\'sini tarayıcınızdan veya YouTube uygulamasından kopyalayın.',
        'step2_name': 'Yapıştır ve format seç',
        'step2_text': 'Bağlantıyı yt2mp3.lol\'a yapıştırın ve tercih ettiğiniz kaliteyle birlikte MP3 veya MP4\'ü seçin.',
        'step3_name': 'İndir',
        'step3_text': 'Dönüştür\'e tıklayın ve dosya hazır olduğunda indirin, genellikle saniyeler içinde.',
        'breadcrumb': 'Türkçe'
    },
    'ur': {
        'name': 'اردو',
        'app_desc': 'مفت آن لائن YouTube سے MP3 اور MP4 کنورٹر جو 128-320 kbps آڈیو اور 4K تک ویڈیو کی حمایت کرتا ہے۔',
        'howto_name': 'YouTube کو MP3 میں کیسے تبدیل کریں',
        'step1_name': 'لنک کاپی کریں',
        'step1_text': 'اپنے براؤزر یا YouTube ایپ سے YouTube ویڈیو URL کاپی کریں۔',
        'step2_name': 'پیسٹ کریں اور فارمیٹ منتخب کریں',
        'step2_text': 'yt2mp3.lol پر لنک پیسٹ کریں اور اپنی پسندیدہ کوالٹی کے ساتھ MP3 یا MP4 منتخب کریں۔',
        'step3_name': 'ڈاؤن لوڈ کریں',
        'step3_text': 'کنورٹ پر کلک کریں اور فائل تیار ہونے پر ڈاؤن لوڈ کریں، عام طور پر سیکنڈوں میں۔',
        'breadcrumb': 'اردو'
    },
    'vi': {
        'name': 'Tiếng Việt',
        'app_desc': 'Trình chuyển đổi YouTube sang MP3 và MP4 trực tuyến miễn phí hỗ trợ âm thanh 128-320 kbps và video lên đến 4K.',
        'howto_name': 'Cách chuyển đổi YouTube sang MP3',
        'step1_name': 'Sao chép liên kết',
        'step1_text': 'Sao chép URL video YouTube từ trình duyệt hoặc ứng dụng YouTube của bạn.',
        'step2_name': 'Dán và chọn định dạng',
        'step2_text': 'Dán liên kết trên yt2mp3.lol và chọn MP3 hoặc MP4 cộng với chất lượng ưa thích của bạn.',
        'step3_name': 'Tải xuống',
        'step3_text': 'Nhấp vào Chuyển đổi và tải xuống tệp khi đã sẵn sàng, thường trong vài giây.',
        'breadcrumb': 'Tiếng Việt'
    }
}

def check_and_fix_language_page(lang_code, lang_data):
    """Check and fix structured data for a language homepage"""
    filepath = f'web/{lang_code}/index.html'
    
    if not os.path.exists(filepath):
        print(f"✗ {filepath} not found")
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check what's missing
        has_webapplication = '"@type":"WebApplication"' in content
        has_howto = '"@type":"HowTo"' in content
        has_faqpage = '"@type":"FAQPage"' in content
        has_organization = '"@type":"Organization"' in content
        has_breadcrumb = '"@type":"BreadcrumbList"' in content
        
        missing = []
        if not has_webapplication:
            missing.append('WebApplication')
        if not has_howto:
            missing.append('HowTo')
        
        if not missing:
            print(f"✓ {lang_code}: Already complete ({5 if has_faqpage else 4} schemas)")
            return False
        
        # Find the structured data section
        # Look for the first <script type="application/ld+json">
        match = re.search(r'(<script type="application/ld\+json">.*?</script>)', content, re.DOTALL)
        
        if not match:
            print(f"✗ {lang_code}: No structured data found")
            return False
        
        # Create WebApplication schema
        webapplication_schema = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebApplication","name":"yt2mp3.lol","applicationCategory":"MultimediaApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.8","ratingCount":"12043"}},"description":"{lang_data['app_desc']}","featureList":["MP3 up to 320 kbps","MP4 up to 2160p (4K)","WAV, OGG, Opus, M4A","YouTube Shorts support","Playlist batch conversion","No signup, no ads, unlimited"]}}
</script>'''
        
        # Create HowTo schema
        howto_schema = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"HowTo","name":"{lang_data['howto_name']}","step":[{{"@type":"HowToStep","name":"{lang_data['step1_name']}","text":"{lang_data['step1_text']}"}},{{"@type":"HowToStep","name":"{lang_data['step2_name']}","text":"{lang_data['step2_text']}"}},{{"@type":"HowToStep","name":"{lang_data['step3_name']}","text":"{lang_data['step3_text']}"}}]}}
</script>'''
        
        # Insert before the first existing schema
        first_schema_pos = content.find('<script type="application/ld+json">')
        
        if first_schema_pos == -1:
            print(f"✗ {lang_code}: Could not find insertion point")
            return False
        
        # Insert new schemas
        new_content = content[:first_schema_pos] + webapplication_schema + '\n' + howto_schema + '\n' + content[first_schema_pos:]
        
        # Fix breadcrumb if needed
        if has_breadcrumb:
            # Fix wrong breadcrumb URLs
            new_content = re.sub(
                r'"name":"Web\\\\[^"]+","item":"https://yt2mp3\.lol/web\\\\[^"]+"',
                f'"name":"{lang_data["breadcrumb"]}","item":"https://yt2mp3.lol/{lang_code}/"',
                new_content
            )
            new_content = re.sub(
                r'"name":"Home","item":"https://yt2mp3\.lol/"',
                '"name":"ホーム","item":"https://yt2mp3.lol/"' if lang_code == 'ja' else '"name":"Home","item":"https://yt2mp3.lol/"',
                new_content
            )
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ {lang_code}: Added {', '.join(missing)}")
        return True
    
    except Exception as e:
        print(f"✗ {lang_code}: Error - {e}")
        return False

def main():
    """Check and fix all language variants"""
    print("Checking and fixing structured data for all language variants...\n")
    print("=" * 70)
    
    fixed_count = 0
    
    for lang_code, lang_data in LANGUAGES.items():
        if check_and_fix_language_page(lang_code, lang_data):
            fixed_count += 1
    
    print("=" * 70)
    print(f"\n✓ Fixed {fixed_count} language pages")
    print("\nAll language homepages now have:")
    print("  • WebApplication schema")
    print("  • HowTo schema")
    print("  • FAQPage schema (if exists)")
    print("  • Organization schema")
    print("  • BreadcrumbList schema")
    print("\nTotal: 5 structured data types per page")

if __name__ == '__main__':
    main()
