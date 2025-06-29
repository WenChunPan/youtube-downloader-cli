from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import subprocess
import logging
import re
import sys
import json

__version__ = "1.0.1"
print(f"YouTube ダウンローダー - バージョン {__version__}")


download_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_dir, exist_ok=True)

# config.jsonを読み込む
try:
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError:
    config = {"debug": False}  # ファイルが存在しない場合はdebugをFalse

debug = config.get("debug", False)  # "debug" が存在しない場合、False を返す


if debug:
    # ログ設定
    log_path = os.path.join(download_dir, "log.txt")
    print("ログ出力先:", log_path)
    logging.basicConfig(
        filename=log_path,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
else:
    logging.basicConfig(
        stream=sys.stdout,  # 画面にのみ表示し、ファイルには出力しません
        level=logging.INFO,
        format="%(message)s",
    )

try:
    # 動画をダウンロード
    url = input("URLを入力してください：")
    if not url.strip():
        raise ValueError("URLを入力してください！")

    yt = YouTube(url, on_progress_callback=on_progress)

    print("-----")
    print("タイトル：", yt.title)
    print(f"動画の長さ： {yt.length // 60}分{yt.length % 60}秒")
    print("チャンネル：", yt.author)
    print("チャンネルURL：", yt.channel_url)
    print("サムネイル：", yt.thumbnail_url)
    print("再生回数：", yt.views)

    # ストリームを取得
    video_stream = (
        yt.streams.filter(adaptive=True, only_video=True)  # 動画のみダウンロード
        .order_by("resolution")
        .desc()
        .first()
    )
    # 音声を取得
    audio_stream = (
        yt.streams.filter(adaptive=True, only_audio=True).order_by("abr").desc().first()
    )

    # ファイル名を整理
    safe_title = re.sub(r'[\\/*?:"<>|]', "_", yt.title)
    output_path = os.path.join(download_dir, f"{safe_title}.mp4")

    logging.info("\n🎞️ 動画をダウンロード中...")
    video_path = os.path.join(download_dir, "temp_video.mp4")
    video_stream.download(download_dir, filename="temp_video.mp4")

    logging.info("\n🎵 音声をダウンロード中...")
    audio_path = os.path.join(download_dir, "temp_audio.mp4")
    audio_stream.download(download_dir, filename="temp_audio.mp4")

    # 映像と音声を結合
    logging.info("🔧 映像と音声を結合中...")

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
    result = subprocess.run(cmd, shell=True)

    # 一時ファイルを削除
    os.remove(video_path)
    os.remove(audio_path)

    print("\n✅ ダウンロード完了！保存先：", output_path)
except Exception as e:
    print(f"\n 	エラーが発生しました：{e}")
    logging.error("	エラーが発生しました", exc_info=True)
