from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import subprocess
import logging
import re
import sys
import json

__version__ = "1.0.1"
print(f"YouTube Downloader - 版本 {__version__}")


download_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_dir, exist_ok=True)

# 嘗試讀取config.json
try:
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError:
    config = {"debug": False}  # 沒有檔案就預設為False

debug = config.get("debug", False)  # 避免key錯誤、沒有key


if debug:
    # 設定log
    log_path = os.path.join(download_dir, "log.txt")
    logging.basicConfig(
        filename=log_path,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
else:
    logging.basicConfig(
        stream=sys.stdout,  # 只顯示在螢幕上，不輸出成檔案
        level=logging.INFO,
        format="%(message)s",
    )

try:
    # 下載影片
    url = input("請輸入影片網址：")
    if not url.strip():
        raise ValueError("請輸入影片網址！")

    yt = YouTube(url, on_progress_callback=on_progress)

    print("-----")
    print("標題：", yt.title)  # 標題
    print(f"影片長度： {yt.length // 60}分{yt.length % 60}秒")  # 長度
    print("作者：", yt.author)  # 作者
    print("作者頻道：", yt.channel_url)  # 作者頻道網址
    print("縮圖網址：", yt.thumbnail_url)  # 縮圖網址
    print("瀏覽次數：", yt.views)  # 瀏覽次數

    # 抓取串流
    video_stream = (
        yt.streams.filter(adaptive=True, only_video=True)
        .order_by("resolution")
        .desc()
        .first()
    )
    audio_stream = (
        yt.streams.filter(adaptive=True, only_audio=True).order_by("abr").desc().first()
    )

    # 安全命名
    safe_title = re.sub(r'[\\/*?:"<>|]', "_", yt.title)
    output_path = os.path.join(download_dir, f"{safe_title}.mp4")

    logging.info("\n🎞️ 正在下載影片...")
    video_path = os.path.join(download_dir, "temp_video.mp4")
    video_stream.download(download_dir, filename="temp_video.mp4")

    logging.info("\n🎵 正在下載音訊...")
    audio_path = os.path.join(download_dir, "temp_audio.mp4")
    audio_stream.download(download_dir, filename="temp_audio.mp4")

    # 合併影片和音訊
    logging.info("🔧 正在合併影片與音訊...")
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        video_path,
        "-i",
        audio_path,
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        output_path,
    ]
    subprocess.run(cmd, shell=True)

    # 刪除暫存檔
    os.remove(video_path)
    os.remove(audio_path)

    print("\n✅ 下載完成！儲存位置：", output_path)
except Exception as e:
    print(f"\n 發生錯誤：{e}")
    logging.error("錯誤發生", exc_info=True)
