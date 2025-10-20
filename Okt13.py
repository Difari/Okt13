import os
from flask import Flask, request, render_template
from telebot import TeleBot, types

# Load token from environment for safety
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("Set BOT_TOKEN env var before starting the app")

bot = TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # templates/index.html
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    # Telegram will POST application/json updates here
    if request.headers.get("content-type") != "application/json":
        return "Unsupported Media Type", 415
    update = types.Update.de_json(request.get_data(as_text=True))
    bot.process_new_updates([update])
    return "", 200

@app.route("/healthz", methods=["GET"])
def healthz():
    return "ok", 200

if __name__ == "__main__":
    # Local dev: this won't receive Telegram updates unless publicly reachable via HTTPS
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")), debug=True)
