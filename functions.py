import json
import logging
from json import JSONDecodeError

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
logger = logging.getLogger('basiq')


def load_data():
    """Загружает данные из файла"""
    try:
        with open("posts.json", encoding='utf-8') as f:
            data = json.load(f)
            return data
    except(FileNotFoundError, JSONDecodeError):
        return "Не удается получить данные из data.json"


def get_all_data():
    """Отдает все данные из файла"""
    data = load_data()
    return data


def search_posts(substring):
    """Поиск по вхождению"""
    substring = substring.lower()
    founded_posts = []
    posts = load_data()
    for post in posts:
        if substring in post["content"].lower():
            founded_posts.append(post)
    return founded_posts


def save_posts_js(data):
    """Перезаписывает js файл с постами"""
    with open("posts.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_post(post):
    """Добавляет пост"""
    posts = load_data()
    posts.append(post)
    save_posts_js(posts)


def is_filename_allowed(filename):
    """Проверяем файл на расширения"""
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False
