"""
Date Manager Bot - Telegram Bot
"""
import telebot
import logging
import sys

from config import BOT_TOKEN, LOCATIONS
from handlers.commands import (
    handle_start, handle_back, handle_location,
    handle_dress_code, handle_bonus, handle_ticket,
    handle_echo, handle_location_selected
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('bot.log', encoding='utf-8')]
)

logger = logging.getLogger(__name__)
bot = telebot.TeleBot(BOT_TOKEN)
user_data = {}


def register_handlers():
    """Регистрация всех обработчиков"""
    
    @bot.message_handler(commands=['start'])
    def cmd_start(msg):
        handle_start(bot, msg)
    
    @bot.message_handler(func=lambda m: m.text in ["⬅️ Назад", "💕 Главное меню"])
    def cmd_back(msg):
        handle_back(bot, msg)
    
    @bot.message_handler(func=lambda m: m.text == "📍 Локация")
    def cmd_location(msg):
        handle_location(bot, msg)
    
    @bot.message_handler(func=lambda m: m.text == "☕ Кофейня")
    def cmd_coffee(msg):
        handle_location_selected(bot, msg, "☕ Уютная кофейня")
    
    @bot.message_handler(func=lambda m: m.text == "🌳 Парк")
    def cmd_park(msg):
        handle_location_selected(bot, msg, "🌳 Парк")
    
    @bot.message_handler(func=lambda m: m.text == "✨ Необычное место")
    def cmd_secret(msg):
        handle_location_selected(bot, msg, "✨ Секретное место")
    
    @bot.message_handler(func=lambda m: m.text == "👗 Дресс-код")
    def cmd_dress(msg):
        handle_dress_code(bot, msg)
    
    @bot.message_handler(func=lambda m: m.text == "🎁 Бонус")
    def cmd_bonus(msg):
        handle_bonus(bot, msg)
    
    @bot.message_handler(func=lambda m: m.text == "🎫 Билет")
    def cmd_ticket(msg):
        handle_ticket(bot, msg)
    
    @bot.message_handler(func=lambda m: m.text == "🎫 Ещё билет")
    def cmd_another_ticket(msg):
        handle_ticket(bot, msg)
    
    @bot.message_handler(func=lambda m: True)
    def cmd_echo(msg):
        if msg.text and not msg.text.startswith('/'):
            handle_echo(bot, msg)


def main():
    if not BOT_TOKEN:
        logger.error("Установите BOT_TOKEN в .env!")
        sys.exit(1)
    
    register_handlers()
    logger.info("Бот запущен!")
    
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except KeyboardInterrupt:
        logger.info("Бот остановлен")


if __name__ == '__main__':
    main()
