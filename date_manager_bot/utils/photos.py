import os
import random
from config import PHOTOS_DIR


def get_random_photo():
    photos = [f for f in os.listdir(PHOTOS_DIR) 
              if f.endswith(('.jpg', '.png', '.jpeg'))]
    if photos:
        return os.path.join(PHOTOS_DIR, random.choice(photos))
    return None


def get_photo_by_number(num):
    path = os.path.join(PHOTOS_DIR, f"{num}.jpg")
    return path if os.path.exists(path) else get_random_photo()
