#!/usr/bin/env python3
from pathlib import Path

pt_trans = {
    "Save YouTube Shorts as MP3 audio or MP4 video in seconds. Original vertical aspect ratio preserved.": "Salve YouTube Shorts como áudio MP3 ou vídeo MP4 em segundos. Proporção de aspecto vertical original preservada.",
    "Download multiple YouTube videos at once. Paste multiple URLs and convert them all in one go.": "Baixe vários vídeos do YouTube de uma vez. Cole vários URLs e converta todos de uma vez.",
    "Downloading videos one by one is incredibly tedious. Our YouTube Playlist Downloader is engineered for bulk operations. By parsing the playlist metadata, our servers generate individual conversion jobs for every single video in the list, allowing you to download an entire album, lecture series, or podcast backlog with minimal effort.": "Baixar vídeos um por um é incrivelmente tedioso. Nosso YouTube Playlist Downloader é projetado para operações em massa. Ao analisar os metadados da playlist, nossos servidores geram trabalhos de conversão individuais para cada vídeo da lista, permitindo que você baixe um álbum inteiro, série de palestras ou backlog de podcast com o mínimo de esforço.",
    "When you download a playlist, organization is key. Our system automatically grabs the original video titles and structures the downloads so you can easily maintain the intended order. This is perfect for sequential tutorials, multi-part documentaries, or chronologically ordered music albums.": "Quando você baixa uma playlist, a organização é fundamental. Nosso sistema captura automaticamente os títulos de vídeo originais e estrutura os downloads para que você possa facilmente manter a ordem pretendida. Isso é perfeito para tutoriais sequenciais, documentários em várias partes ou álbuns de música ordenados cronologicamente.",
    "You aren't locked into a single format. You can choose to download an entire music playlist as crisp 320kbps MP3s, or an entire educational course as 1080p MP4s. Our FFmpeg backend applies your selected format uniformly across all items in the batch.": "Você não está preso a um único formato. Você pode escolher baixar uma playlist de música inteira como MP3s nítidos de 320kbps, ou um curso educacional inteiro como MP4s de 1080p. Nosso backend FFmpeg aplica seu formato selecionado uniformemente em todos os itens do lote.",
    "We don't make you wait for one video to finish before starting the next. Our cloud infrastructure utilizes high-concurrency processing, meaning multiple videos from your playlist are downloaded and converted simultaneously. A 50-video playlist is processed significantly faster than doing it manually.": "Não fazemos você esperar um vídeo terminar antes de começar o próximo. Nossa infraestrutura em nuvem utiliza processamento de alta concorrência, o que significa que vários vídeos de sua playlist são baixados e convertidos simultaneamente. Uma playlist de 50 vídeos é processada significativamente mais rápido do que fazer manualmente.",
}

for f in ['web/pt/youtube-playlist-downloader/index.html', 'web/pt/youtube-shorts-downloader/index.html', 'web/pt/youtube-multi-downloader/index.html']:
    c = Path(f).read_text(encoding='utf-8')
    for e, p in pt_trans.items():
        c = c.replace(e, p)
    Path(f).write_text(c, encoding='utf-8')
    print(f"✓ {f}")
print("\n✅ Portuguese (pt) complete - 3/3")
