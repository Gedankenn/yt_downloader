from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import os

def download_youtube_video(url, output_path=""):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        print("Downloading video...")
        video_stream.download(output_path)
        print("Video downloaded successfully!")

        # Convert video to audio (MP3)
        video_filename = video_stream.default_filename
        audio_filename = video_filename.split(".")[0] + ".mp3"
        video_path = os.path.join(output_path, video_filename)
        audio_path = os.path.join(output_path, audio_filename)

        print("Converting video to MP3...")
        ffmpeg_extract_audio(video_path, audio_path)
        print("Conversion to MP3 completed!")

        # Remove the original video file
        os.remove(video_path)
        print("Original video file removed.")

        return audio_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Input YouTube URL
    youtube_url = input("Enter YouTube video URL: ")

    # Output path (default is the current working directory)
    output_directory = input("Enter output directory (press Enter for current directory): ").strip() or "."

    # Download and convert to MP3
    mp3_file_path = download_youtube_video(youtube_url, output_directory)

    if mp3_file_path:
        print(f"MP3 file saved at: {mp3_file_path}")
    else:
        print("Failed to download and convert the YouTube video.")
