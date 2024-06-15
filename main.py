
import asyncio
from aiogram import Bot, Dispatcher

from bot.handlers.authHandlers import router as authRouter
from bot.handlers.mainHandlers import router as mainRouter
from bot.handlers.trainingsHandlers import router as trainingsRouter
from bot.db.db import async_main
from bot.setup import bot


async def main():
    await async_main()
    dp = Dispatcher()

    dp.include_router(authRouter)
    dp.include_router(mainRouter)
    dp.include_router(trainingsRouter)
    
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is turned off")