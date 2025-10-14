from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Ваш файл с кодом выше

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Для HTTPS в dev (Telegram требует HTTPS)