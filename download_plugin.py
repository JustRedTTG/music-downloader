import os
import time

from pytube import YouTube

DIR = "Music"
os.makedirs(DIR, exist_ok=True)


def download_youtube(yt: YouTube):
    title = "".join(c for c in yt.title if c.isalpha() or c.isdigit() or c == ' ').rstrip()
    music_only = f'{title}.mp3'
    if music_only in os.listdir(DIR):
        return

    video = yt.streams.filter(only_audio=True).first()

    print(f'Downloading "{title}"')

    file = video.download(output_path=DIR, skip_existing=True)

    os.rename(file, os.path.join(DIR, music_only))


def download_link(link: str):
    yt = YouTube(link)

    download_youtube(yt)


if __name__ == "__main__":
    link = input("Enter the link of the video: ")
    download_link(link)
    print("Download completed")
    time.sleep(2)
