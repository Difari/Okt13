import os
from flask import Flask, render_template, request, jsonify
import telebot  # pip install pyTelegramBotAPI

app = Flask(__name__)

# Токен бота из env (безопасно)
BOT_TOKEN = "8083991871:AAFQUf9VaHYh362ygDiwvDiDt1xMZUuEnQc"  # Установите в Amvera env vars
bot = telebot.TeleBot(BOT_TOKEN)

@app.route('/')
def index():
    return render_template('index.html')  # templates/index.html

# Обработка данных из Mini App (web_app_data через webhook или polling)
@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()
    # Здесь обработка update от Telegram (если webhook)
    try:
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return jsonify({'status': 'ok'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Handler для web_app_data (если используете polling — запустите отдельно)
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data
    bot.reply_to(message, f"Получено из Mini App: {data}")

# Для production: Gunicorn запустит, не используйте app.run()
# Но для локального теста добавьте:
if __name__ == '__main__':
    # Установите webhook локально один раз: bot.remove_webhook(); bot.set_webhook(url='https://your-url.amvera.io/webhook')
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')  # HTTPS для теста
