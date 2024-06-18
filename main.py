
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.utils.i18n import I18n
from pathlib import Path

from bot.handlers.authHandlers import router as authRouter
from bot.handlers.mainHandlers import router as mainRouter
from bot.handlers.trainingsHandlers import router as trainingsRouter
from bot.handlers.adminHandlers import router as adminRouter
from bot.handlers.settingsHandlers import router as settingseRouter

from bot.setup import bot

from bot.db.db import async_main
from bot.utils.dailyMealRecommendation import schedule_daily_meal_recommendation
from bot.utils.generateDailyMeals import schedule_daily_meals
from bot.utils.recountSubscriptionAccess import schedule_recount_access
from bot.utils.randomiseMotivationFrase import schedule_daily_motivation

from bot.middlewares.localeMiddleware import GetLocaleMiddleware


async def main():
    await async_main()

    schedule_daily_meal_recommendation()
    schedule_daily_meals()
    schedule_recount_access()
    schedule_daily_motivation()

    WORKDIR = Path(__file__).parent
    
    i18n = I18n(path=WORKDIR / 'locales', default_locale='en', domain='messages')
    
    dp = Dispatcher()
    
    dp.include_router(authRouter)
    dp.include_router(mainRouter)
    dp.include_router(trainingsRouter)
    dp.include_router(adminRouter)
    dp.include_router(settingseRouter)
    
    GetLocaleMiddleware(i18n=i18n).setup(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is turned off")