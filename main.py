from typing import Final
import asyncio
from aiogram import Bot, Dispatcher

from bot.handlers.authHandlers import router
from bot.db.db import async_main


TOKEN: Final = "6596751567:AAE2SonIff-ZrvSEfmqpP4Hp2v_7dZRJehE"

BOT_USERNAME: Final = "@sportTestty_bot"


async def main():
    await async_main()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is turned off")