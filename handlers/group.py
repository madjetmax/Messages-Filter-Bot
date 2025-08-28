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

# # start command
# @router.message(CommandStart())
# async def start(message: Message, state: FSMContext):
#     await message.answer(
#         "Enter text"
#     )
#     # set state
#     await state.clear()
#     await state.set_state(TextParseState.text)

# # get text to parse
# @router.message(F.text, TextParseState.text)
# async def get_text(message: Message, state: FSMContext):
#     print(11)
#     await message.answer(
#         "Enter keywords <em>(kw1, kw2, kw3)</em> or .", parse_mode="HTML"
#     )
#     # update and set state
#     await state.update_data(
#         text=message.text   
#     )
#     await state.set_state(TextParseState.keywords)
# # get keywords
# @router.message(F.text, TextParseState.keywords)
# async def get_keywords(message: Message, state: FSMContext):
#     await message.answer(
#         "Enter names <em>(name1, name2, name3)</em> or .", parse_mode="HTML"
#     )
#     # update and set state
#     keywords = []
#     if message.text != ".":
#         keywords = message.text.replace(" ", "").split(",")

#     await state.update_data(
#         keywords=keywords
#     )
#     await state.set_state(TextParseState.names)

# # get names
# @router.message(F.text, TextParseState.names)
# async def get_names(message: Message, state: FSMContext):
#     await message.answer(
#         "Enter phrases <em>(some phrase1, some phrase2, some phrase3)</em> or .", parse_mode="HTML"
#     )
#     # update and set state
#     names = []
#     if message.text != ".":
#         names = message.text.replace(" ", "").split(",")
        
#     await state.update_data(
#         names=names
#     )
#     await state.set_state(TextParseState.phrases)

# # get phrases and send result
# @router.message(F.text, TextParseState.phrases)
# async def get_phrases(message: Message, state: FSMContext):
#     # update state and get data
#     phrases = []
#     if message.text != ".":
#         phrases = list(map(lambda x: x.strip(), message.text.split(",")))
#     state_data = await state.update_data(
#         phrases=phrases
#     )
#     # get parsed text data based on state_data
#     parse_result = parse_text(
#         state_data["text"], 
#         # triggers
#         state_data["keywords"],
#         state_data["names"], 
#         state_data["phrases"],
#     )
#     # get result
#     parsed_text = parse_result["parsed_text"]    
#     keywords_result = parse_result["keywords"]    
#     names_result = parse_result["names"]    
#     phrases_result = parse_result["phrases"]  

#     # send message  
#     text = f"""
# prsed_text: {parsed_text}
# keywords: {keywords_result}
# names: {names_result}
# phrases: {phrases_result}
# """
#     await message.answer(text)

