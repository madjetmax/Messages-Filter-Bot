from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Filter
import datetime 
from zoneinfo import ZoneInfo

from config import *
import config
from keydoards import admin as admin_kbs
from utils.parse_text import check_trigger

router = Router()

# filters
class MessageFilter(Filter):
    allowed_chat_types = ("group", "supergroup")
    async def __call__(self, message: Message) -> bool:
        return (
            message.text 
            # check chat type and id
            and message.chat.type in self.allowed_chat_types 
            and message.chat.id == GROUP_ID
            # check user is not in users exceptions
            and message.from_user.id not in USERS_EXCEPTIONS 
        )
    
def limit_string(s: str, max_len: int = 3000, suffix: str = "...") -> str:
    if len(s) <= max_len:
        return s
    # cut enough to fit suffix inside the limit
    return s[: max_len - len(suffix)] + suffix

# * check message
# if sent
@router.message(MessageFilter())
async def check_sent_message(message: Message):
    triggered = check_trigger(
        message.text, 
        # triggers
        config.CLEAR_KEYWORDS_TRIGGERS,
        config.CLEAR_NAMES_TRIGGERS,
        config.CLEAR_PHRASES_TRIGGERS,
    )

    if triggered:
        # delete message
        await message.delete()

        # send to admins
        user = message.from_user
        now: str = datetime.datetime.now(ZoneInfo(DATETIME_TIME_ZONE)).strftime("%H:%M.%S %d-%m-%Y")
        message_text = limit_string(message.text)

        if user.full_name:
            user_link = f"@{user.full_name}"
        else:
            first_name = user.first_name.capitalize() if user.first_name else ""
            last_name = user.last_name.capitalize() if user.last_name else ""

            user_link = f'<a href="tg://user?id={user.id}">{first_name} {last_name}</a>'

        text = TRIGGERED_MESSAGE_LOG.format(
            username=user_link,
            text=message_text,
            date_sent=now
        )
        kb = admin_kbs.get_ban_user_kb(user.id)

        for send_user in SEND_LOGS_USERS:
            await message.bot.send_message(
                send_user, text, reply_markup=kb, parse_mode="HTML",
                disable_notification=True,
            )

# if edited
@router.edited_message(MessageFilter())
async def check_edited_message(message: Message):
    triggered = check_trigger(
        message.text, 
        # triggers
        config.CLEAR_KEYWORDS_TRIGGERS,
        config.CLEAR_NAMES_TRIGGERS,
        config.CLEAR_PHRASES_TRIGGERS,
    )
    
    if triggered:
        # delete message
        await message.delete()

        # send to admins
        user = message.from_user
        now: str = datetime.datetime.now(ZoneInfo(DATETIME_TIME_ZONE)).strftime("%H:%M.%S %d-%m-%Y")
        message_text = limit_string(message.text)

        if user.full_name:
            user_link = f"@{user.full_name}"
        else:
            first_name = user.first_name.capitalize() if user.first_name else ""
            last_name = user.last_name.capitalize() if user.last_name else ""

            user_link = f'<a href="tg://user?id={user.id}">{first_name} {last_name}</a>'


        text = EDITED_TRIGGERED_MESSAGE_LOG.format(
            username=user_link,
            text=message_text,
            date_edited=now
        )
        kb = admin_kbs.get_ban_user_kb(user.id)

        for send_user in SEND_LOGS_USERS:
            await message.bot.send_message(
                send_user, text, reply_markup=kb, parse_mode="HTML",
                disable_notification=True,
            )

