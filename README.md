# 🎥 YouTube Downloader CLI ツール

YouTube の動画と音声を高画質でダウンロードし、自動で結合して MP4 に保存できる、シンプルな Python CLI ツールです。

> 🈯️ 言語切替 / 切換語言  
> 👉 [🇯🇵 日本語](./README.md) ｜ [🌐 繁體中文](./README_zh-tw.md)

---

## 📦 使用技術

- Python 3.x
- pytubefix
- ffmpeg（外部ツール）

---

## 🚀 使用方法

1. 必要なパッケージをインストール：`pip install -r requirements.txt`
2.  [FFmpeg（公式サイト）](https://www.gyan.dev/ffmpeg/builds/)をダウンロード
3. 解凍後、 `ffmpeg.exe` をこのプロジェクトのフォルダに配置
4. ツールを実行する：`python Youtube_Downloader.py`
---

## 📁 出力結果

- 保存先：`downloads/動画タイトル.mp4`
- エラーログ：`downloads/log.txt`

---

## 🧊 EXE 版（実行ファイル版）

プログラミング不要！ 
 [Releases](https://github.com/WenChunPan/youtube-downloader-cli/releases) ページから EXE 版をダウンロードして、解凍後すぐに使用できます。

---

## ⚠️ 注意事項

- このツールは学術目的のみに使用してください。YouTube の利用規約に反しないようご注意ください。
- 音声がない場合や合成エラーが出た場合は、ffmpeg.exe が正しく配置されているか確認してください。

---

## 🔧 FFmpeg について

このツールは FFmpeg を使って音声と映像を結合しています。

- `ffmpeg.exe` は GPLv3 ライセンスの元で配布されています
- ソース元：[https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
- 詳細ライセンス：[https://ffmpeg.org/legal.html](https://ffmpeg.org/legal.html)

---

## 📜 License

MIT ライセンスの元で公開しています。自由に使用・改変可能です。
