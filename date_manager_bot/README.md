# Date Manager Bot

Telegram-бот для планирования идеального свидания.

## Структура

```
date_manager_bot/
├── bot.py              # Точка входа
├── config.py           # Конфигурация
├── handlers/
│   └── commands.py     # Обработчики команд
├── keyboards/
│   └── menu.py         # Клавиатуры
├── utils/
│   └── photos.py       # Работа с фото
├── photos/             # Фотографии (1-8.jpg)
└── .env                # Токен
```

## Запуск

```bash
pip install -r requirements.txt
cp .env.example .env
# Укажи BOT_TOKEN в .env
python bot.py
```

## Хостинг

### Render.com
1. GitHub → New → Web Service
2. Root Directory: `date_manager_bot`
3. Build: `pip install -r requirements.txt`
4. Start: `python bot.py`
5. Add `BOT_TOKEN` env var

### VPS
```bash
pip install -r requirements.txt
python bot.py
```
