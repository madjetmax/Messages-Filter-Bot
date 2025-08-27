from dotenv import load_dotenv
import os
import json
load_dotenv()

# bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = json.loads(os.getenv("ADMINS")) # ids
USERS_EXCEPTIONS = json.loads(os.getenv("USERS_EXCEPTIONS")) # ids
GROUP_ID = int(os.getenv("GROUP_ID"))

# dababase
DB_NAME = "database.db"
DB_URL = f"sqlite+aiosqlite:///{DB_NAME}"
DB_LOGGING = False

MODELS_TIME_ZONE = "UTC"

# admin menu texts
ADMIN_MENU_TITILE = "Админка"
ADMIN_KEYWORDS_TITLE = "Ключевые Слова"
ADMIN_TIGGER_NAMES_TITLE = "Триггерные Имена"
ADMIN_PHRASES_TITLE = "Фразы"
# todo ---------------------------
ALL_KEYWORDS_BTN = "Все Ключевые Слова"
ADD_KEYWORDS_BTN = "Добавить Ключевые Слова"
EMPTY_KEYWORDS_CALLBACK_ANS = "Ключевые Слова не Добавлены"
ADD_KEYWORDS_TITLE = """
Отправте слова в фотмате: <em>слово1, слово2, слово3 ...</em>
Для отмены отправте "."
Добаленные ключевые слова: {keywords}
"""
ADD_KEYWORDS_TITLE_EMPTY = """
Отправте слова в фотмате: <em>слово1, слово2, слово3 ...</em>
Для отмены отправте "."
"""
# todo ---------------------------
ALL_TIGGER_NAMES_BTN = "Все Триггерные Имена"
ADD_TIGGER_NAMES_BTN = "Добавить Триггерные Имена"
EMPTY_TRIGGER_NAMES_CALLBACK_ANS = "Триггерные Имена не Добавлены"
ADD_TRIGGER_NAMES_TITLE = """
Отправте имена в фотмате: <em>имя1, имя2, имя3 ...</em>
Для отмены отправте "."
Добаленные имена: {trigger_names}
"""
ADD_TRIGGER_NAMES_TITLE_EMPTY = """
Отправте имена в фотмате: <em>имя1, имя2, имя3 ...</em>
Для отмены отправте "."
"""
# todo ---------------------------
ALL_PHRASES_BTN = "Все Фразы"
ADD_PHRASES_BTN = "Добавить Фразы"
EMPTY_PHRASES_CALLBACK_ANS = "Фразы не Добавлены"
ADD_PHRASES_TITLE = """
Отправте фразы в фотмате: <em>первая фраза, вторая фраза ...</em>
Для отмены отправте "."
Добаленные фразы: {phrases}
"""
ADD_PHRASES_TITLE_EMPTY = """
Отправте фразы в фотмате: <em>первая фраза, вторая фраза ...</em>
Для отмены отправте "."
"""
# todo ---------------------------
DELETE_BTN = "Удилить ❌"
BACK_BTN = "Назад ⬅️"

# triggers and text parsing
KEYWORDS_TRIGGERS = []
NAMES_TRIGGERS = []
PHRASES_TRIGGERS = []

LETTER_MATCH = {
    "a": "а", "@": "а",
    "o": "о", "0": "о", "ö": "о",
    "e": "е", "3": "е", "ё": "е",
    "i": "и", "1": "и", "l": "и",
    "u": "у", "y": "у",
    
    "c": "с", "¢": "с",
    "p": "р",
    "x": "х",
    "k": "к",
    "b": "в", "6": "в",
    "m": "м",
    "h": "н", "n": "н",
    "$": "с",
}