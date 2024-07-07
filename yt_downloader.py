#!/usr/bin/env python3

import os
import sys
import pytube as pt


def download_yt_video(url):
    yt = pt.YouTube(url)
    print("Downloading video...")
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

def download_yt_playlist(url):
    playlist = pt.Playlist(url)
    print("Downloading playlist...")
    for video in playlist.videos:
        video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

def download_yt_audio(url):
    yt = pt.YouTube(url)
    print(f"Downloading audio from {yt.title}...")
    yt.streams.filter(only_audio=True).order_by('abr').desc().first().download()
    os.system(f"mv '{yt.title}'.webm '{yt.title}'.mp3")

def download_yt_audio_playlist(url):
    playlist = pt.Playlist(url)
    print("Downloading audio playlist...")
    length = playlist.length
    position = 1
    downloaded = read_musics_in_folder()

    for video in playlist.videos:
        try:
            if f"{video.title}.mp3" in downloaded:
                print(f"{position} / {length} Skipping {video.title}")
                position += 1
                continue
            print(f"{position} / {length} Downloading {video.title}")
            video.streams.filter(only_audio=True).order_by('abr').desc().first().download()
            os.system(f"mv '{video.title}'.webm '{video.title}'.mp3")
            position += 1
        except:
            print(f"Error: Unable to download {video.title}")

def read_musics_in_folder():
    musics = []
    for music in os.listdir():
        if music.endswith(".mp3"):
            musics.append(music)
    return musics

def convert_webm_to_mp3():
    for music in os.listdir():
        if music.endswith(".mp3") or music.endswith(".py"):
            continue

        music2 = music.split(".")[0] + ".mp3"
        os.system(f"mv '{music}' '{music2}'")

def help():
    print("Usage: yt_downloader.py [URL] [OPTIONS]")
    print("Options:")
    print("    -h, --help: Display this help message")
    print("    -p, --playlist: Download a playlist")
    print("    -v, --video: Download a single video")
    print("    -a, --audio: Download audio only")
    print("Example: yt_downloader.py https://www.youtube.com/watch?v=video_id")


def main():
    if len(sys.argv) < 2:
        url = input("Enter the URL: ")
        option = input("Enter the option: ")
        if option in ("-h", "--help"):
            help()
            sys.exit(0)
        if option in ("-v", "--video"):
            download_yt_video(url)
            sys.exit(0)

        if option in ("-p", "--playlist"):
            download_yt_playlist(url)
            sys.exit(0)

        if option in ("-a", "--audio"):
            download_yt_audio(url)
            sys.exit(0)

        if option in ("-ap", "--audio-playlist"):
            download_yt_audio_playlist(url)
            sys.exit(0)
        
        if option in ("-c", "--convert"):
            convert_webm_to_mp3()
            sys.exit(0)

        print("Error: Invalid option")
        help()
        sys.exit(1)

    if sys.argv[1] in ("-h", "--help"):
        help()
        sys.exit(0)

    if sys.argv[1] in ("-v", "--video"):
        download_yt_video(sys.argv[2])
        sys.exit(0)

    if sys.argv[1] in ("-p", "--playlist"):
        download_yt_playlist(sys.argv[2])
        sys.exit(0)

    if sys.argv[1] in ("-a", "--audio"):
        download_yt_audio(sys.argv[2])
        sys.exit(0)

    if sys.argv[1] in ("-ap", "--audio-playlist"):
        download_yt_audio_playlist(sys.argv[2])
        sys.exit(0)

    print("Error: Invalid option")
    help()
    sys.exit(1)

if __name__ == "__main__":
    main()
