from flask import Flask, render_template, request
import telebot  # Если интегрируете с ботом; pip install pyTelegramBotAPI

app = Flask(__name__)

# Ваш токен бота (храните в переменных окружения!)
BOT_TOKEN = '8083991871:AAFQUf9VaHYh362ygDiwvDiDt1xMZUuEnQc'
bot = telebot.TeleBot(BOT_TOKEN)

@app.route('/')
def index():
    return render_template('index.html')

# Обработка данных из Mini App (web_app_data)
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data
    bot.reply_to(message, f"Получено из Mini App: {data}")

if __name__ == '__main__':
    # Для dev: app.run(ssl_context='adhoc')  # HTTPS для теста
    # В production: Gunicorn через amvera.yml
    app.run(host='0.0.0.0', port=5000)
    https://prod.liveshare.vsengsaas.visualstudio.com/join?CED0A27A52F9A5C51A51677B9EDF31EF96B1