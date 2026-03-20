import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN', '')
HER_NAME = os.getenv('HER_NAME', 'Арина')
HIS_NAME = os.getenv('HIS_NAME', 'Никита')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PHOTOS_DIR = os.path.join(BASE_DIR, 'photos')

LOCATIONS = [
    ("☕ Уютная кофейня", "Как насчёт ароматного капучино в тёплой атмосфере?"),
    ("🌳 Парк", "Прогулка под звёздами — что может быть романтичнее?"),
    ("✨ Секретное место", "Специальное место... поверь, тебе понравится!")
]
