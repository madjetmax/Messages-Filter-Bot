from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Filter

from config import *
import config
from utils.parse_text import parse_text

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

# check message 
@router.message(MessageFilter())
@router.edited_message(MessageFilter())
async def check_message(message: Message):
    user = message.from_user
    parse_result = parse_text(
        message.text, 
        # triggers
        [kw[1] for kw in config.KEYWORDS_TRIGGERS],
        [name[1] for name in config.NAMES_TRIGGERS],
        [phrase[1] for phrase in config.PHRASES_TRIGGERS]
    )
    # get result
    parsed_text = parse_result["parsed_text"]    
    triggered_by = parse_result["triggered_dy"]
    # send message  
    text = f"""
prsed_text: {parsed_text}
triggered_by: {triggered_by}
user: {user.full_name}
"""
    await message.answer(text)
    # delete message
    if triggered_by:
        await message.delete()
