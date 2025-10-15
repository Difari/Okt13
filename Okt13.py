import os
from flask import Flask, render_template, request, jsonify
import telebot

app = Flask(__name__)

BOT_TOKEN = "8083991871:AAFQUf9VaHYh362ygDiwvDiDt1xMZUuEnQc"
bot = telebot.TeleBot(BOT_TOKEN)

@app.route('/')
def index():
    return render_template('templates/index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()
    try:
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return jsonify({'status': 'ok'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data
    bot.reply_to(message, f"Получено из Mini App: {data}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
