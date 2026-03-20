"""
Менеджер Свидания - Telegram Bot
"""

import telebot
import logging
import sys
import os
import random
from datetime import datetime
from config import BOT_TOKEN, HER_NAME, HIS_NAME, PHOTOS_DIR, LOCATIONS

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('date_manager.log', encoding='utf-8')
    ]
)

logger = logging.getLogger(__name__)
bot = telebot.TeleBot(BOT_TOKEN)

user_data = {}


def get_random_photo():
    photos = [f for f in os.listdir(PHOTOS_DIR) if f.endswith(('.jpg', '.png', '.jpeg'))]
    return os.path.join(PHOTOS_DIR, random.choice(photos)) if photos else None


def get_photo_by_number(num):
    path = os.path.join(PHOTOS_DIR, f"{num}.jpg")
    return path if os.path.exists(path) else get_random_photo()


def send_photo_with_text(chat_id, text, photo=None, reply_markup=None, parse_mode='Markdown'):
    if photo:
        try:
            with open(photo, 'rb') as f:
                bot.send_photo(chat_id, f, caption=text, parse_mode=parse_mode, reply_markup=reply_markup)
        except Exception as e:
            logger.error(f"Photo error: {e}")
            bot.send_message(chat_id, text, parse_mode=parse_mode, reply_markup=reply_markup)
    else:
        bot.send_message(chat_id, text, parse_mode=parse_mode, reply_markup=reply_markup)


def main_menu_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, selective=True)
    
    buttons = [
        telebot.types.KeyboardButton("📍 Локация"),
        telebot.types.KeyboardButton("👗 Дресс-код"),
        telebot.types.KeyboardButton("🎁 Бонус"),
        telebot.types.KeyboardButton("🎫 Билет"),
        telebot.types.KeyboardButton("💕 Главное меню")
    ]
    
    keyboard.add(*buttons[:2])
    keyboard.add(*buttons[2:4])
    keyboard.add(buttons[4])
    
    return keyboard


def back_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    keyboard.add(telebot.types.KeyboardButton("⬅️ Назад"))
    return keyboard


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    
    photo = get_random_photo()
    welcome_text = f"""💕 *Привет, {HER_NAME}!*

Я — твой персональный менеджер свидания!
Давай спланируем наш идеальный вечер ✨

━━━━━━━━━━━━━━━━━━━━━━
📍 Выбрать локацию
👗 Дресс-код  
🎁 Секретный бонус
🎫 Получить билет
━━━━━━━━━━━━━━━━━━━━━━"""

    send_photo_with_text(chat_id, welcome_text, photo, main_menu_keyboard())


@bot.message_handler(func=lambda m: m.text == "⬅️ Назад" or m.text == "💕 Главное меню")
def back_to_main(message):
    chat_id = message.chat.id
    
    photo = get_random_photo()
    menu_text = f"""💕 *Главное меню*

Выбери, что хочешь настроить:
"""

    send_photo_with_text(chat_id, menu_text, photo, main_menu_keyboard())


@bot.message_handler(func=lambda m: m.text == "📍 Локация")
def location_handler(message):
    chat_id = message.chat.id
    
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    keyboard.add(telebot.types.KeyboardButton("☕ Кофейня"))
    keyboard.add(telebot.types.KeyboardButton("🌳 Парк"))
    keyboard.add(telebot.types.KeyboardButton("✨ Необычное место"))
    keyboard.add(telebot.types.KeyboardButton("⬅️ Назад"))
    
    photo = get_random_photo()
    text = f"""📍 *Выбери локацию*

Где мы проведём наш вечер?
"""
    
    send_photo_with_text(chat_id, text, photo, keyboard)


@bot.message_handler(func=lambda m: m.text == "☕ Кофейня")
def coffee_selected(message):
    chat_id = message.chat.id
    user_data[chat_id]['location'] = "☕ Уютная кофейня"
    
    photo = get_photo_by_number(random.randint(1, 8))
    text = f"""☕ *Кофейня выбрана!*

Как насчёт ароматного капучино 
в тёплой атмосфере? 

💫 Записала в план!"""

    send_photo_with_text(chat_id, text, photo, main_menu_keyboard())


@bot.message_handler(func=lambda m: m.text == "🌳 Парк")
def park_selected(message):
    chat_id = message.chat.id
    user_data[chat_id]['location'] = "🌳 Парк"
    
    photo = get_photo_by_number(random.randint(1, 8))
    text = f"""🌳 *Парк выбран!*

Прогулка под звёздами — 
что может быть романтичнее?

💫 Записала в план!"""

    send_photo_with_text(chat_id, text, photo, main_menu_keyboard())


@bot.message_handler(func=lambda m: m.text == "✨ Необычное место")
def secret_selected(message):
    chat_id = message.chat.id
    user_data[chat_id]['location'] = "✨ Секретное место"
    
    photo = get_photo_by_number(random.randint(1, 8))
    text = f"""✨ *Секретное место!*

Специальное место... 
Поверь, тебе понравится! 💕

💫 Записала в план!"""

    send_photo_with_text(chat_id, text, photo, main_menu_keyboard())


@bot.message_handler(func=lambda m: m.text == "👗 Дресс-код")
def dress_code_handler(message):
    chat_id = message.chat.id
    
    photo = get_photo_by_number(random.randint(1, 8))
    text = f"""👗 *Дресс-код*

Надень то, в чём тебе удобно 
и комфортно...

Я всё равно буду смотреть 
только в твои глаза 💕"""

    send_photo_with_text(chat_id, text, photo, main_menu_keyboard())


@bot.message_handler(func=lambda m: m.text == "🎁 Бонус")
def bonus_handler(message):
    chat_id = message.chat.id
    
    photo = get_photo_by_number(random.randint(1, 8))
    text = f"""🎁 *Секретный бонус активирован!*

Теперь при встрече ты 
обязана поцеловать меня 
в щёчку 💋

*Шутка!* 
(Или нет... 😏)"""

    send_photo_with_text(chat_id, text, photo, main_menu_keyboard())


@bot.message_handler(func=lambda m: m.text == "🎫 Билет")
def ticket_handler(message):
    chat_id = message.chat.id
    now = datetime.now()
    
    location = user_data.get(chat_id, {}).get('location', "✨ Секретное место")
    
    photo = get_photo_by_number(random.randint(1, 8))
    text = f"""🎫 *БИЛЕТ НА СВИДАНИЕ* 🎫

━━━━━━━━━━━━━━━━━━━━━━

👫 *Участники:*
{HIS_NAME} 💕 {HER_NAME}

📅 *Дата:* {now.strftime('%d.%m.%Y')}
🕐 *Время:* 19:00
📍 *Место:* {location}

━━━━━━━━━━━━━━━━━━━━━━

✨ *Особые отметки:*
• Обязательно улыбаться!
• Секретный бонус активен
• Ждём невероятный вечер!

━━━━━━━━━━━━━━━━━━━━━━

🎟️ *Действителен при предъявлении 
хорошего настроения* 💕"""

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    keyboard.add(telebot.types.KeyboardButton("🎫 Ещё билет"))
    keyboard.add(telebot.types.KeyboardButton("💕 Главное меню"))
    
    send_photo_with_text(chat_id, text, photo, keyboard)


@bot.message_handler(func=lambda m: m.text == "🎫 Ещё билет")
def another_ticket(message):
    ticket_handler(message)


@bot.message_handler(func=lambda message: True)
def echo(message):
    if message.text and message.text.startswith('/'):
        return
    
    photo = get_random_photo()
    responses = [
        "Я здесь, чтобы планировать наше свидание! 💕",
        "Давай лучше спланируем вечер? ✨",
        "Наше свидание ждёт! 💫"
    ]
    
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    keyboard.add(telebot.types.KeyboardButton("💕 Главное меню"))
    
    send_photo_with_text(message.chat.id, random.choice(responses), photo, keyboard)


def main():
    try:
        if BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
            logger.error("❌ Установите токен бота в .env!")
            return
        
        logger.info(f"🎉 Менеджер Свидания запущен!")
        logger.info(f"Для {HER_NAME} от {HIS_NAME} 💕")
        
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
        
    except KeyboardInterrupt:
        logger.info("\n🛑 Бот остановлен")
    except Exception as e:
        logger.error(f"❌ Ошибка: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
