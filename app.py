from flask import Flask, request
import yt_dlp
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Clipper 2.0 Running"

@app.route("/download")
def download():
    url = request.args.get("url")
    if not url:
        return "No URL provided"

    # yt-dlp options
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': 'downloaded_video.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return f"Downloaded video from URL: {url}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
