# yt_downloader

Python command-line script to download YouTube videos, playlists or audio, using [pytube](https://github.com/pytube/pytube).

## Requirements

```bash
pip install pytube
```

Files are saved in the current directory. Renaming audio to `.mp3` uses the `mv` shell command, so the audio options expect Linux/macOS.

## Usage

```bash
python3 yt_downloader.py -v  <video-url>       # single video (highest-resolution progressive MP4)
python3 yt_downloader.py -p  <playlist-url>    # every video of a playlist
python3 yt_downloader.py -a  <video-url>       # audio only (best bitrate), renamed .webm -> .mp3
python3 yt_downloader.py -ap <playlist-url>    # audio of a playlist, skipping .mp3 files already in the folder
python3 yt_downloader.py -h                    # help
```

Run it without arguments to be prompted for the URL and the option. Interactive mode also has `-c` / `--convert`, which renames every non-`.mp3`, non-`.py` file in the folder to `.mp3` (a rename only, with no transcoding).
