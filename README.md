# 🎥 YouTube Downloader CLI 工具

一個簡單的 Python 命令列工具，支援從 YouTube 下載最高畫質影片與音訊，自動合併並儲存為 MP4 檔案。

---

## 📦 技術使用

- Python 3.x
- pytubefix
- ffmpeg（外部工具）

---

## 🚀 使用方法

1. 安裝套件：pip install -r requirements.txt
2. 下載免安裝 [FFmpeg](https://www.gyan.dev/ffmpeg/builds/)或直接使用 zip 包中附的 ffmpeg.exe（建議保留在 `ffmpeg/` 資料夾中）
3. 執行程式：python Youtube_Downloader.py
---

## 📁 輸出結果

- 儲存路徑：`downloads/影片標題.mp4`
- 錯誤紀錄：`downloads/log.txt`

---

## 🧊 EXE 版本

不會寫程式也能使用！  
前往 [Releases](https://github.com/WenChunPan/youtube-downloader-cli/releases) 頁面下載打包好的執行檔。

---

## ⚠️ 注意事項

- 僅供學術用途，請勿違反平台規定（如 YouTube 條款）
- 若合併失敗或影片缺音，請確認 `ffmpeg.exe` 是否存在於資料夾中

---

## 🔧 關於 FFmpeg 使用

本工具使用 FFmpeg 合併音訊與影片。

- `ffmpeg.exe` 為 GPLv3 授權
- 來源：[https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
- 授權條款詳見：[https://ffmpeg.org/legal.html](https://ffmpeg.org/legal.html)

---

## 📜 License

本專案採用 MIT 授權條款，歡迎自由使用與修改。
