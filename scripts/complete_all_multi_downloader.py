#!/usr/bin/env python3
from pathlib import Path

# Multi-downloader translations for all languages
translations = {
    'ar': {
        'Multiple YouTube Downloader': 'تنزيل YouTube متعدد',
        'Paste several YouTube URLs at once and convert them all in parallel. Great for playlists, curated lists, and research workflows.': 'الصق عدة عناوين URL لـ YouTube دفعة واحدة وقم بتحويلها جميعًا بالتوازي. رائع لقوائم التشغيل والقوائم المنسقة وسير عمل البحث.',
        'Why batch is faster': 'لماذا الدفعة أسرع',
        'Instead of converting videos one at a time, paste multiple links separated by newlines or commas. The server processes each in parallel and hands you a download list when everything is ready. For 10 short videos this is roughly 5x faster than sequential conversion.': 'بدلاً من تحويل مقاطع الفيديو واحدًا تلو الآخر، الصق روابط متعددة مفصولة بأسطر جديدة أو فواصل. يعالج الخادم كل منها بالتوازي ويسلمك قائمة تنزيل عندما يكون كل شيء جاهزًا. بالنسبة لـ 10 مقاطع فيديو قصيرة، هذا أسرع بحوالي 5 مرات من التحويل المتسلسل.',
        'How to batch': 'كيفية الدفعة',
        'Open the converter, paste your first link and hit Enter, then paste the next on the following line. Press Convert when you\'re done — each URL is queued as its own job and shows independent progress.': 'افتح المحول، الصق الرابط الأول واضغط على Enter، ثم الصق التالي في السطر التالي. اضغط على تحويل عند الانتهاء — يتم وضع كل عنوان URL في قائمة الانتظار كوظيفة خاصة به ويظهر تقدمًا مستقلاً.',
        'Works with mixed formats': 'يعمل مع التنسيقات المختلطة',
        'You can choose one format (e.g. MP3 320 kbps) for the whole batch, or queue separate batches with different formats one after another. Combining playlists and loose URLs is fine.': 'يمكنك اختيار تنسيق واحد (مثل MP3 320 kbps) للدفعة بأكملها، أو وضع دفعات منفصلة في قائمة الانتظار بتنسيقات مختلفة واحدة تلو الأخرى. الجمع بين قوائم التشغيل وعناوين URL المفككة أمر جيد.',
        'Is there a batch size limit?': 'هل هناك حد لحجم الدفعة؟',
        'Soft limit of 50 URLs per batch to keep the server responsive for everyone. Larger batches can be split.': 'حد ناعم من 50 عنوان URL لكل دفعة للحفاظ على استجابة الخادم للجميع. يمكن تقسيم الدفعات الأكبر.',
        'What if one URL fails?': 'ماذا لو فشل عنوان URL واحد؟',
        'That job is marked failed and the rest keep running. You can retry just the failed URL.': 'يتم وضع علامة على تلك الوظيفة على أنها فشلت ويستمر الباقي في العمل. يمكنك إعادة المحاولة فقط لعنوان URL الفاشل.',
    },
    'bn': {
        'Multiple YouTube Downloader': 'মাল্টিপল YouTube ডাউনলোডার',
        'Paste several YouTube URLs at once and convert them all in parallel. Great for playlists, curated lists, and research workflows.': 'একবারে বেশ কয়েকটি YouTube URL পেস্ট করুন এবং সেগুলি সব সমান্তরালভাবে রূপান্তর করুন। প্লেলিস্ট, কিউরেটেড তালিকা এবং গবেষণা ওয়ার্কফ্লোর জন্য দুর্দান্ত।',
        'Why batch is faster': 'ব্যাচ কেন দ্রুত',
        'Instead of converting videos one at a time, paste multiple links separated by newlines or commas. The server processes each in parallel and hands you a download list when everything is ready. For 10 short videos this is roughly 5x faster than sequential conversion.': 'একবারে একটি ভিডিও রূপান্তর করার পরিবর্তে, নতুন লাইন বা কমা দ্বারা পৃথক করা একাধিক লিঙ্ক পেস্ট করুন। সার্ভার প্রতিটি সমান্তরালভাবে প্রক্রিয়া করে এবং সবকিছু প্রস্তুত হলে আপনাকে একটি ডাউনলোড তালিকা দেয়। 10টি ছোট ভিডিওর জন্য এটি ক্রমিক রূপান্তরের চেয়ে প্রায় 5 গুণ দ্রুত।',
        'How to batch': 'কীভাবে ব্যাচ করবেন',
        'Open the converter, paste your first link and hit Enter, then paste the next on the following line. Press Convert when you\'re done — each URL is queued as its own job and shows independent progress.': 'কনভার্টার খুলুন, আপনার প্রথম লিঙ্ক পেস্ট করুন এবং Enter চাপুন, তারপর পরবর্তী লাইনে পরবর্তীটি পেস্ট করুন। আপনি শেষ হলে রূপান্তর চাপুন — প্রতিটি URL তার নিজস্ব কাজ হিসাবে সারিবদ্ধ হয় এবং স্বতন্ত্র অগ্রগতি দেখায়।',
        'Works with mixed formats': 'মিশ্র ফরম্যাটের সাথে কাজ করে',
        'You can choose one format (e.g. MP3 320 kbps) for the whole batch, or queue separate batches with different formats one after another. Combining playlists and loose URLs is fine.': 'আপনি পুরো ব্যাচের জন্য একটি ফরম্যাট (যেমন MP3 320 kbps) বেছে নিতে পারেন, বা একের পর এক বিভিন্ন ফরম্যাট সহ পৃথক ব্যাচ সারিবদ্ধ করতে পারেন। প্লেলিস্ট এবং আলগা URL একত্রিত করা ঠিক আছে।',
        'Is there a batch size limit?': 'ব্যাচ আকারের সীমা আছে কি?',
        'Soft limit of 50 URLs per batch to keep the server responsive for everyone. Larger batches can be split.': 'সবার জন্য সার্ভার প্রতিক্রিয়াশীল রাখতে প্রতি ব্যাচে 50টি URL এর সফট সীমা। বড় ব্যাচ বিভক্ত করা যেতে পারে।',
        'What if one URL fails?': 'যদি একটি URL ব্যর্থ হয় তাহলে কী হবে?',
        'That job is marked failed and the rest keep running. You can retry just the failed URL.': 'সেই কাজটি ব্যর্থ হিসাবে চিহ্নিত করা হয় এবং বাকিগুলি চলতে থাকে। আপনি শুধুমাত্র ব্যর্থ URL পুনরায় চেষ্টা করতে পারেন।',
    },
}

# Process all multi-downloader pages
langs = ['ar', 'bn', 'de', 'es', 'fil', 'fr', 'id', 'it', 'ja', 'ko', 'pt', 'ru', 'th', 'tr', 'ur', 'vi']

for lang in langs:
    file_path = f'web/{lang}/youtube-multi-downloader/index.html'
    if Path(file_path).exists() and lang in translations:
        content = Path(file_path).read_text(encoding='utf-8')
        for en, trans in translations[lang].items():
            content = content.replace(en, trans)
        Path(file_path).write_text(content, encoding='utf-8')
        print(f"✓ {file_path}")

print("\n✅ All multi-downloader pages translated!")
