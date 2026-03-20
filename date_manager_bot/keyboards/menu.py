import telebot.types as types


def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    keyboard.add(
        types.KeyboardButton("📍 Локация"),
        types.KeyboardButton("👗 Дресс-код"),
        types.KeyboardButton("🎁 Бонус"),
        types.KeyboardButton("🎫 Билет"),
        types.KeyboardButton("💕 Главное меню")
    )
    
    return keyboard


def location_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    keyboard.add(types.KeyboardButton("☕ Кофейня"))
    keyboard.add(types.KeyboardButton("🌳 Парк"))
    keyboard.add(types.KeyboardButton("✨ Необычное место"))
    keyboard.add(types.KeyboardButton("⬅️ Назад"))
    
    return keyboard


def ticket_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    keyboard.add(types.KeyboardButton("🎫 Ещё билет"))
    keyboard.add(types.KeyboardButton("💕 Главное меню"))
    
    return keyboard


def back_button():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("⬅️ Назад"))
    return keyboard
