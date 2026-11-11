import os
import subprocess
import sys

# 1. Automatic dependency installation
for pkg in ["yt-dlp", "rich", "requests"]:
  try:
    __import__(pkg)
  except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

import yt_dlp
from rich import print as rprint
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)


def print_banner():
  banner_text = (
      "[bold cyan]YOUTUBE MULTI-FORMAT DOWNLOADER[/bold cyan]\n"
      "[yellow]Creator :[/yellow] [bold white]Aruack (Aryan Kumar)[/bold white]\n"
      "[green]GitHub  :[/green] [link=https://github.com/Aruack]github.com/Aruack[/link]"
  )
  rprint(
      Panel(
          banner_text,
          title="[bold magenta]✦ Aruack Tools ✦[/bold magenta]",
          subtitle="[dim]Secure & Portable[/dim]",
          expand=False,
          border_style="bright_blue",
      )
  )


def main():
  print_banner()

  url = input("\nEnter YouTube Link: ").strip()
  if not url:
    print("[!] No link provided. Exiting.")
    return

  print("\n[*] Fetching video details...")
  try:
    with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
      info = ydl.extract_info(url, download=False)
      title = info.get("title", "Unknown")
      uploader = info.get("uploader", "Unknown")

    print(f"\n[Title]   : {title}")
    print(f"[Channel] : {uploader}")
  except Exception as e:
    print(f"[!] Error fetching video: {e}")
    return

  if input("\nIs this correct? (y/n): ").strip().lower() != "y":
    print("Cancelled.")
    return

  print("\nSelect Format:")
  print("  1. Best Video (MP4) -> Videos/")
  print("  2. 1080p Video (MP4) -> Videos/")
  print("  3. 720p Video (MP4)  -> Videos/")
  print("  4. 360p Video (MP4)  -> Videos/")
  print("  5. Audio Only (MP3 with Embedded Thumbnail) -> Music/")
  print("  6. Audio Only (M4A with Embedded Thumbnail) -> Music/")

  choice = input("\nEnter choice (1-6): ").strip()

  # Set paths and folders inside 'Aruack ytDownloads'
  if os.path.exists("/data/data/com.termux/files/home"):
    base_dir = "/sdcard/Aruack ytDownloads"
  else:
    base_dir = os.path.join(os.getcwd(), "Aruack ytDownloads")

  is_audio = choice in ["5", "6"]
  folder = "Music" if is_audio else "Videos"
  out_dir = os.path.join(base_dir, folder)
  os.makedirs(out_dir, exist_ok=True)

  # Base options
  ydl_opts = {
      "outtmpl": os.path.join(out_dir, "%(title)s.%(ext)s"),
  }

  if choice == "1":
    ydl_opts.update({
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "writethumbnail": True,
        "embedthumbnail": True,
    })
  elif choice == "2":
    ydl_opts.update({
        "format": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "merge_output_format": "mp4",
        "writethumbnail": True,
        "embedthumbnail": True,
    })
  elif choice == "3":
    ydl_opts.update({
        "format": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "merge_output_format": "mp4",
        "writethumbnail": True,
        "embedthumbnail": True,
    })
  elif choice == "4":
    ydl_opts.update({
        "format": "bestvideo[height<=360]+bestaudio/best[height<=360]",
        "merge_output_format": "mp4",
        "writethumbnail": True,
        "embedthumbnail": True,
    })
  elif choice == "5":
    ydl_opts.update({
        "format": "bestaudio/best",
        "writethumbnail": True,
        "embedthumbnail": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {"key": "EmbedThumbnail"},
        ],
    })
  elif choice == "6":
    ydl_opts.update({
        "format": "bestaudio[ext=m4a]/best",
        "writethumbnail": True,
        "embedthumbnail": True,
        "postprocessors": [{"key": "EmbedThumbnail"}],
    })
  else:
    print("[!] Invalid choice.")
    return

  # Rich Progress Bar Setup
  progress = Progress(
      TextColumn("[bold cyan]{task.description}"),
      BarColumn(bar_width=None),
      "[progress.percentage]{task.percentage:>3.1f}%",
      "•",
      DownloadColumn(),
      "•",
      TransferSpeedColumn(),
      "•",
      TimeRemainingColumn(),
  )

  task_id = None

  def progress_hook(d):
    nonlocal task_id
    if d["status"] == "downloading":
      total = d.get("total_bytes") or d.get("total_bytes_estimate", 0)
      downloaded = d.get("downloaded_bytes", 0)
      if total > 0:
        if task_id is None:
          task_id = progress.add_task("[green]Downloading", total=total)
        progress.update(task_id, completed=downloaded)
    elif d["status"] == "finished":
      if task_id is not None:
        progress.update(
            task_id, completed=progress.tasks[task_id].total, description="[bold green]Processing & Embedding"
        )

  ydl_opts["progress_hooks"] = [progress_hook]

  print(f"\n[*] Downloading into 'Aruack ytDownloads/{folder}' folder...\n")
  try:
    with progress:
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("\n[✔] Download Complete Successfully! Thumbnail embedded into file.")
  except Exception as e:
    print(f"\n[✘] Failed: {e}")


if __name__ == "__main__":
  main()
