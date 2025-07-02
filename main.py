from flask import Flask, Response
import os
from telegram import Bot

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

@app.route("/")
def index():
    return Response(status=204)

@app.route("/send_alert")
def send_alert():
    bot.send_message(chat_id=CHAT_ID, text="🔔 Elliott Wave Update Alert Triggered!")
    return "Message sent!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
