import youtube_dl

ydl_opts = {
    'ignoreerrors': True,
    'quiet': False
}

PLAYLIST_URL = ""

with youtube_dl.YoutubeDL(ydl_opts) as ydl:

    playlist_dict = ydl.extract_info(PLAYLIST_URL, download=False)

    for video in playlist_dict['entries']:

        print()

        if not video:
            print('ERROR: Unable to get info. Continuing...')
            continue

        for property in ['thumbnail', 'id', 'title', 'description', 'duration']:
            print(property, '--', video.get(property))
