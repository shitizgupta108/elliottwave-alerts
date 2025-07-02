
from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

html_form = """
<!DOCTYPE html>
<html>
<head><title>Telegram Bot Tester</title></head>
<body>
  <h2>Send Test Message to Telegram Channel</h2>
  <form method="POST">
    <label>Bot Token:</label><br>
    <input type="text" name="token" size="60"><br><br>
    <label>Chat ID (e.g., @yourchannel):</label><br>
    <input type="text" name="chat_id" size="60"><br><br>
    <label>Message:</label><br>
    <textarea name="message" rows="4" cols="60">📈 Elliott Wave Test Alert</textarea><br><br>
    <input type="submit" value="Send">
  </form>
  {% if result %}
    <h3>Result:</h3>
    <pre>{{ result }}</pre>
  {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def send_message():
    result = None
    if request.method == 'POST':
        token = request.form.get('token')
        chat_id = request.form.get('chat_id')
        message = request.form.get('message')
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        try:
            response = requests.post(url, data={"chat_id": chat_id, "text": message})
            result = response.json()
        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(html_form, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
