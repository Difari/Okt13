# Okt13 (fixed)

## Запуск локально (UI без Telegram)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python sho.py
# откройте http://localhost:5000
```

## Продакшн / приём Telegram-обновлений
1. Задайте переменную среды:
```bash
export BOT_TOKEN="<НОВЫЙ_ТОКЕН_ОТ_BOTFATHER>"
```
2. Запустите сервер:
```bash
gunicorn Okt13:app --bind 0.0.0.0:8000
```
3. После деплоя на публичный HTTPS-домен установите вебхук:
```bash
curl "https://api.telegram.org/bot$BOT_TOKEN/setWebhook?url=https://ВАШ-ДОМЕН/webhook"
```
4. Проверка здоровья: `GET /healthz` → `ok`.
