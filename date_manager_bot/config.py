# Менеджер Свидания - Configuration

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

HER_NAME = "Арина"
HIS_NAME = "Никита"

PHOTOS_DIR = os.path.join(os.path.dirname(__file__), 'photos')

LOCATIONS = [
    ("☕ Уютная кофейня", "Как насчёт ароматного капучино в тёплой атмосфере?"),
    ("🌳 Парк", "Прогулка под звёздами — что может быть романтичнее?"),
    ("✨ Что-то необычное", "Секретное место... поверь, тебе понравится!")
]

LOCATIONS_PHOTOS = {
    0: "coffee.jpg",
    1: "park.jpg", 
    2: "secret.jpg"
}
