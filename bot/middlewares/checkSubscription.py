from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from typing import Callable, Dict, Any, Awaitable
from aiogram.utils.i18n import gettext as _

import bot.db.services.UserService as userService

class CheckSubscriptionMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]):
        user = await userService.get_user(event.from_user.id)

        if (user.free_days_left > 0 or user.subscription_days_left > 0):
            result = await handler(event, data)
            return result
        
        await event.answer(_("Your subscription expired"))