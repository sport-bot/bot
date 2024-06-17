from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from typing import Callable, Dict, Any, Awaitable

import bot.db.services.UserService as userService

class CheckAdminRoleMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]):
        user = await userService.get_user(event.from_user.id)

        if (user.is_admin):
            result = await handler(event, data)
            return result
        
        await event.answer("Not supported command")