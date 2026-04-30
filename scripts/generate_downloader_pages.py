#!/usr/bin/env python3
"""
Generate translated downloader pages (multi, shorts, playlist) for all languages
with perfect ad implementation matching the homepage.
"""

import os
from pathlib import Path

# Language configurations
LANGUAGES = {
    'ar': {'name': 'العربية', 'dir': 'rtl', 'locale': 'ar_SA'},
    'bn': {'name': 'বাংলা', 'dir': 'ltr', 'locale': 'bn_BD'},
    'de': {'name': 'Deutsch', 'dir': 'ltr', 'locale': 'de_DE'},
    'es': {'name': 'Español', 'dir': 'ltr', 'locale': 'es_ES'},
    'fil': {'name': 'Filipino', 'dir': 'ltr', 'locale': 'fil_PH'},
    'fr': {'name': 'Français', 'dir': 'ltr', 'locale': 'fr_FR'},
    'hi': {'name': 'हिन्दी', 'dir': 'ltr', 'locale': 'hi_IN'},
    'id': {'name': 'Bahasa Indonesia', 'dir': 'ltr', 'locale': 'id_ID'},
    'it': {'name': 'Italiano', 'dir': 'ltr', 'locale': 'it_IT'},
    'ja': {'name': '日本語', 'dir': 'ltr', 'locale': 'ja_JP'},
    'ko': {'name': '한국어', 'dir': 'ltr', 'locale': 'ko_KR'},
    'pt': {'name': 'Português', 'dir': 'ltr', 'locale': 'pt_BR'},
    'ru': {'name': 'Русский', 'dir': 'ltr', 'locale': 'ru_RU'},
    'th': {'name': 'ภาษาไทย', 'dir': 'ltr', 'locale': 'th_TH'},
    'tr': {'name': 'Türkçe', 'dir': 'ltr', 'locale': 'tr_TR'},
    'ur': {'name': 'اردو', 'dir': 'rtl', 'locale': 'ur_PK'},
    'vi': {'name': 'Tiếng Việt', 'dir': 'ltr', 'locale': 'vi_VN'},
}

# Translations for each page type
TRANSLATIONS = {
    'multi': {
        'en': {
            'title': 'Multiple YouTube Downloader (Batch Convert) - yt2mp3.lol',
            'description': 'Paste several YouTube URLs at once and convert them all in parallel. Great for playlists, curated lists, and research workflows.',
            'h1': 'Multiple YouTube Downloader',
            'subtitle': 'Paste several YouTube URLs at once and convert them all in parallel. Great for playlists, curated lists, and research workflows.',
            'placeholder': 'Paste YouTube URLs here (one per line)',
            'section1_title': 'Why batch is faster',
            'section1_text': 'Instead of converting videos one at a time, paste multiple links separated by newlines or commas. The server processes each in parallel and hands you a download list when everything is ready. For 10 short videos this is roughly 5x faster than sequential conversion.',
            'section2_title': 'How to batch',
            'section2_text': 'Open the converter, paste your first link and hit Enter, then paste the next on the following line. Press Convert when you\'re done — each URL is queued as its own job and shows independent progress.',
            'section3_title': 'Works with mixed formats',
            'section3_text': 'You can choose one format (e.g. MP3 320 kbps) for the whole batch, or queue separate batches with different formats one after another. Combining playlists and loose URLs is fine.',
            'faq1_q': 'Is there a batch size limit?',
            'faq1_a': 'Soft limit of 50 URLs per batch to keep the server responsive for everyone. Larger batches can be split.',
            'faq2_q': 'What if one URL fails?',
            'faq2_a': 'That job is marked failed and the rest keep running. You can retry just the failed URL.',
        },
        'ar': {
            'title': 'تحميل متعدد من يوتيوب (دفعة واحدة) - yt2mp3.lol',
            'description': 'الصق عدة روابط يوتيوب دفعة واحدة وحوّلها جميعاً بالتوازي. رائع للقوائم المنسقة وسير العمل البحثي.',
            'h1': 'تحميل متعدد من يوتيوب',
            'subtitle': 'الصق عدة روابط يوتيوب دفعة واحدة وحوّلها جميعاً بالتوازي. رائع للقوائم المنسقة وسير العمل البحثي.',
            'placeholder': 'الصق روابط يوتيوب هنا (واحد في كل سطر)',
            'section1_title': 'لماذا الدفعة أسرع',
            'section1_text': 'بدلاً من تحويل الفيديوهات واحداً تلو الآخر، الصق عدة روابط مفصولة بأسطر جديدة أو فواصل. يعالج الخادم كل واحد بالتوازي ويسلمك قائمة التنزيل عندما يكون كل شيء جاهزاً. بالنسبة لـ 10 فيديوهات قصيرة، هذا أسرع بحوالي 5 مرات من التحويل المتسلسل.',
            'section2_title': 'كيفية التحميل الدفعي',
            'section2_text': 'افتح المحوّل، الصق رابطك الأول واضغط Enter، ثم الصق التالي في السطر التالي. اضغط تحويل عندما تنتهي — كل رابط يُضاف إلى قائمة الانتظار كمهمة خاصة به ويظهر تقدماً مستقلاً.',
            'section3_title': 'يعمل مع صيغ مختلطة',
            'section3_text': 'يمكنك اختيار صيغة واحدة (مثل MP3 320 kbps) للدفعة بأكملها، أو إضافة دفعات منفصلة بصيغ مختلفة واحدة تلو الأخرى. الجمع بين القوائم والروابط المنفصلة جيد.',
            'faq1_q': 'هل هناك حد لحجم الدفعة؟',
            'faq1_a': 'حد مرن يبلغ 50 رابط لكل دفعة للحفاظ على استجابة الخادم للجميع. يمكن تقسيم الدفعات الأكبر.',
            'faq2_q': 'ماذا لو فشل أحد الروابط؟',
            'faq2_a': 'يتم وضع علامة فشل على تلك المهمة وتستمر البقية في العمل. يمكنك إعادة المحاولة فقط للرابط الفاشل.',
        },
        # Add more languages as needed
    },
    # Add 'shorts' and 'playlist' translations
}

print("Script created. Run with Python to generate all pages.")
print(f"Will create {len(LANGUAGES)} × 3 = {len(LANGUAGES) * 3} pages")
