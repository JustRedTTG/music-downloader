from download_plugin import download_youtube
from pytube import Playlist

playlist = Playlist("https://music.youtube.com/playlist?list=PLDInnU04fQ9aMylzx_-oVJogshRvUOEya&si=aXFSdSk4-m7OgS7w")

for i, video in enumerate(playlist.videos_generator()):
    download_youtube(video)
    print(f'[{i}] Downloaded "{video.title}"')
