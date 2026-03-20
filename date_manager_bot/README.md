# 💕 Date Manager Bot

Telegram-бот для планирования идеального свидания.

## 🚀 Быстрый старт

```bash
pip install -r requirements.txt
cp .env.example .env
# Укажи BOT_TOKEN в .env
python bot.py
```

## ☁️ Хостинг

### Render (бесплатно)
1. Создай аккаунт на render.com
2. Подключи GitHub репозиторий
3. Create Web Service:
   - Root Directory: `date_manager_bot`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
4. Добавь `BOT_TOKEN` в Environment Variables

### Railway
1. railway.app → New Project → Deploy from GitHub
2. Добавь переменную `BOT_TOKEN`

## ⚙️ Настройки (.env)

| Переменная | По умолчанию |
|------------|--------------|
| BOT_TOKEN | Обязательно |
| HER_NAME | Арина |
| HIS_NAME | Никита |

## 📁 Структура

```
date_manager_bot/
├── bot.py
├── config.py
├── .env
├── .env.example
├── requirements.txt
├── Procfile
├── photos/ (1-8.jpg)
└── .gitignore
```

---

*Сделано с 💕*
