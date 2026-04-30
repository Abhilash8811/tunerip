#!/usr/bin/env python3
"""
Complete ALL translations - translate every remaining English content paragraph
This script will translate ALL content sections that were missed in the initial translation
"""

from pathlib import Path
import re

# Complete content translations for Hindi
hindi_content = {
    # Table content
    'Universal audio playback': 'सार्वभौमिक ऑडियो प्लेबैक',
    'Video playback everywhere': 'हर जगह वीडियो प्लेबैक',
    'Lossless audio editing': 'लॉसलेस ऑडियो एडिटिंग',
    'Apple devices': 'Apple डिवाइस',
    'Native AAC': 'नेटिव AAC',
    
    # Long paragraphs
    'Downloading videos one by one is incredibly tedious. Our YouTube Playlist Downloader is engineered for bulk operations. By parsing the playlist metadata, our servers generate individual conversion jobs for every single video in the list, allowing you to download an entire album, lecture series, or podcast backlog with minimal effort.': 'एक-एक करके वीडियो डाउनलोड करना अविश्वसनीय रूप से थकाऊ है। हमारा YouTube प्लेलिस्ट डाउनलोडर बल्क ऑपरेशन के लिए इंजीनियर किया गया है। प्लेलिस्ट मेटाडेटा को पार्स करके, हमारे सर्वर सूची में प्रत्येक एकल वीडियो के लिए व्यक्तिगत रूपांतरण कार्य उत्पन्न करते हैं, जिससे आप न्यूनतम प्रयास के साथ एक संपूर्ण एल्बम, लेक्चर सीरीज़, या पॉडकास्ट बैकलॉग डाउनलोड कर सकते हैं।',
    
    'When you download a playlist, organization is key. Our system automatically grabs the original video titles and structures the downloads so you can easily maintain the intended order. This is perfect for sequential tutorials, multi-part documentaries, or chronologically ordered music albums.': 'जब आप एक प्लेलिस्ट डाउनलोड करते हैं, तो संगठन महत्वपूर्ण है। हमारा सिस्टम स्वचालित रूप से मूल वीडियो शीर्षक को पकड़ता है और डाउनलोड को संरचित करता है ताकि आप आसानी से इच्छित क्रम बनाए रख सकें। यह क्रमिक ट्यूटोरियल, बहु-भाग वृत्तचित्र, या कालानुक्रमिक रूप से क्रमबद्ध संगीत एल्बमों के लिए एकदम सही है।',
    
    "You aren't locked into a single format. You can choose to download an entire music playlist as crisp 320kbps MP3s, or an entire educational course as 1080p MP4s. Our FFmpeg backend applies your selected format uniformly across all items in the batch.": 'आप एक ही फॉर्मेट में लॉक नहीं हैं। आप एक संपूर्ण संगीत प्लेलिस्ट को क्रिस्प 320kbps MP3 के रूप में डाउनलोड करना चुन सकते हैं, या एक संपूर्ण शैक्षिक पाठ्यक्रम को 1080p MP4 के रूप में। हमारा FFmpeg बैकएंड बैच में सभी आइटम पर आपके चयनित फॉर्मेट को समान रूप से लागू करता है।',
    
    "We don't make you wait for one video to finish before starting the next. Our cloud infrastructure utilizes high-concurrency processing, meaning multiple videos from your playlist are downloaded and converted simultaneously. A 50-video playlist is processed significantly faster than doing it manually.": 'हम आपको अगला शुरू करने से पहले एक वीडियो समाप्त होने की प्रतीक्षा नहीं करवाते। हमारा क्लाउड इंफ्रास्ट्रक्चर उच्च-समवर्ती प्रसंस्करण का उपयोग करता है, जिसका अर्थ है कि आपकी प्लेलिस्ट से कई वीडियो एक साथ डाउनलोड और परिवर्तित किए जाते हैं। 50-वीडियो प्लेलिस्ट को मैन्युअल रूप से करने की तुलना में काफी तेजी से संसाधित किया जाता है।',
    
    "Whether it's a 10-track EP or a massive 300-video mega-mix, our tool is built to handle it. While extremely large playlists may take a few minutes to fully parse and render download buttons, our backend will not time out or crash during the operation.": 'चाहे वह 10-ट्रैक EP हो या विशाल 300-वीडियो मेगा-मिक्स, हमारा टूल इसे संभालने के लिए बनाया गया है। जबकि अत्यधिक बड़ी प्लेलिस्ट को पूरी तरह से पार्स करने और डाउनलोड बटन रेंडर करने में कुछ मिनट लग सकते हैं, हमारा बैकएंड ऑपरेशन के दौरान टाइम आउट या क्रैश नहीं होगा।',
    
    "Did YouTube's algorithm create the perfect 'My Mix' or 'Discover Weekly' equivalent for you? Just copy the URL of that auto-generated playlist and paste it here. You can rip the entire curated mix to your local device for offline listening on road trips or flights.": "क्या YouTube के एल्गोरिदम ने आपके लिए सही 'My Mix' या 'Discover Weekly' समकक्ष बनाया? बस उस ऑटो-जनरेटेड प्लेलिस्ट के URL को कॉपी करें और यहां पेस्ट करें। आप रोड ट्रिप या फ्लाइट पर ऑफ़लाइन सुनने के लिए अपने स्थानीय डिवाइस पर संपूर्ण क्यूरेटेड मिक्स को रिप कर सकते हैं।",
    
    'Many professors and online instructors organize their course modules into public YouTube playlists. Students can use our tool to download the entire semester\'s worth of lectures in MP4 format, ensuring they have access to study materials even without an internet connection.': 'कई प्रोफेसर और ऑनलाइन प्रशिक्षक अपने पाठ्यक्रम मॉड्यूल को सार्वजनिक YouTube प्लेलिस्ट में व्यवस्थित करते हैं। छात्र हमारे टूल का उपयोग करके पूरे सेमेस्टर के लेक्चर को MP4 फॉर्मेट में डाउनलोड कर सकते हैं, यह सुनिश्चित करते हुए कि उनके पास इंटरनेट कनेक्शन के बिना भी अध्ययन सामग्री तक पहुंच है।',
    
    "Playlists often contain videos that have been deleted, made private, or restricted in your region. Our parser intelligently skips these dead links and continues processing the available videos, so your batch download isn't ruined by a single broken link.": 'प्लेलिस्ट में अक्सर ऐसे वीडियो होते हैं जो हटा दिए गए हैं, निजी बना दिए गए हैं, या आपके क्षेत्र में प्रतिबंधित हैं। हमारा पार्सर बुद्धिमानी से इन मृत लिंक को छोड़ देता है और उपलब्ध वीडियो को संसाधित करना जारी रखता है, इसलिए आपका बैच डाउनलोड एक टूटे हुए लिंक से बर्बाद नहीं होता है।',
    
    "1. Navigate to the playlist on YouTube. Ensure the URL contains 'list=' (e.g., youtube.com/playlist?list=...). 2. Copy the URL. 3. Paste it into our converter. 4. Select your global format (MP3 or MP4). 5. Click Convert. 6. Wait for the parser to extract the videos, then click the individual download buttons as they appear.": "1. YouTube पर प्लेलिस्ट पर नेविगेट करें। सुनिश्चित करें कि URL में 'list=' है (जैसे, youtube.com/playlist?list=...)। 2. URL कॉपी करें। 3. इसे हमारे कनवर्टर में पेस्ट करें। 4. अपना ग्लोबल फॉर्मेट (MP3 या MP4) चुनें। 5. बदलें पर क्लिक करें। 6. पार्सर के वीडियो निकालने की प्रतीक्षा करें, फिर जैसे ही वे दिखाई दें व्यक्तिगत डाउनलोड बटन पर क्लिक करें।",
    
    # FAQ answers
    'No hard cap, but very large playlists (500+ videos) may take several minutes to process in full.': 'कोई हार्ड कैप नहीं, लेकिन बहुत बड़ी प्लेलिस्ट (500+ वीडियो) को पूरी तरह से संसाधित करने में कई मिनट लग सकते हैं।',
    
    'Yes. Original playlist ordering is preserved by default.': 'हां। मूल प्लेलिस्ट क्रम डिफ़ॉल्ट रूप से संरक्षित है।',
    
    'We can theoretically parse playlists of any size, but for optimal performance and browser stability, we recommend downloading playlists with 200 videos or fewer at a time.': 'हम सैद्धांतिक रूप से किसी भी आकार की प्लेलिस्ट को पार्स कर सकते हैं, लेकिन इष्टतम प्रदर्शन और ब्राउज़र स्थिरता के लिए, हम एक समय में 200 या उससे कम वीडियो वाली प्लेलिस्ट डाउनलोड करने की सलाह देते हैं।',
    
    'Each video in the playlist is converted and downloaded as its own separate file. We do not merge them into a single massive audio/video file.': 'प्लेलिस्ट में प्रत्येक वीडियो को अपनी अलग फ़ाइल के रूप में परिवर्तित और डाउनलोड किया जाता है। हम उन्हें एक विशाल ऑडियो/वीडियो फ़ाइल में मर्ज नहीं करते हैं।',
    
    "Your 'Watch Later' playlist is private to your account. Our servers cannot access it. You would need to move those videos to a Public or Unlisted playlist first.": "आपकी 'Watch Later' प्लेलिस्ट आपके खाते के लिए निजी है। हमारे सर्वर इसे एक्सेस नहीं कर सकते। आपको पहले उन वीडियो को सार्वजनिक या अनलिस्टेड प्लेलिस्ट में ले जाना होगा।",
    
    'If the live stream has ended and is available as a VOD, it will download normally. If the stream is currently live, the tool will skip it, as it has no finite length.': 'यदि लाइव स्ट्रीम समाप्त हो गई है और VOD के रूप में उपलब्ध है, तो यह सामान्य रूप से डाउनलोड होगी। यदि स्ट्रीम वर्तमान में लाइव है, तो टूल इसे छोड़ देगा, क्योंकि इसकी कोई सीमित लंबाई नहीं है।',
    
    'Parsing the list takes only seconds. The conversion time depends on the total length of the videos and the chosen quality, but our concurrent processing usually finishes a typical music playlist in under 3 minutes.': 'सूची को पार्स करने में केवल सेकंड लगते हैं। रूपांतरण समय वीडियो की कुल लंबाई और चुनी गई गुणवत्ता पर निर्भर करता है, लेकिन हमारी समवर्ती प्रसंस्करण आमतौर पर 3 मिनट से कम में एक विशिष्ट संगीत प्लेलिस्ट समाप्त कर देती है।',
    
    'Currently, browser security restrictions prevent websites from automatically triggering 50 file downloads at once. You will need to click the download button for each generated file.': 'वर्तमान में, ब्राउज़र सुरक्षा प्रतिबंध वेबसाइटों को एक बार में 50 फ़ाइल डाउनलोड को स्वचालित रूप से ट्रिगर करने से रोकते हैं। आपको प्रत्येक उत्पन्न फ़ाइल के लिए डाउनलोड बटन पर क्लिक करना होगा।',
    
    'The individual video files will have their respective video thumbnails embedded as metadata (for audio formats) or as the poster frame (for video formats).': 'व्यक्तिगत वीडियो फ़ाइलों में उनके संबंधित वीडियो थंबनेल मेटाडेटा के रूप में एम्बेडेड होंगे (ऑडियो फॉर्मेट के लिए) या पोस्टर फ्रेम के रूप में (वीडियो फॉर्मेट के लिए)।',
    
    "If the channel has a 'Play All' button or a playlist containing all their uploads, yes. Just copy that specific playlist URL.": "यदि चैनल में 'Play All' बटन है या उनके सभी अपलोड वाली प्लेलिस्ट है, तो हां। बस उस विशिष्ट प्लेलिस्ट URL को कॉपी करें।",
    
    "The files retain their original YouTube titles. If the creator numbered the titles (e.g., 'Episode 1: ...'), that numbering will be in your downloaded file.": "फ़ाइलें अपने मूल YouTube शीर्षक बनाए रखती हैं। यदि निर्माता ने शीर्षकों को क्रमांकित किया है (जैसे, 'Episode 1: ...'), तो वह क्रमांकन आपकी डाउनलोड की गई फ़ाइल में होगा।",
    
    'This usually means the missing videos are either Private, Deleted, or Region-Blocked. Our tool can only fetch publicly accessible media.': 'इसका आमतौर पर मतलब है कि लापता वीडियो या तो निजी, हटाए गए, या क्षेत्र-अवरुद्ध हैं। हमारा टूल केवल सार्वजनिक रूप से सुलभ मीडिया प्राप्त कर सकता है।',
}

def translate_hindi_file(file_path):
    """Translate all remaining English content in Hindi file"""
    if not Path(file_path).exists():
        print(f"✗ File not found: {file_path}")
        return False
        
    content = Path(file_path).read_text(encoding='utf-8')
    
    # Apply all translations
    for en, hi in hindi_content.items():
        content = content.replace(en, hi)
    
    Path(file_path).write_text(content, encoding='utf-8')
    print(f"✓ Completed: {file_path}")
    return True

# Translate Hindi playlist page
print("Completing Hindi translations...")
translate_hindi_file('web/hi/youtube-playlist-downloader/index.html')

print("\n✅ Hindi content translation complete!")
print("\nNote: This is a sample for Hindi. Similar comprehensive translations")
print("need to be created for all other 16 languages.")
