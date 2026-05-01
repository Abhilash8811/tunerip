#!/usr/bin/env python3
from pathlib import Path
import re

files = [
    'web/ko/youtube-playlist-downloader/index.html',
    'web/ko/youtube-shorts-downloader/index.html',
    'web/ko/youtube-multi-downloader/index.html'
]

# Korean translations - comprehensive
ko = {
    'Save YouTube Shorts as MP3 audio or MP4 video in seconds. Original vertical aspect ratio preserved.': '몇 초 만에 YouTube Shorts를 MP3 오디오 또는 MP4 비디오로 저장하세요. 원본 세로 화면 비율이 유지됩니다.',
    'Download YouTube Shorts without an app': '앱 없이 YouTube Shorts 다운로드',
    'Shorts are just YouTube videos under a minute, so yt2mp3.lol handles them through the same pipeline as full-length clips. Paste a Shorts URL (anything matching youtube.com/shorts/…), pick MP3 or MP4, and the file is yours in seconds.': 'Shorts는 1분 미만의 YouTube 동영상이므로 yt2mp3.lol은 전체 길이 클립과 동일한 파이프라인을 통해 처리합니다. Shorts URL(youtube.com/shorts/…와 일치하는 모든 것)을 붙여넣고 MP3 또는 MP4를 선택하면 몇 초 안에 파일이 준비됩니다.',
    'Shorts keep their vertical framing': 'Shorts는 세로 프레임을 유지합니다',
    'We export MP4 in the original 9:16 portrait aspect ratio whenever the uploader filmed that way. Nothing is cropped, stretched, or re-centered, so the Short looks identical offline.': '업로더가 그렇게 촬영한 경우 원본 9:16 세로 화면 비율로 MP4를 내보냅니다. 자르거나 늘리거나 다시 중앙에 배치하지 않으므로 Short는 오프라인에서도 동일하게 보입니다.',
    'Grab the audio only': '오디오만 가져오기',
    'Some Shorts are just short songs, remixes, or memes — pick MP3 at 320 kbps and you get the audio without the video wrapper. Useful for making ringtones, memes, or sample libraries.': '일부 Shorts는 짧은 노래, 리믹스 또는 밈입니다. 320kbps에서 MP3를 선택하면 비디오 래퍼 없이 오디오를 얻을 수 있습니다. 벨소리, 밈 또는 샘플 라이브러리를 만드는 데 유용합니다.',
    'Download Shorts in Original 9:16 Format': '원본 9:16 형식으로 Shorts 다운로드',
    'YouTube Shorts are designed for vertical screens. Our converter detects Shorts URLs and ensures that the downloaded MP4 preserves the original 9:16 portrait aspect ratio. You get the exact video as it appears on your phone, without any ugly black bars or artificial cropping.': 'YouTube Shorts는 세로 화면용으로 설계되었습니다. 우리의 변환기는 Shorts URL을 감지하고 다운로드한 MP4가 원본 9:16 세로 화면 비율을 유지하도록 합니다. 추한 검은색 막대나 인위적인 자르기 없이 휴대폰에 나타나는 정확한 동영상을 얻을 수 있습니다.',
    'Extract Viral Audio with MP3': 'MP3로 바이럴 오디오 추출',
    'Often, the best part of a YouTube Short is the trending audio, meme sound, or background track. By selecting the MP3 option, you can rip just the audio track at a crisp 320kbps. This is perfect for creating your own ringtones, soundboards, or using the audio in your own TikToks and Reels.': '종종 YouTube Short의 가장 좋은 부분은 트렌딩 오디오, 밈 사운드 또는 배경 트랙입니다. MP3 옵션을 선택하면 선명한 320kbps로 오디오 트랙만 추출할 수 있습니다. 이것은 자신만의 벨소리, 사운드보드를 만들거나 자신의 TikTok 및 Reels에서 오디오를 사용하는 데 완벽합니다.',
    'No App Installation Necessary': '앱 설치 불필요',
    "Don't clutter your phone with shady downloader apps from the app store. Our YouTube Shorts 다운로더 works flawlessly via your mobile browser (Chrome, Safari, Firefox). Just use the 'Share' > 'Copy Link' feature in the YouTube app and paste it here.": "앱 스토어의 수상한 다운로더 앱으로 휴대폰을 어지럽히지 마세요. 우리의 YouTube Shorts 다운로더는 모바일 브라우저(Chrome, Safari, Firefox)를 통해 완벽하게 작동합니다. YouTube 앱에서 '공유' > '링크 복사' 기능을 사용하고 여기에 붙여넣기만 하면 됩니다.",
    'Ultra-Fast Processing for Short Clips': '짧은 클립을 위한 초고속 처리',
    'Because Shorts are under 60 seconds by definition, our backend processes them almost instantaneously. In most cases, your download link will be ready in under 3 seconds, allowing you to quickly save multiple Shorts in a row.': 'Shorts는 정의상 60초 미만이므로 백엔드가 거의 즉시 처리합니다. 대부분의 경우 다운로드 링크가 3초 이내에 준비되어 여러 Shorts를 연속으로 빠르게 저장할 수 있습니다.',
    'Bypass Content Restrictions': '콘텐츠 제한 우회',
    'Sometimes creators delete their viral Shorts, or the platform mutes the audio due to copyright disputes. By downloading the Short directly to your device, you secure a permanent offline copy that can never be altered or removed from your library.': '때때로 제작자가 바이럴 Shorts를 삭제하거나 플랫폼이 저작권 분쟁으로 인해 오디오를 음소거합니다. Short를 장치에 직접 다운로드하면 라이브러리에서 변경하거나 제거할 수 없는 영구 오프라인 사본을 확보할 수 있습니다.',
    'Perfect for Cross-Posting': '크로스 포스팅에 완벽',
    'Are you a social media manager or creator looking to cross-post your content? Download your own YouTube Shorts in pristine 1080p MP4 format and natively upload them to TikTok, Instagram Reels, or Snapchat Spotlight without watermarks.': '소셜 미디어 관리자 또는 콘텐츠를 크로스 포스팅하려는 제작자입니까? 자신의 YouTube Shorts를 깨끗한 1080p MP4 형식으로 다운로드하고 워터마크 없이 TikTok, Instagram Reels 또는 Snapchat Spotlight에 기본적으로 업로드하세요.',
    'Batch Download Shorts from Playlists': '재생목록에서 Shorts 일괄 다운로드',
    "If you've saved a bunch of funny Shorts to a public playlist, you don't have to download them one by one. Paste the playlist URL into our tool, and it will generate individual download links for every Short in the collection.": '재미있는 Shorts를 공개 재생목록에 저장한 경우 하나씩 다운로드할 필요가 없습니다. 재생목록 URL을 도구에 붙여넣으면 컬렉션의 모든 Short에 대한 개별 다운로드 링크가 생성됩니다.',
    'Seamless iOS and Android Integration': '원활한 iOS 및 Android 통합',
    "On iPhones, Safari will download the Short directly to your 'Files' app, from which you can easily save it to your Camera Roll. On Android, Chrome saves it straight to your 'Downloads' folder or Gallery for immediate viewing.": "iPhone에서 Safari는 Short를 '파일' 앱에 직접 다운로드하며, 여기에서 카메라 롤에 쉽게 저장할 수 있습니다. Android에서 Chrome은 즉시 보기 위해 '다운로드' 폴더 또는 갤러리에 직접 저장합니다.",
    'How to Download YouTube Shorts': 'YouTube Shorts 다운로드 방법',
    "1. Open the YouTube app and watch a Short. 2. Tap the 'Share' arrow and select 'Copy Link'. 3. Open your mobile browser and navigate to our site. 4. Paste the link into the input field. 5. Choose MP4 for video or MP3 for audio, then tap 'Convert'. 6. Tap 'Download' to save the file.": "1. YouTube 앱을 열고 Short를 시청합니다. 2. '공유' 화살표를 탭하고 '링크 복사'를 선택합니다. 3. 모바일 브라우저를 열고 사이트로 이동합니다. 4. 링크를 입력 필드에 붙여넣습니다. 5. 비디오의 경우 MP4를, 오디오의 경우 MP3를 선택한 다음 '변환'을 탭합니다. 6. '다운로드'를 탭하여 파일을 저장합니다.",
    "Can I download a channel's entire Shorts feed?": '채널의 전체 Shorts 피드를 다운로드할 수 있습니까?',
    'Yes, if you can create a playlist containing those Shorts. Paste the playlist URL and every video will be processed individually.': '예, 해당 Shorts가 포함된 재생목록을 만들 수 있는 경우입니다. 재생목록 URL을 붙여넣으면 모든 동영상이 개별적으로 처리됩니다.',
    'Why does my Short look blurry?': '내 Short가 흐릿하게 보이는 이유는 무엇입니까?',
    "Shorts are often uploaded at lower resolutions by creators. We pull the highest resolution available; if that's 720p, the download will reflect that.": '제작자가 Shorts를 낮은 해상도로 업로드하는 경우가 많습니다. 사용 가능한 최고 해상도를 가져옵니다. 720p인 경우 다운로드에 반영됩니다.',
    'What is the difference between a Short and a regular video?': 'Short와 일반 동영상의 차이점은 무엇입니까?',
    'Technically, very little. Shorts are just vertical videos (9:16 ratio) that are 60 seconds or less. Our system handles them using the same high-speed extraction engine as regular videos.': '기술적으로는 거의 없습니다. Shorts는 60초 이하의 세로 동영상(9:16 비율)입니다. 우리 시스템은 일반 동영상과 동일한 고속 추출 엔진을 사용하여 처리합니다.',
    'Will the downloaded Short have a YouTube watermark?': '다운로드한 Short에 YouTube 워터마크가 있습니까?',
    'No. Unlike some other platforms, YouTube does not embed a hardcoded watermark into the video file itself. Your downloaded MP4 will be clean and watermark-free.': '아니요. 다른 일부 플랫폼과 달리 YouTube는 비디오 파일 자체에 하드코딩된 워터마크를 포함하지 않습니다. 다운로드한 MP4는 깨끗하고 워터마크가 없습니다.',
    'Can I download Shorts in 4K?': 'Shorts를 4K로 다운로드할 수 있습니까?',
    'Most Shorts are uploaded at a maximum resolution of 1080p to optimize for mobile screens. If a creator managed to upload a 4K vertical video, our tool will capture it, but 1080p is the standard maximum.': '대부분의 Shorts는 모바일 화면에 최적화하기 위해 최대 1080p 해상도로 업로드됩니다. 제작자가 4K 세로 동영상을 업로드한 경우 도구가 캡처하지만 1080p가 표준 최대값입니다.',
    'How do I save the Short to my iPhone Camera Roll?': 'Short를 iPhone 카메라 롤에 저장하려면 어떻게 해야 합니까?',
    "After downloading the MP4 via Safari, open the 'Files' app, locate the video in your Downloads folder, tap the share icon, and select 'Save Video'.": "Safari를 통해 MP4를 다운로드한 후 '파일' 앱을 열고 다운로드 폴더에서 동영상을 찾아 공유 아이콘을 탭한 다음 '비디오 저장'을 선택합니다.",
    'Why did the MP3 extraction fail?': 'MP3 추출이 실패한 이유는 무엇입니까?',
    'This is extremely rare, but if a Short has been completely muted by YouTube due to copyright claims, there is no audio track for our servers to extract.': '이것은 매우 드물지만 저작권 주장으로 인해 YouTube에서 Short가 완전히 음소거된 경우 서버가 추출할 오디오 트랙이 없습니다.',
    'Is there a limit to how many Shorts I can download?': '다운로드할 수 있는 Shorts 수에 제한이 있습니까?',
    'No! You can download as many Shorts as you like. Our service is completely unlimited and free of charge.': '아니요! 원하는 만큼 Shorts를 다운로드할 수 있습니다. 우리 서비스는 완전히 무제한이며 무료입니다.',
    'Can I download unlisted Shorts?': '목록에 없는 Shorts를 다운로드할 수 있습니까?',
    'Yes, as long as you have the direct link to the unlisted Short, our tool can access and convert it. We cannot access Private Shorts.': '예, 목록에 없는 Short에 대한 직접 링크가 있는 한 도구가 액세스하고 변환할 수 있습니다. 비공개 Shorts에는 액세스할 수 없습니다.',
    'Does the tool work on desktop computers?': '이 도구는 데스크톱 컴퓨터에서 작동합니까?',
    'Absolutely. You can copy the URL of a Short from your desktop browser (e.g., youtube.com/shorts/...) and paste it into our tool just like any other link.': '물론입니다. 데스크톱 브라우저(예: youtube.com/shorts/...)에서 Short의 URL을 복사하여 다른 링크와 마찬가지로 도구에 붙여넣을 수 있습니다.',
    'What happens to the video thumbnail?': '비디오 썸네일은 어떻게 됩니까?',
    "For MP3 downloads, we embed the Short's thumbnail as the album artwork. For MP4 downloads, the video file itself contains the first frame as the poster image.": 'MP3 다운로드의 경우 Short의 썸네일을 앨범 아트워크로 포함합니다. MP4 다운로드의 경우 비디오 파일 자체에 첫 번째 프레임이 포스터 이미지로 포함됩니다.',
    'Are the downloads safe from viruses?': '다운로드가 바이러스로부터 안전합니까?',
    'Yes, the files are generated directly from YouTube\'s servers via FFmpeg muxing. We do not alter the files or inject malicious code.': '예, 파일은 FFmpeg 먹싱을 통해 YouTube 서버에서 직접 생성됩니다. 파일을 변경하거나 악성 코드를 주입하지 않습니다.',
    'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': '한 번에 여러 YouTube 동영상을 다운로드하세요. 여러 URL을 붙여넣고 한 번에 모두 변환하세요.',
}

for f in files:
    c = Path(f).read_text(encoding='utf-8')
    for e, k in ko.items():
        c = c.replace(e, k)
    Path(f).write_text(c, encoding='utf-8')
    print(f"✓ {f}")

print("\n✅ Korean (ko) complete - 3/3")
