"""
YouTube Downloader - MP4 & MP3
Simple YouTube downloader using yt-dlp for downloading videos in MP4 or MP3 format
Author: Souta78
"""

import os
import sys
import yt_dlp
from pathlib import Path

class YouTubeDownloader:
    def __init__(self):
        self.download_path = self.get_downloads_folder()
        
    def get_downloads_folder(self):
        """Get the default Downloads folder for the current OS"""
        home = Path.home()
        
        downloads_win = home / "Downloads"
        if downloads_win.exists():
            return downloads_win
            
        downloads_paths = [
            home / "Downloads",
            home / "Download",
            home / "downloads",
            home / "Desktop"  
        ]
        
        for path in downloads_paths:
            if path.exists():
                return path
                
        downloads_default = home / "Downloads"
        downloads_default.mkdir(exist_ok=True)
        return downloads_default
    
    def download_mp4(self, url, quality='720p'):
        """Download video in MP4 format"""
        ydl_opts = {
            'format': f'best[height<={quality[:-1]}][ext=mp4]/best[ext=mp4]/best',
            'outtmpl': str(self.download_path / '%(title)s.%(ext)s'),
            'writeinfojson': False,
            'writesubtitles': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                print(f"Downloading video in {quality} quality...")
                ydl.download([url])
                print("MP4 download completed successfully!")
                return True
            except Exception as e:
                print(f"Error: {str(e)}")
                return False
    
    def download_mp3(self, url, quality='192'):
        """Download audio in MP3 format"""
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(self.download_path / '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': quality,
            }],
            'writeinfojson': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                print(f"Downloading audio in {quality}kbps quality...")
                ydl.download([url])
                print("MP3 download completed successfully!")
                return True
            except Exception as e:
                print(f"Error: {str(e)}")
                return False
    
    def download_playlist(self, url, format_type='mp4', quality='720p'):
        """Download playlist"""
        if format_type.lower() == 'mp3':
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': str(self.download_path / '%(playlist_index)s - %(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': quality if quality.isdigit() else '192',
                }],
            }
        else:
            ydl_opts = {
                'format': f'best[height<={quality[:-1]}][ext=mp4]/best[ext=mp4]/best',
                'outtmpl': str(self.download_path / '%(playlist_index)s - %(title)s.%(ext)s'),
            }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                print(f"Downloading playlist in {format_type.upper()} format...")
                ydl.download([url])
                print("Playlist download completed successfully!")
                return True
            except Exception as e:
                print(f"Error: {str(e)}")
                return False

def main():
    print("YouTube Downloader MP4/MP3")
    print("Author: Souta")
    print("=" * 40)
    
    downloader = YouTubeDownloader()
    print(f"Download location: {downloader.download_path}")
    
    while True:
        print("\nMenu:")
        print("1. Download MP4 (Video)")
        print("2. Download MP3 (Audio)")
        print("3. Download Playlist")
        print("4. Exit")
        
        choice = input("\nChoose option (1-4): ").strip()
        
        if choice == '4':
            print("Thank you for using YouTube Downloader!")
            break
        
        if choice not in ['1', '2', '3']:
            print("Invalid choice!")
            continue
        
        url = input("\nEnter YouTube URL: ").strip()
        if not url:
            print("URL cannot be empty!")
            continue
        

        if 'youtube.com' not in url and 'youtu.be' not in url:
            print("URL must be from YouTube!")
            continue
        
        if choice == '1':
            print("\nSelect video quality:")
            print("1. 360p (Small)")
            print("2. 480p (Medium)")
            print("3. 720p (HD)")
            print("4. 1080p (Full HD)")
            
            quality_choice = input("Choose quality (1-4, default=3): ").strip()
            quality_map = {'1': '360p', '2': '480p', '3': '720p', '4': '1080p'}
            quality = quality_map.get(quality_choice, '720p')
            
            downloader.download_mp4(url, quality)
        
        elif choice == '2':
            print("\nSelect audio quality:")
            print("1. 128 kbps (Standard)")
            print("2. 192 kbps (Good)")
            print("3. 320 kbps (Best)")
            
            quality_choice = input("Choose quality (1-3, default=2): ").strip()
            quality_map = {'1': '128', '2': '192', '3': '320'}
            quality = quality_map.get(quality_choice, '192')
            
            downloader.download_mp3(url, quality)
        
        elif choice == '3':
            format_choice = input("\nFormat (mp4/mp3, default=mp4): ").strip().lower()
            if format_choice not in ['mp4', 'mp3']:
                format_choice = 'mp4'
            
            if format_choice == 'mp4':
                quality_choice = input("Video quality (360p/480p/720p/1080p, default=720p): ").strip()
                quality = quality_choice if quality_choice in ['360p', '480p', '720p', '1080p'] else '720p'
            else:
                quality_choice = input("Audio quality (128/192/320, default=192): ").strip()
                quality = quality_choice if quality_choice in ['128', '192', '320'] else '192'
            
            downloader.download_playlist(url, format_choice, quality)

if __name__ == "__main__":
    try:
        import yt_dlp
    except ImportError:
        print("Library yt-dlp is not installed!")
        print("Install with: pip install yt-dlp")
        sys.exit(1)
    
    main()
