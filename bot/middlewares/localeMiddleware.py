from aiogram.utils.i18n import I18nMiddleware
from aiogram.types import TelegramObject, Message
from typing import Callable, Dict, Any, Awaitable

import bot.db.services.UserService as userService

class GetLocaleMiddleware(I18nMiddleware):
    async def get_locale(self,
                       event: Message,
                       data: Dict[str, Any]):
        user = await userService.get_user(event.from_user.id)
        
        if not user:
            return 'en'
        
        return user.lang