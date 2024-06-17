import random
from aiogram.enums.parse_mode import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

from bot.setup import bot
from bot.db.models.UserModel import User
from bot.db.models.MealRecommendationModel import MealRecommendation

import bot.db.services.MealRecommendationService as mealRecommendationService
import bot.db.services.UserService as userService


async def recount_subscription_access():
    users: list[User] = await userService.get_all_users()

    for i in range(len(users)):
        if users[i].free_days_left > 0:
            await userService.decrease_free_days(users[i].tg_id)
        elif users[i].subscription_days_left > 0:
            await userService.decrease_subscription_days()
            

def schedule_recount_access():
    scheduler = AsyncIOScheduler(timezone="Europe/Kiev")
    scheduler.add_job(recount_subscription_access, trigger="cron", hour=12, minute=57, start_date=datetime.now())
    scheduler.start()