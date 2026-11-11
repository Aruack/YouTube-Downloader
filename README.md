# YouTube Multi-Format Downloader

A fast, lightweight, and user-friendly cross-platform YouTube downloader written in Python. Developed by **Aryan Kumar ([@Aruack](https://github.com/Aruack))**, it supports Android (**Termux**) and Desktop (**Windows/macOS/Linux**), offering multi-resolution video downloads, audio extractions, embedded thumbnail art, automatic folder management, and a sleek terminal interface powered by `rich`.

---

## Author & Maintainer

- **Developer**: Aryan Kumar
- **GitHub**: [@Aruack](https://github.com/Aruack)

---

## Features

- **Cross-Platform Storage Detection**: Automatically detects Termux (Android) vs. PC environments and routes downloaded files accordingly.
- **Auto Dependency Installation**: Checks for required Python packages (`yt-dlp`, `rich`, `requests`) on launch and installs any missing libraries automatically.
- **Automated Directory Organization**: Saves outputs inside a dedicated `Aruack ytDownloads` directory, automatically separating media into `Videos/` and `Music/` subfolders.
- **Embedded Cover Art**: Embeds thumbnails directly into MP3/M4A audio tags and MP4 video metadata.
- **Rich Terminal UI**: Features a clean progress bar showing percentage, download speed, downloaded size, and estimated time remaining (ETA).
- **Format Options**:
  - **Video (MP4)**: Best Quality (Auto-merge), 1080p, 720p, 360p
  - **Audio**: MP3 (192kbps) with embedded cover art, M4A with embedded cover art

---

## System Prerequisites

1. **Python 3.x**
2. **FFmpeg**: Required by `yt-dlp` to merge video/audio streams and embed thumbnails into media files.
   - **Termux (Android)**: Run `pkg install ffmpeg`
   - **Windows**: Install via `winget install ffmpeg` or download binaries and add them to system `PATH`.
   - **Linux/macOS**: Install via package manager (`sudo apt install ffmpeg` or `brew install ffmpeg`).

---

## Installation & Setup

1. Clone or download this repository:
   ```bash
   git clone https://github.com/Aruack/YouTube-Downloader.git
   cd YouTube-Downloader
   ```
2. On **Termux (Android)**, grant storage access before running for the first time:
   ```bash
   termux-setup-storage
   ```

---

## How to Run

Launch the script using Python:

```bash
python yt_downloader.py
```

### Usage Steps
1. Paste the target YouTube video URL.
2. Confirm the retrieved title and channel details.
3. Select your desired resolution or audio format (choices `1`–`6`).
4. Find your downloaded file inside the designated `Aruack ytDownloads` folder.

---

## File Destinations

- **Android (Termux)**: `/sdcard/Aruack ytDownloads/`
- **PC (Windows/Linux/macOS)**: `<Current_Directory>/Aruack ytDownloads/`

---

## License

This project is licensed under the [MIT License](LICENSE) — authored by **Aryan Kumar (Aruack)**.
