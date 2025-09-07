from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Filter

from config import *
import config
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

    # delete message
    if triggered:
        await message.delete()

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
    
    # delete message
    if triggered:
        await message.delete()
