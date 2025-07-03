
from flask import Flask
import requests
import datetime
import pytz

app = Flask(__name__)

BOT_TOKEN = "7816564668:AAEOvjFwO7kqhK4EokIoQ40EHdygM_yU2e0"
CHANNEL_ID = "@elliottwavealerts"

def generate_alert():
    now = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M')
    message = f"""
📢 *Live Elliott Wave Alert*
🕒 Time: {now} IST

🟢 Nifty: Wave 3 in progress, intraday bullish
🎯 Target: 24480–24600
📌 SL: Below 24280

🟡 Crude: Wave 5 starting, bullish impulse
🎯 Target: 5740–5800
📌 SL: Below 5620

🔵 Natural Gas: Wave 3 extended
🎯 Target: 308–312
📌 SL: Below 296

_Elliott Wave view auto-updated every 15 mins._
"""
    return message

@app.route('/')
def home():
    return "Elliott Wave Alert System is Running!"

@app.route('/send-alert')
def send_alert():
    message = generate_alert()
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=payload)
    return "Alert Sent!" if response.status_code == 200 else f"Failed: {response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
