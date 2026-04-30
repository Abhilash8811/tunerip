#!/usr/bin/env python3
"""Complete Arabic (ar) - all 3 pages"""
from pathlib import Path

arabic_translations = {
    # Table
    'Format': 'التنسيق',
    'Best For': 'الأفضل لـ',
    'Quality Options': 'خيارات الجودة',
    'File Size': 'حجم الملف',
    'Universal audio playback': 'تشغيل صوتي عالمي',
    'Small': 'صغير',
    'Video playback everywhere': 'تشغيل الفيديو في كل مكان',
    'Large': 'كبير',
    'Lossless audio editing': 'تحرير صوتي بدون فقدان',
    'Very Large': 'كبير جداً',
    'Apple devices': 'أجهزة Apple',
    'Native AAC': 'AAC أصلي',
    'Medium': 'متوسط',
    
    # Headings
    'Batch Conversion Masterclass': 'دورة تحويل الدفعات',
    'Preserve Original Order and Titles': 'الحفاظ على الترتيب والعناوين الأصلية',
    'Flexible Format Selection for Playlists': 'اختيار تنسيق مرن لقوائم التشغيل',
    'High-Concurrency Processing': 'معالجة عالية التزامن',
    'Support for Massive Playlists': 'دعم قوائم التشغيل الضخمة',
    'Download Auto-Generated Mixes': 'تنزيل المزيجات التلقائية',
    'Ideal for Educators and Students': 'مثالي للمعلمين والطلاب',
    'Handling Unavailable or Private Videos': 'التعامل مع مقاطع الفيديو غير المتاحة أو الخاصة',
    'How to Download a Full Playlist': 'كيفية تنزيل قائمة تشغيل كاملة',
    
    # Paragraphs
    'Downloading videos one by one is incredibly tedious. Our YouTube Playlist Downloader is engineered for bulk operations. By parsing the playlist metadata, our servers generate individual conversion jobs for every single video in the list, allowing you to download an entire album, lecture series, or podcast backlog with minimal effort.': 'تنزيل مقاطع الفيديو واحدة تلو الأخرى أمر ممل للغاية. تم تصميم أداة تنزيل قوائم تشغيل YouTube الخاصة بنا للعمليات المجمعة. من خلال تحليل البيانات الوصفية لقائمة التشغيل، تقوم خوادمنا بإنشاء مهام تحويل فردية لكل فيديو في القائمة، مما يتيح لك تنزيل ألبوم كامل أو سلسلة محاضرات أو أرشيف بودكاست بأقل جهد.',
    
    'When you download a playlist, organization is key. Our system automatically grabs the original video titles and structures the downloads so you can easily maintain the intended order. This is perfect for sequential tutorials, multi-part documentaries, or chronologically ordered music albums.': 'عند تنزيل قائمة تشغيل، التنظيم هو المفتاح. يقوم نظامنا تلقائياً بالحصول على عناوين الفيديو الأصلية وتنظيم التنزيلات حتى تتمكن من الحفاظ بسهولة على الترتيب المقصود. هذا مثالي للدروس المتسلسلة أو الأفلام الوثائقية متعددة الأجزاء أو ألبومات الموسيقى المرتبة زمنياً.',
    
    "You aren't locked into a single format. You can choose to download an entire music playlist as crisp 320kbps MP3s, or an entire educational course as 1080p MP4s. Our FFmpeg backend applies your selected format uniformly across all items in the batch.": 'أنت لست مقيداً بتنسيق واحد. يمكنك اختيار تنزيل قائمة تشغيل موسيقية كاملة بصيغة MP3 بجودة 320kbps، أو دورة تعليمية كاملة بصيغة MP4 بدقة 1080p. يطبق نظام FFmpeg الخلفي لدينا التنسيق المحدد بشكل موحد عبر جميع العناصر في الدفعة.',
    
    "We don't make you wait for one video to finish before starting the next. Our cloud infrastructure utilizes high-concurrency processing, meaning multiple videos from your playlist are downloaded and converted simultaneously. A 50-video playlist is processed significantly faster than doing it manually.": 'نحن لا نجعلك تنتظر انتهاء فيديو واحد قبل بدء التالي. تستخدم بنيتنا التحتية السحابية معالجة عالية التزامن، مما يعني أن مقاطع فيديو متعددة من قائمة التشغيل الخاصة بك يتم تنزيلها وتحويلها في وقت واحد. تتم معالجة قائمة تشغيل مكونة من 50 فيديو بشكل أسرع بكثير من القيام بذلك يدوياً.',
    
    "Whether it's a 10-track EP or a massive 300-video mega-mix, our tool is built to handle it. While extremely large playlists may take a few minutes to fully parse and render download buttons, our backend will not time out or crash during the operation.": 'سواء كان EP مكوناً من 10 مقاطع أو مزيج ضخم من 300 فيديو، فإن أداتنا مصممة للتعامل معه. بينما قد تستغرق قوائم التشغيل الكبيرة جداً بضع دقائق للتحليل الكامل وعرض أزرار التنزيل، فإن نظامنا الخلفي لن ينتهي وقته أو يتعطل أثناء العملية.',
    
    "Did YouTube's algorithm create the perfect 'My Mix' or 'Discover Weekly' equivalent for you? Just copy the URL of that auto-generated playlist and paste it here. You can rip the entire curated mix to your local device for offline listening on road trips or flights.": "هل أنشأت خوارزمية YouTube مزيج 'My Mix' أو 'Discover Weekly' المثالي لك؟ فقط انسخ عنوان URL لقائمة التشغيل التي تم إنشاؤها تلقائياً والصقه هنا. يمكنك نسخ المزيج المنسق بالكامل إلى جهازك المحلي للاستماع دون اتصال في رحلات الطريق أو الرحلات الجوية.",
    
    'Many professors and online instructors organize their course modules into public YouTube playlists. Students can use our tool to download the entire semester\'s worth of lectures in MP4 format, ensuring they have access to study materials even without an internet connection.': 'ينظم العديد من الأساتذة والمدربين عبر الإنترنت وحدات دوراتهم في قوائم تشغيل YouTube عامة. يمكن للطلاب استخدام أداتنا لتنزيل محاضرات الفصل الدراسي بأكمله بتنسيق MP4، مما يضمن وصولهم إلى المواد الدراسية حتى بدون اتصال بالإنترنت.',
    
    "Playlists often contain videos that have been deleted, made private, or restricted in your region. Our parser intelligently skips these dead links and continues processing the available videos, so your batch download isn't ruined by a single broken link.": 'غالباً ما تحتوي قوائم التشغيل على مقاطع فيديو تم حذفها أو جعلها خاصة أو مقيدة في منطقتك. يتخطى محللنا بذكاء هذه الروابط الميتة ويستمر في معالجة مقاطع الفيديو المتاحة، لذلك لن يتم إفساد تنزيل الدفعة الخاص بك برابط واحد معطل.',
    
    "1. Navigate to the playlist on YouTube. Ensure the URL contains 'list=' (e.g., youtube.com/playlist?list=...). 2. Copy the URL. 3. Paste it into our converter. 4. Select your global format (MP3 or MP4). 5. Click Convert. 6. Wait for the parser to extract the videos, then click the individual download buttons as they appear.": "1. انتقل إلى قائمة التشغيل على YouTube. تأكد من أن عنوان URL يحتوي على 'list=' (مثل youtube.com/playlist?list=...). 2. انسخ عنوان URL. 3. الصقه في المحول الخاص بنا. 4. حدد التنسيق العام (MP3 أو MP4). 5. انقر فوق تحويل. 6. انتظر حتى يستخرج المحلل مقاطع الفيديو، ثم انقر فوق أزرار التنزيل الفردية عند ظهورها.",
    
    # FAQ
    'Is there a maximum playlist length?': 'هل يوجد حد أقصى لطول قائمة التشغيل؟',
    'Are playlists downloaded in order?': 'هل يتم تنزيل قوائم التشغيل بالترتيب؟',
    'Is there a limit to the number of videos in a playlist?': 'هل يوجد حد لعدد مقاطع الفيديو في قائمة التشغيل؟',
    'Will it download as one giant file or separate files?': 'هل سيتم التنزيل كملف واحد ضخم أم ملفات منفصلة؟',
    "Can I download a 'Watch Later' playlist?": "هل يمكنني تنزيل قائمة تشغيل 'شاهد لاحقاً'؟",
    'What happens if the playlist contains a live stream?': 'ماذا يحدث إذا كانت قائمة التشغيل تحتوي على بث مباشر؟',
    'How long does a 50-video playlist take to convert?': 'كم من الوقت تستغرق قائمة تشغيل مكونة من 50 فيديو للتحويل؟',
    'Do I have to click download 50 times?': 'هل يجب علي النقر فوق تنزيل 50 مرة؟',
    'Does it download the playlist thumbnail?': 'هل يقوم بتنزيل صورة مصغرة لقائمة التشغيل؟',
    "Can I download a channel's entire video list?": 'هل يمكنني تنزيل قائمة الفيديو الكاملة للقناة؟',
    'Are the files numbered?': 'هل الملفات مرقمة؟',
    'Why did only half the videos appear?': 'لماذا ظهر نصف مقاطع الفيديو فقط؟',
    
    'No hard cap, but very large playlists (500+ videos) may take several minutes to process in full.': 'لا يوجد حد صارم، ولكن قوائم التشغيل الكبيرة جداً (500+ فيديو) قد تستغرق عدة دقائق للمعالجة الكاملة.',
    'Yes. Original playlist ordering is preserved by default.': 'نعم. يتم الحفاظ على ترتيب قائمة التشغيل الأصلية افتراضياً.',
    'We can theoretically parse playlists of any size, but for optimal performance and browser stability, we recommend downloading playlists with 200 videos or fewer at a time.': 'يمكننا نظرياً تحليل قوائم تشغيل بأي حجم، ولكن للحصول على أداء مثالي واستقرار المتصفح، نوصي بتنزيل قوائم تشغيل تحتوي على 200 فيديو أو أقل في المرة الواحدة.',
    'Each video in the playlist is converted and downloaded as its own separate file. We do not merge them into a single massive audio/video file.': 'يتم تحويل كل فيديو في قائمة التشغيل وتنزيله كملف منفصل خاص به. نحن لا ندمجها في ملف صوتي/فيديو واحد ضخم.',
    "Your 'Watch Later' playlist is private to your account. Our servers cannot access it. You would need to move those videos to a Public or Unlisted playlist first.": "قائمة تشغيل 'شاهد لاحقاً' الخاصة بك خاصة بحسابك. لا يمكن لخوادمنا الوصول إليها. ستحتاج إلى نقل تلك مقاطع الفيديو إلى قائمة تشغيل عامة أو غير مدرجة أولاً.",
    'If the live stream has ended and is available as a VOD, it will download normally. If the stream is currently live, the tool will skip it, as it has no finite length.': 'إذا انتهى البث المباشر وكان متاحاً كـ VOD، فسيتم تنزيله بشكل طبيعي. إذا كان البث مباشراً حالياً، فستتخطاه الأداة، حيث ليس له طول محدد.',
    'Parsing the list takes only seconds. The conversion time depends on the total length of the videos and the chosen quality, but our concurrent processing usually finishes a typical music playlist in under 3 minutes.': 'يستغرق تحليل القائمة ثوانٍ فقط. يعتمد وقت التحويل على الطول الإجمالي لمقاطع الفيديو والجودة المختارة، ولكن معالجتنا المتزامنة عادة ما تنهي قائمة تشغيل موسيقية نموذجية في أقل من 3 دقائق.',
    'Currently, browser security restrictions prevent websites from automatically triggering 50 file downloads at once. You will need to click the download button for each generated file.': 'حالياً، تمنع قيود أمان المتصفح مواقع الويب من تشغيل 50 تنزيل ملف تلقائياً في وقت واحد. ستحتاج إلى النقر فوق زر التنزيل لكل ملف تم إنشاؤه.',
    'The individual video files will have their respective video thumbnails embedded as metadata (for audio formats) or as the poster frame (for video formats).': 'ستحتوي ملفات الفيديو الفردية على صورها المصغرة المضمنة كبيانات وصفية (لتنسيقات الصوت) أو كإطار ملصق (لتنسيقات الفيديو).',
    "If the channel has a 'Play All' button or a playlist containing all their uploads, yes. Just copy that specific playlist URL.": "إذا كانت القناة تحتوي على زر 'تشغيل الكل' أو قائمة تشغيل تحتوي على جميع تحميلاتهم، نعم. فقط انسخ عنوان URL لقائمة التشغيل المحددة.",
    "The files retain their original YouTube titles. If the creator numbered the titles (e.g., 'Episode 1: ...'), that numbering will be in your downloaded file.": "تحتفظ الملفات بعناوين YouTube الأصلية. إذا قام المنشئ بترقيم العناوين (مثل 'الحلقة 1: ...')، فسيكون هذا الترقيم في ملفك الذي تم تنزيله.",
    'This usually means the missing videos are either Private, Deleted, or Region-Blocked. Our tool can only fetch publicly accessible media.': 'هذا يعني عادة أن مقاطع الفيديو المفقودة إما خاصة أو محذوفة أو محظورة إقليمياً. يمكن لأداتنا فقط جلب الوسائط المتاحة للعامة.',
    
    # Shorts/Multi specific
    'YouTube Shorts Downloader': 'تنزيل YouTube Shorts',
    'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'قم بتنزيل مقاطع فيديو YouTube Shorts بتنسيق MP3 أو MP4. سريع ومجاني وسهل الاستخدام.',
    'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter, تنزيل يوتيوب شورتس, شورتس إلى mp3',
    'YouTube Multi Downloader': 'تنزيل متعدد من YouTube',
    'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': 'قم بتنزيل مقاطع فيديو YouTube متعددة دفعة واحدة. الصق عدة عناوين URL وقم بتحويلها جميعاً دفعة واحدة.',
    'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download, تنزيل متعدد يوتيوب, تنزيل جماعي',
}

def translate(file_path):
    content = Path(file_path).read_text(encoding='utf-8')
    for en, ar in arabic_translations.items():
        content = content.replace(en, ar)
    Path(file_path).write_text(content, encoding='utf-8')
    print(f"✓ {file_path}")

translate('web/ar/youtube-playlist-downloader/index.html')
translate('web/ar/youtube-shorts-downloader/index.html')
translate('web/ar/youtube-multi-downloader/index.html')
print("\n✅ Arabic (ar) complete - 3/3 pages")
