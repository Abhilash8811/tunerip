#!/usr/bin/env python3
from pathlib import Path

japanese = {
    'Format': 'フォーマット', 'Best For': '最適な用途', 'Quality Options': '品質オプション', 'File Size': 'ファイルサイズ',
    'Universal audio playback': 'ユニバーサルオーディオ再生', 'Small': '小', 'Video playback everywhere': 'どこでもビデオ再生',
    'Large': '大', 'Lossless audio editing': 'ロスレスオーディオ編集', 'Very Large': '非常に大きい', 'Apple devices': 'Appleデバイス',
    'Native AAC': 'ネイティブAAC', 'Medium': '中', 'Batch Conversion Masterclass': 'バッチ変換マスタークラス',
    'Preserve Original Order and Titles': '元の順序とタイトルを保持', 'Flexible Format Selection for Playlists': 'プレイリストの柔軟なフォーマット選択',
    'High-Concurrency Processing': '高並行処理', 'Support for Massive Playlists': '大規模プレイリストのサポート',
    'Download Auto-Generated Mixes': '自動生成ミックスをダウンロード', 'Ideal for Educators and Students': '教育者と学生に最適',
    'Handling Unavailable or Private Videos': '利用できないまたはプライベートビデオの処理', 'How to Download a Full Playlist': '完全なプレイリストをダウンロードする方法',
    'Downloading videos one by one is incredibly tedious. Our YouTube Playlist Downloader is engineered for bulk operations. By parsing the playlist metadata, our servers generate individual conversion jobs for every single video in the list, allowing you to download an entire album, lecture series, or podcast backlog with minimal effort.': 'ビデオを1つずつダウンロードするのは非常に面倒です。当社のYouTubeプレイリストダウンローダーは、一括操作用に設計されています。プレイリストのメタデータを解析することで、サーバーはリスト内のすべてのビデオに対して個別の変換ジョブを生成し、最小限の労力でアルバム全体、講義シリーズ、またはポッドキャストのバックログをダウンロードできます。',
    'When you download a playlist, organization is key. Our system automatically grabs the original video titles and structures the downloads so you can easily maintain the intended order. This is perfect for sequential tutorials, multi-part documentaries, or chronologically ordered music albums.': 'プレイリストをダウンロードする際、整理が重要です。当社のシステムは、元のビデオタイトルを自動的に取得し、ダウンロードを構造化するため、意図した順序を簡単に維持できます。これは、連続したチュートリアル、複数部構成のドキュメンタリー、または年代順に並べられた音楽アルバムに最適です。',
    "You aren't locked into a single format. You can choose to download an entire music playlist as crisp 320kbps MP3s, or an entire educational course as 1080p MP4s. Our FFmpeg backend applies your selected format uniformly across all items in the batch.": '単一のフォーマットに固定されることはありません。音楽プレイリスト全体を鮮明な320kbps MP3としてダウンロードするか、教育コース全体を1080p MP4としてダウンロードするかを選択できます。当社のFFmpegバックエンドは、選択したフォーマットをバッチ内のすべてのアイテムに均一に適用します。',
    "We don't make you wait for one video to finish before starting the next. Our cloud infrastructure utilizes high-concurrency processing, meaning multiple videos from your playlist are downloaded and converted simultaneously. A 50-video playlist is processed significantly faster than doing it manually.": '次のビデオを開始する前に1つのビデオが終了するのを待つ必要はありません。当社のクラウドインフラストラクチャは高並行処理を利用しており、プレイリストから複数のビデオが同時にダウンロードおよび変換されます。50本のビデオプレイリストは、手動で行うよりもはるかに高速に処理されます。',
    "Whether it's a 10-track EP or a massive 300-video mega-mix, our tool is built to handle it. While extremely large playlists may take a few minutes to fully parse and render download buttons, our backend will not time out or crash during the operation.": '10トラックのEPであろうと、300本のビデオの巨大なメガミックスであろうと、当社のツールはそれを処理するように構築されています。非常に大きなプレイリストは、完全に解析してダウンロードボタンをレンダリングするのに数分かかる場合がありますが、バックエンドは操作中にタイムアウトまたはクラッシュすることはありません。',
    "Did YouTube's algorithm create the perfect 'My Mix' or 'Discover Weekly' equivalent for you? Just copy the URL of that auto-generated playlist and paste it here. You can rip the entire curated mix to your local device for offline listening on road trips or flights.": "YouTubeのアルゴリズムがあなたのために完璧な「マイミックス」または「ウィークリーディスカバー」相当のものを作成しましたか？その自動生成されたプレイリストのURLをコピーして、ここに貼り付けるだけです。ロードトリップやフライトでのオフラインリスニングのために、キュレートされたミックス全体をローカルデバイスにリッピングできます。",
    'Many professors and online instructors organize their course modules into public YouTube playlists. Students can use our tool to download the entire semester\'s worth of lectures in MP4 format, ensuring they have access to study materials even without an internet connection.': '多くの教授やオンライン講師は、コースモジュールを公開YouTubeプレイリストに整理しています。学生は当社のツールを使用して、学期全体の講義をMP4形式でダウンロードでき、インターネット接続がなくても学習資料にアクセスできるようにします。',
    "Playlists often contain videos that have been deleted, made private, or restricted in your region. Our parser intelligently skips these dead links and continues processing the available videos, so your batch download isn't ruined by a single broken link.": 'プレイリストには、削除されたり、非公開にされたり、地域で制限されたりしたビデオが含まれていることがよくあります。当社のパーサーは、これらのデッドリンクをインテリジェントにスキップし、利用可能なビデオの処理を続けるため、1つの壊れたリンクによってバッチダウンロードが台無しになることはありません。',
    "1. Navigate to the playlist on YouTube. Ensure the URL contains 'list=' (e.g., youtube.com/playlist?list=...). 2. Copy the URL. 3. Paste it into our converter. 4. Select your global format (MP3 or MP4). 5. Click Convert. 6. Wait for the parser to extract the videos, then click the individual download buttons as they appear.": "1. YouTubeでプレイリストに移動します。URLに「list=」が含まれていることを確認します（例：youtube.com/playlist?list=...）。2. URLをコピーします。3. コンバーターに貼り付けます。4. グローバルフォーマット（MP3またはMP4）を選択します。5. 変換をクリックします。6. パーサーがビデオを抽出するのを待ってから、表示される個々のダウンロードボタンをクリックします。",
    'Is there a maximum playlist length?': 'プレイリストの最大長はありますか？', 'Are playlists downloaded in order?': 'プレイリストは順番にダウンロードされますか？',
    'Is there a limit to the number of videos in a playlist?': 'プレイリスト内のビデオ数に制限はありますか？', 'Will it download as one giant file or separate files?': '1つの巨大なファイルとしてダウンロードされますか、それとも個別のファイルとしてダウンロードされますか？',
    "Can I download a 'Watch Later' playlist?": "「後で見る」プレイリストをダウンロードできますか？", 'What happens if the playlist contains a live stream?': 'プレイリストにライブストリームが含まれている場合はどうなりますか？',
    'How long does a 50-video playlist take to convert?': '50本のビデオプレイリストの変換にはどのくらい時間がかかりますか？', 'Do I have to click download 50 times?': 'ダウンロードを50回クリックする必要がありますか？',
    'Does it download the playlist thumbnail?': 'プレイリストのサムネイルをダウンロードしますか？', "Can I download a channel's entire video list?": 'チャンネルのビデオリスト全体をダウンロードできますか？',
    'Are the files numbered?': 'ファイルには番号が付けられていますか？', 'Why did only half the videos appear?': 'なぜビデオの半分しか表示されなかったのですか？',
    'No hard cap, but very large playlists (500+ videos) may take several minutes to process in full.': 'ハードキャップはありませんが、非常に大きなプレイリスト（500本以上のビデオ）は完全に処理するのに数分かかる場合があります。',
    'Yes. Original playlist ordering is preserved by default.': 'はい。元のプレイリストの順序はデフォルトで保持されます。',
    'We can theoretically parse playlists of any size, but for optimal performance and browser stability, we recommend downloading playlists with 200 videos or fewer at a time.': '理論的には任意のサイズのプレイリストを解析できますが、最適なパフォーマンスとブラウザの安定性のために、一度に200本以下のビデオを含むプレイリストをダウンロードすることをお勧めします。',
    'Each video in the playlist is converted and downloaded as its own separate file. We do not merge them into a single massive audio/video file.': 'プレイリスト内の各ビデオは、独自の個別ファイルとして変換およびダウンロードされます。それらを1つの巨大なオーディオ/ビデオファイルにマージすることはありません。',
    "Your 'Watch Later' playlist is private to your account. Our servers cannot access it. You would need to move those videos to a Public or Unlisted playlist first.": '「後で見る」プレイリストはアカウントに対してプライベートです。当社のサーバーはアクセスできません。最初にそれらのビデオを公開または非公開のプレイリストに移動する必要があります。',
    'If the live stream has ended and is available as a VOD, it will download normally. If the stream is currently live, the tool will skip it, as it has no finite length.': 'ライブストリームが終了してVODとして利用可能な場合、通常どおりダウンロードされます。ストリームが現在ライブの場合、有限の長さがないため、ツールはそれをスキップします。',
    'Parsing the list takes only seconds. The conversion time depends on the total length of the videos and the chosen quality, but our concurrent processing usually finishes a typical music playlist in under 3 minutes.': 'リストの解析には数秒しかかかりません。変換時間はビデオの合計長と選択した品質に依存しますが、当社の並行処理は通常、典型的な音楽プレイリストを3分以内に完了します。',
    'Currently, browser security restrictions prevent websites from automatically triggering 50 file downloads at once. You will need to click the download button for each generated file.': '現在、ブラウザのセキュリティ制限により、ウェブサイトが一度に50個のファイルダウンロードを自動的にトリガーすることはできません。生成された各ファイルのダウンロードボタンをクリックする必要があります。',
    'The individual video files will have their respective video thumbnails embedded as metadata (for audio formats) or as the poster frame (for video formats).': '個々のビデオファイルには、それぞれのビデオサムネイルがメタデータとして埋め込まれます（オーディオフォーマットの場合）またはポスターフレームとして（ビデオフォーマットの場合）。',
    "If the channel has a 'Play All' button or a playlist containing all their uploads, yes. Just copy that specific playlist URL.": "チャンネルに「すべて再生」ボタンまたはすべてのアップロードを含むプレイリストがある場合は、はい。その特定のプレイリストURLをコピーするだけです。",
    "The files retain their original YouTube titles. If the creator numbered the titles (e.g., 'Episode 1: ...'), that numbering will be in your downloaded file.": "ファイルは元のYouTubeタイトルを保持します。作成者がタイトルに番号を付けた場合（例：「エピソード1：...」）、その番号付けはダウンロードしたファイルに含まれます。",
    'This usually means the missing videos are either Private, Deleted, or Region-Blocked. Our tool can only fetch publicly accessible media.': 'これは通常、欠落しているビデオがプライベート、削除、または地域ブロックされていることを意味します。当社のツールは、公開アクセス可能なメディアのみを取得できます。',
    'Bulk-convert every video in a playlist': 'プレイリスト内のすべてのビデオを一括変換',
    'Paste any public YouTube playlist URL (for example ?list=PL…) and yt2mp3.lol queues every video individually. Each conversion runs in parallel where possible, so even long playlists finish quickly. You get one clean file per video, named with the original title.': '任意の公開YouTubeプレイリストURL（例：?list=PL…）を貼り付けると、yt2mp3.lolは各ビデオを個別にキューに入れます。各変換は可能な限り並行して実行されるため、長いプレイリストでも迅速に完了します。元のタイトルで名前が付けられた、ビデオごとに1つのクリーンなファイルが得られます。',
    'Supports mixes and topic playlists': 'ミックスとトピックプレイリストをサポート',
    'Auto-generated mixes, Topic artist playlists, and user-curated playlists all work as long as they\'re set to Public or Unlisted. Private playlists won\'t resolve.': '自動生成されたミックス、トピックアーティストプレイリスト、およびユーザーがキュレートしたプレイリストは、公開または非公開に設定されている限り、すべて機能します。プライベートプレイリストは解決されません。',
    'Picking the right format': '適切なフォーマットの選択',
    'For music, MP3 at 320 kbps is the standard. For podcasts, M4A produces smaller files at equal quality. For lecture series you plan to re-watch, MP4 at 720p balances storage and clarity.': '音楽の場合、320 kbpsのMP3が標準です。ポッドキャストの場合、M4Aは同等の品質でより小さなファイルを生成します。再視聴する予定の講義シリーズの場合、720pのMP4はストレージと明瞭さのバランスを取ります。',
    'Format Comparison Table': 'フォーマット比較表',
    'YouTube Shorts Downloader': 'YouTube Shortsダウンローダー', 'Download YouTube Shorts videos in MP3 or MP4 format. Fast, free, and easy to use.': 'YouTube ShortsビデオをMP3またはMP4形式でダウンロードします。高速、無料、使いやすい。',
    'youtube shorts downloader, shorts to mp3, download youtube shorts, shorts converter': 'youtube shortsダウンローダー、shortsからmp3、youtube shortsダウンロード、shortsコンバーター',
    'YouTube Multi Downloader': 'YouTube マルチダウンローダー', 'Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.': '複数のYouTubeビデオを一度にダウンロードします。複数のURLを貼り付けて、一度にすべて変換します。',
    'youtube multi downloader, bulk youtube download, multiple youtube videos, batch download': 'youtube マルチダウンローダー、一括youtubeダウンロード、複数のyoutubeビデオ、バッチダウンロード',
}

def t(f):
    c = Path(f).read_text(encoding='utf-8')
    for e, b in japanese.items(): c = c.replace(e, b)
    Path(f).write_text(c, encoding='utf-8')
    print(f"✓ {f}")

t('web/ja/youtube-playlist-downloader/index.html')
t('web/ja/youtube-shorts-downloader/index.html')
t('web/ja/youtube-multi-downloader/index.html')
print("\n✅ Japanese (ja) complete - 3/3")
