import json
path = "posts.json"


def load_data():
    """Загружает данные из файла"""
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


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
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_post(post):
    """Добавляет пост"""
    posts = load_data()
    posts.append(post)
    save_posts_js(posts)

