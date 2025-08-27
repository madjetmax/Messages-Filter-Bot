from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *

main_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=ADMIN_KEYWORDS_TITLE, callback_data="ad_setting_keywords")],
    [InlineKeyboardButton(text=ADMIN_TIGGER_NAMES_TITLE, callback_data="ad_setting_names")],
    [InlineKeyboardButton(text=ADMIN_PHRASES_TITLE, callback_data="ad_setting_phrases")],
])

# * setting triggers
# keywords
keywords_setting_kb  = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=ALL_KEYWORDS_BTN, callback_data="ad_get_all_keywords")],
    [InlineKeyboardButton(text=ADD_KEYWORDS_BTN, callback_data="ad_add_keywords")],
    # back btn
    [InlineKeyboardButton(text=BACK_BTN, callback_data="ad_back_main")],
])

def get_delete_keyword_kb(keyword_id: int, add_back_btn: bool) -> InlineKeyboardMarkup: 
    rows = [
        [InlineKeyboardButton(text=DELETE_BTN, callback_data=f"ad_delete_keyword_{keyword_id}")],
    ]
    if add_back_btn:
        rows.append([InlineKeyboardButton(text=BACK_BTN, callback_data="ad_back_keywords")])

    return InlineKeyboardMarkup(inline_keyboard=rows)

# tigger names
trigger_names_setting_kb  = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=ALL_TIGGER_NAMES_BTN, callback_data="ad_get_all_names")],
    [InlineKeyboardButton(text=ADD_TIGGER_NAMES_BTN, callback_data="ad_add_names")],
    # back btn
    [InlineKeyboardButton(text=BACK_BTN, callback_data="ad_back_main")],
])

def get_delete_trigger_name_kb(trigger_name_id: int, add_back_btn: bool) -> InlineKeyboardMarkup: 
    rows = [
        [InlineKeyboardButton(text=DELETE_BTN, callback_data=f"ad_delete_name_{trigger_name_id}")],
    ]
    if add_back_btn:
        rows.append([InlineKeyboardButton(text=BACK_BTN, callback_data="ad_back_names")])

    return InlineKeyboardMarkup(inline_keyboard=rows)

# phrases
phrases_setting_kb  = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=ALL_PHRASES_BTN, callback_data="ad_get_all_phrases")],
    [InlineKeyboardButton(text=ADD_PHRASES_BTN, callback_data="ad_add_phrases")],
    # back btn
    [InlineKeyboardButton(text=BACK_BTN, callback_data="ad_back_main")],
])

def get_delete_phrase_kb(phrase_id: int, add_back_btn: bool) -> InlineKeyboardMarkup: 
    rows = [
        [InlineKeyboardButton(text=DELETE_BTN, callback_data=f"ad_delete_phrase_{phrase_id}")],
    ]
    if add_back_btn:
        rows.append([InlineKeyboardButton(text=BACK_BTN, callback_data="ad_back_phrases")])

    return InlineKeyboardMarkup(inline_keyboard=rows)