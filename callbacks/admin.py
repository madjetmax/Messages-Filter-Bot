from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
import config
from config import *
# packages
from fsm_states import admin as states
from keydoards import admin as kbs
import database as db 
from database.models import Keyword, TriggerName, Phrase
from middlewares.admin import CallbacksMiddleware

router = Router()
router.callback_query.middleware.register(CallbacksMiddleware())


async def delete_messages(bot, chat_id: int, messages: list[int]):
    if messages:
        await bot.delete_messages(chat_id, messages)

# back to main 
@router.callback_query(F.data == "ad_back_main")
async def back_to_main(call: CallbackQuery):
    message = call.message
    # get kb and edit message
    kb = kbs.main_menu_kb
    text = ADMIN_MENU_TITILE
    await message.edit_text(text, reply_markup=kb)

# * tirggers setting
# * keywords
# back to keywords
@router.callback_query(F.data == "ad_back_keywords")
async def back_to_keywords(call: CallbackQuery, state: FSMContext):
    message = call.message
    chat_id = message.chat.id
    bot = message.bot
    state_data = await state.get_data()

    # delete messages to delete
    messages_to_delete = state_data.get("messages_to_delete")
    await delete_messages(bot, chat_id, messages_to_delete)

    # send message
    kb = kbs.keywords_setting_kb
    text = ADMIN_KEYWORDS_TITLE
    await message.answer(text, reply_markup=kb)

    await state.clear()

# settings
@router.callback_query(F.data == "ad_setting_keywords")
async def setting_keywords(call: CallbackQuery):
    message = call.message
    # edit message
    kb = kbs.keywords_setting_kb
    text = ADMIN_KEYWORDS_TITLE
    await message.edit_text(text, reply_markup=kb)

# get add delete
@router.callback_query(F.data == "ad_get_all_keywords")
async def get_all_keywords(call: CallbackQuery, state: FSMContext):
    message = call.message
    # get from db
    keywords: list[Keyword] = await db.get_all_keywords()
    keywords_len = len(keywords)
    # answer empty callback
    if keywords_len == 0:
        await call.answer(EMPTY_KEYWORDS_CALLBACK_ANS)
        return

    # send messages
    messages = []
    for i, kw in enumerate(keywords):
        kb = kbs.get_delete_keyword_kb(kw.id, (i+1 == keywords_len))
        text = kw.word
        msg = await message.answer(text, reply_markup=kb)
        messages.append(msg.message_id)

    await message.delete()

    # update state
    await state.clear()
    await state.set_state(states.MessagesClear)
    await state.update_data(messages_to_delete=messages)

@router.callback_query(F.data == "ad_add_keywords")
async def add_keywords(call: CallbackQuery, state: FSMContext):
    message = call.message
    # get text and edit message
    if len(config.KEYWORDS_TRIGGERS) > 0:
        text = config.ADD_KEYWORDS_TITLE.format(
            keywords=", ".join([kw[1] for kw in config.KEYWORDS_TRIGGERS])
        )
    else:
        text = config.ADD_KEYWORDS_TITLE_EMPTY

    await message.edit_text(
        text, parse_mode="HTML"
    )
    # update state
    await state.clear()
    await state.set_state(states.AdminTriggersSetting.add_keywords)

@router.callback_query(F.data.startswith("ad_delete_keyword_"))
async def delete_keyword(call: CallbackQuery):
    message = call.message
    keyword_id = int(call.data.replace("ad_delete_keyword_", ""))
    # delete message
    await message.delete()
    try:
        # delete in database
        await db.delete_keyword(keyword_id)
        # delete from config
        for i, kw in enumerate(config.KEYWORDS_TRIGGERS):
            if kw[0] == keyword_id:
                config.KEYWORDS_TRIGGERS.pop(i)
                break
    except: 
        pass

# * tigger names
# back to trigger names
@router.callback_query(F.data == "ad_back_names")
async def back_to_trigger_names(call: CallbackQuery, state: FSMContext):
    message = call.message
    chat_id = message.chat.id
    bot = message.bot
    state_data = await state.get_data()

    # delete messages to delete
    messages_to_delete = state_data.get("messages_to_delete")
    await delete_messages(bot, chat_id, messages_to_delete)

    # send message
    kb = kbs.trigger_names_setting_kb
    text = ADMIN_TIGGER_NAMES_TITLE
    await message.answer(text, reply_markup=kb)

    await state.clear()
# setting
@router.callback_query(F.data == "ad_setting_names")
async def setting_trigger_names(call: CallbackQuery):
    message = call.message
    # edit message
    kb = kbs.trigger_names_setting_kb
    text = ADMIN_TIGGER_NAMES_TITLE
    await message.edit_text(text, reply_markup=kb)

# get add delete
@router.callback_query(F.data == "ad_get_all_names")
async def get_all_trigger_names(call: CallbackQuery, state: FSMContext):
    message = call.message
    # get from db
    names: list[TriggerName] = await db.get_all_trigger_names()
    names_len = len(names)
    # answer empty callback
    if names_len == 0:
        await call.answer(EMPTY_TRIGGER_NAMES_CALLBACK_ANS)
        return
    # send messages
    messages = []
    for i, name in enumerate(names):
        kb = kbs.get_delete_trigger_name_kb(name.id, (i+1 == names_len))
        text = name.name
        msg = await message.answer(text, reply_markup=kb)
        messages.append(msg.message_id)

    await message.delete()

    # update state
    await state.clear()
    await state.set_state(states.MessagesClear)
    await state.update_data(messages_to_delete=messages)

@router.callback_query(F.data == "ad_add_names")
async def add_tigger_names(call: CallbackQuery, state: FSMContext):
    message = call.message
    # get text and edit message
    if len(config.NAMES_TRIGGERS) > 0:
        text = config.ADD_TRIGGER_NAMES_TITLE.format(
            trigger_names=", ".join([name[1] for name in config.NAMES_TRIGGERS])
        )
    else:
        text = config.ADD_TRIGGER_NAMES_TITLE_EMPTY

    await message.edit_text(
        text, parse_mode="HTML"
    )
    # update state
    await state.clear()
    await state.set_state(states.AdminTriggersSetting.add_trigger_names)

@router.callback_query(F.data.startswith("ad_delete_name_"))
async def delete_name(call: CallbackQuery):
    message = call.message
    name_id = int(call.data.replace("ad_delete_name_", ""))
    # delete message
    await message.delete()
    try:
        # delete in database
        await db.delete_trigger_name(name_id)
        # delete from config
        for i, name in enumerate(config.NAMES_TRIGGERS):
            if name[0] == name_id:
                config.NAMES_TRIGGERS.pop(i)
                break
    except: 
        pass

# * phrases
# back to phrases
@router.callback_query(F.data == "ad_back_phrases")
async def back_to_phrases(call: CallbackQuery, state: FSMContext):
    message = call.message
    chat_id = message.chat.id
    bot = message.bot
    state_data = await state.get_data()

    # delete messages to delete
    messages_to_delete = state_data.get("messages_to_delete")
    await delete_messages(bot, chat_id, messages_to_delete)

    # send message
    kb = kbs.phrases_setting_kb
    text = ADMIN_PHRASES_TITLE
    await message.answer(text, reply_markup=kb)

    await state.clear()
# setting
@router.callback_query(F.data == "ad_setting_phrases")
async def setting_phrases(call: CallbackQuery):
    message = call.message
    # edit message
    kb = kbs.phrases_setting_kb
    text = ADMIN_PHRASES_TITLE
    await message.edit_text(text, reply_markup=kb)

# get add delete
@router.callback_query(F.data == "ad_get_all_phrases")
async def get_all_phrases(call: CallbackQuery, state: FSMContext):
    message = call.message
    # get from db
    phrases: list[Phrase] = await db.get_all_phrases()
    phrases_len = len(phrases)
    # answer empty callback
    if phrases_len == 0:
        await call.answer(EMPTY_PHRASES_CALLBACK_ANS)
        return
    # send messages
    messages = []
    for i, phrase in enumerate(phrases):
        kb = kbs.get_delete_phrase_kb(phrase.id, (i+1 == phrases_len))
        text = phrase.text
        msg = await message.answer(text, reply_markup=kb)
        messages.append(msg.message_id)

    await message.delete()

    # update state
    await state.clear()
    await state.set_state(states.MessagesClear)
    await state.update_data(messages_to_delete=messages)

@router.callback_query(F.data == "ad_add_phrases")
async def add_phrases(call: CallbackQuery, state: FSMContext):
    message = call.message
    # get text and edit message
    if len(config.PHRASES_TRIGGERS) > 0:
        text = config.ADD_PHRASES_TITLE.format(
            phrases=", ".join([ph[1] for ph in config.PHRASES_TRIGGERS])
        )
    else:
        text = config.ADD_PHRASES_TITLE_EMPTY
    
    await message.edit_text(
        text, parse_mode="HTML"
    )
    # update state
    await state.clear()
    await state.set_state(states.AdminTriggersSetting.add_phrases)

@router.callback_query(F.data.startswith("ad_delete_phrase_"))
async def delete_phrase(call: CallbackQuery):
    message = call.message
    phrase_id = int(call.data.replace("ad_delete_phrase_", ""))
    # delete message
    await message.delete()
    try:
        # delete in database
        await db.delete_phrase(phrase_id)
        # delete from config
        for i, phrase in enumerate(config.PHRASES_TRIGGERS):
            if phrase[0] == phrase_id:
                config.PHRASES_TRIGGERS.pop(i)
                break
    except: 
        pass
