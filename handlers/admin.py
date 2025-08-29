from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
# packages
import config
from config import *
from fsm_states import admin as states
from keydoards import admin as kbs
import database as db
from middlewares.admin import HandlersMiddleware
from utils.parse_text import normalize

router = Router()
router.message.middleware.register(HandlersMiddleware())


# get admin main menu
@router.message(Command("admin"))
async def get_menu(message: Message, state: FSMContext):
    # get kb send message
    kb = kbs.main_menu_kb
    text = ADMIN_MENU_TITILE
    await message.answer(text, reply_markup=kb)

# new keyword
@router.message(F.text, states.AdminTriggersSetting.add_keywords)
async def new_keywords(message: Message, state: FSMContext):
    # send message 
    kb = kbs.keywords_setting_kb
    text = ADMIN_KEYWORDS_TITLE
    await message.answer(text, reply_markup=kb)

    # quit on .
    if message.text == ".":
        return

    # get and add keywords
    keywords = message.text.replace(" ", "").split(",")
    for kw in keywords:
        if kw:
            # add to database
            new_keyword = await db.add_keyword(
                kw
            )
            # add to config 
            config.KEYWORDS_TRIGGERS.append(
                (new_keyword.id, new_keyword.word)
            )
    await state.clear()

# new trigger name
@router.message(F.text, states.AdminTriggersSetting.add_trigger_names)
async def new_trigger_names(message: Message, state: FSMContext):
    # send message 
    kb = kbs.trigger_names_setting_kb
    text = ADMIN_TIGGER_NAMES_TITLE
    await message.answer(text, reply_markup=kb)

    # quit on .
    if message.text == ".":
        return

    # get and add names
    names = message.text.replace(" ", "").split(",")
    for name in names:
        if name:
            # add to database
            new_name = await db.add_trigger_name(name)
            # add to config 
            config.NAMES_TRIGGERS.append(
                (new_name.id, new_name.name)
            )
    await state.clear()

# new phrases
@router.message(F.text, states.AdminTriggersSetting.add_phrases)
async def new_phrases(message: Message, state: FSMContext):
    # send message 
    kb = kbs.phrases_setting_kb
    text = ADMIN_PHRASES_TITLE
    await message.answer(text, reply_markup=kb)

    # quit on .
    if message.text == ".":
        return

    # get and add phrases
    phrases = list(map(lambda x: x.strip(), message.text.split(",")))
    for phrase in phrases:
        if phrase:
            # add to database
            new_phrase = await db.add_phrase(phrase)
            # add to config 
            config.PHRASES_TRIGGERS.append(
                (
                    new_phrase.id, new_phrase.text,
                    # collect phrase into full string
                    "".join(normalize(word) for word in new_phrase.text.split(" "))
                )
            )
    await state.clear()