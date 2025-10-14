'''import telebot
from telebot import types

key = '8083991871:AAFQUf9VaHYh362ygDiwvDiDt1xMZUuEnQc'
bot = telebot.TeleBot(key)

@bot.message_handler(commands=['start'])
def main(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1=types.KeyboardButton("Магазин")
    item2 = types.KeyboardButton("Корзина")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, reply_markup=markup)


bot.infinity_polling()'''
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