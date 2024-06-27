#!/usr/bin/env python3

import os
import sys
import youtube_dl as ydl

def download_yt_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    ydl.YoutubeDL(ydl_opts).download([url])

def download_yt_playlist(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'yes-playlist': True,
    }
    ydl.YoutubeDL(ydl_opts).download([url])

def download_yt_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    ydl.YoutubeDL(ydl_opts).download([url])

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

    print("Error: Invalid option")
    help()
    sys.exit(1)

if __name__ == "__main__":
    main()
