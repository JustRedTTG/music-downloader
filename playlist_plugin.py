import threading

from download_plugin import download_link
from pytube import Playlist

playlist = Playlist("https://music.youtube.com/playlist?list=PLDInnU04fQ9aMylzx_-oVJogshRvUOEya&si=aXFSdSk4-m7OgS7w")

threads = []

THREADS_LIMIT = 20

for link in playlist.url_generator():
    while threading.active_count() > THREADS_LIMIT:
        print("Waiting for threads to finish", end="\r")
        pass

    thread = threading.Thread(target=download_link, args=(link,))
    thread.start()
    threads.append(thread)

    for thread in threads:
        thread.join()
