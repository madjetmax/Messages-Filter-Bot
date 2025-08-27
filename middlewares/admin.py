from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject, ChatMemberUpdated, CallbackQuery
from config import *

from typing import Any, Coroutine, Dict, Callable, Awaitable

# for messages, commands
class HandlersMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        # check if user is admin and chat is private      
        if event.from_user.id in ADMINS and event.chat.type == "private":
            return await handler(event, data)
        return 

# for callbacks
class CallbacksMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        # check if user is admin and chat is private      
        if event.from_user.id in ADMINS and event.message.chat.type == "private":
            return await handler(event, data)
        return 

