from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Clipper 2.0 Running"

@app.route("/download")
def download():
    url = request.args.get("url")

    if not url:
        return "No URL provided"

    return f"Received URL: {url}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
