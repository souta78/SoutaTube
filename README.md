# YouTube Downloader MP4/MP3

Aplikasi Python sederhana untuk mendownload video YouTube dalam format MP4 (video) atau MP3 (audio).

**Author:** Souta

## Fitur

- Download video dalam format MP4 dengan berbagai kualitas (360p, 480p, 720p, 1080p)
- Download audio dalam format MP3 dengan kualitas pilihan (128, 192, 320 kbps)
- Support download playlist YouTube
- File otomatis tersimpan di folder Downloads sistem
- Interface menu yang mudah digunakan

## Persyaratan

- Python 3.7 atau lebih baru
- Library `yt-dlp`
- FFmpeg (opsional, hanya untuk MP3)

## Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader
```

### 2. Install Library yang Diperlukan
```bash
pip install yt-dlp
```

### 3. Install FFmpeg (Opsional untuk MP3)

**Penting:** FFmpeg hanya dibutuhkan untuk download MP3. Untuk download MP4, aplikasi dapat berjalan tanpa FFmpeg.

#### Windows
1. Download FFmpeg dari [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract dan tambahkan ke system PATH

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

#### macOS
```bash
brew install ffmpeg
```

## Cara Penggunaan

### Menjalankan Aplikasi
```bash
python youtube_downloader.py
```

### Menu Aplikasi
```
YouTube Downloader MP4/MP3
Author: Souta
========================================
Download location: C:\Users\YourName\Downloads

Menu:
1. Download MP4 (Video)
2. Download MP3 (Audio)
3. Download Playlist
4. Exit
```

### Contoh Penggunaan

1. **Download Video MP4:**
   - Pilih menu 1
   - Masukkan URL YouTube
   - Pilih kualitas video (360p/480p/720p/1080p)

2. **Download Audio MP3:**
   - Pilih menu 2
   - Masukkan URL YouTube
   - Pilih kualitas audio (128/192/320 kbps)

3. **Download Playlist:**
   - Pilih menu 3
   - Masukkan URL playlist YouTube
   - Pilih format dan kualitas

## Lokasi File Download

File hasil download akan tersimpan di:
- **Windows:** `C:\Users\[Username]\Downloads`
- **macOS:** `/Users/[Username]/Downloads`
- **Linux:** `/home/[Username]/Downloads`

### Format URL yang Didukung
- Video tunggal: `https://www.youtube.com/watch?v=VIDEO_ID`
- Video pendek: `https://youtu.be/VIDEO_ID`
- Playlist: `https://www.youtube.com/playlist?list=PLAYLIST_ID`

## Troubleshooting

### Error: "Library yt-dlp is not installed!"
```bash
pip install yt-dlp
```

### Download MP3 Gagal
- Pastikan FFmpeg sudah terinstall dengan benar
- Cek apakah FFmpeg sudah ada di system PATH
- Untuk sementara, gunakan download MP4 yang tidak memerlukan FFmpeg

### URL Tidak Valid
- Pastikan URL mengandung `youtube.com` atau `youtu.be`
- Periksa apakah video masih tersedia dan tidak di-private

### Download Gagal / Error
- Update yt-dlp ke versi terbaru: `pip install --upgrade yt-dlp`
- Periksa koneksi internet
- Beberapa video mungkin memiliki pembatasan region

## File Structure

```
youtube-downloader/
│
├── youtube_downloader.py    # File utama aplikasi
├── README.md               # Dokumentasi
└── Downloads/             # Folder sistem (otomatis)
    ├── video1.mp4
    ├── audio1.mp3
    └── ...
```

## Requirements.txt

```txt
yt-dlp>=2023.1.6
```

## Disclaimer

- Aplikasi ini hanya untuk tujuan edukasi dan penggunaan pribadi
- Pastikan Anda memiliki hak untuk mendownload konten
- Hormati hak cipta dan terms of service YouTube
- Developer tidak bertanggung jawab atas penyalahgunaan aplikasi

## Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur baru
3. Commit perubahan Anda
4. Push ke branch
5. Buat Pull Request

## Lisensi

Distributed under the MIT License.

## Kontak

Jika ada pertanyaan atau masalah, silakan buat issue di repository ini.

---

**Dibuat oleh Souta**
