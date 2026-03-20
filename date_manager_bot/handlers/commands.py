from config import HER_NAME, HIS_NAME
from keyboards.menu import main_menu, location_menu, ticket_menu
from utils.photos import get_random_photo, get_photo_by_number
import random


def handle_start(bot, message):
    from bot import user_data
    
    chat_id = message.chat.id
    user_data[chat_id] = {}
    
    photo = get_random_photo()
    text = f"""💕 *Привет, {HER_NAME}!*

Я — твой персональный менеджер свидания!
Давай спланируем наш идеальный вечер ✨

━━━━━━━━━━━━━━━━━━━━━━
📍 Выбрать локацию
👗 Дресс-код  
🎁 Секретный бонус
🎫 Получить билет
━━━━━━━━━━━━━━━━━━━━━━"""
    
    send_photo(bot, chat_id, text, photo, main_menu())


def handle_back(bot, message):
    chat_id = message.chat.id
    photo = get_random_photo()
    text = "💕 *Главное меню*\n\nВыбери, что хочешь настроить:"
    
    send_photo(bot, chat_id, text, photo, main_menu())


def handle_location(bot, message):
    chat_id = message.chat.id
    photo = get_random_photo()
    text = "📍 *Выбери локацию*\n\nГде мы проведём наш вечер?"
    
    send_photo(bot, chat_id, text, photo, location_menu())


def handle_location_selected(bot, message, loc_name):
    from bot import user_data
    
    chat_id = message.chat.id
    user_data[chat_id]['location'] = loc_name
    
    photo = get_photo_by_number(random.randint(1, 8))
    text = f"{loc_name} выбрано!\n\n💫 Записала в план!"
    
    send_photo(bot, chat_id, text, photo, main_menu())


def handle_dress_code(bot, message):
    chat_id = message.chat.id
    photo = get_photo_by_number(random.randint(1, 8))
    text = f"""👗 *Дресс-код*

Надень то, в чём тебе удобно и комфортно...

Я всё равно буду смотреть только в твои глаза 💕"""
    
    send_photo(bot, chat_id, text, photo, main_menu())


def handle_bonus(bot, message):
    chat_id = message.chat.id
    photo = get_photo_by_number(random.randint(1, 8))
    text = f"""🎁 *Секретный бонус активирован!*

Теперь при встрече ты обязана поцеловать меня в щёчку 💋

*Шутка!* (Или нет... 😏)"""
    
    send_photo(bot, chat_id, text, photo, main_menu())


def handle_ticket(bot, message):
    from bot import user_data
    from datetime import datetime
    
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

🎟️ *Действителен при предъявлении хорошего настроения* 💕"""
    
    send_photo(bot, chat_id, text, photo, ticket_menu())


def handle_echo(bot, message):
    photo = get_random_photo()
    responses = [
        "Я здесь, чтобы планировать наше свидание! 💕",
        "Давай лучше спланируем вечер? ✨",
        "Наше свидание ждёт! 💫"
    ]
    
    keyboard = main_menu()
    bot.send_message(message.chat.id, random.choice(responses), 
                     reply_markup=keyboard)


def send_photo(bot, chat_id, text, photo, keyboard=None):
    if photo:
        try:
            with open(photo, 'rb') as f:
                bot.send_photo(chat_id, f, caption=text, 
                             parse_mode='Markdown', reply_markup=keyboard)
        except:
            bot.send_message(chat_id, text, parse_mode='Markdown', 
                           reply_markup=keyboard)
    else:
        bot.send_message(chat_id, text, parse_mode='Markdown', 
                        reply_markup=keyboard)
