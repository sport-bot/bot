import random
from aiogram.enums.parse_mode import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

from bot.setup import bot
from bot.db.models.UserModel import User
from bot.db.models.MealRecommendationModel import MealRecommendation

import bot.db.services.MealRecommendationService as mealRecommendationService
import bot.db.services.UserService as userService

def get_random_recommendation(recommendations: list[MealRecommendation], target_type):
    filtered_recommendations = [rec for rec in recommendations if rec.type == target_type]
    
    if not filtered_recommendations:
        return None
    
    return random.choice(filtered_recommendations)

async def send_daily_recommendation():
    print("sending daily meal recommendation")
    users: list[User] = await userService.get_all_users()

    meal_recommendations: list[MealRecommendation] = await mealRecommendationService.get_all_recommendations()

    for i in range(len(users)):
        recommendation: MealRecommendation = get_random_recommendation(meal_recommendations, users[i].goal)
        await bot.send_message(chat_id=users[i].tg_id, text=f"{recommendation.name}:\n<b>{recommendation.recommendation}</b>", parse_mode=ParseMode.HTML)


def start_day_sending():
    scheduler = AsyncIOScheduler(timezone="Europe/Kiev")
    scheduler.add_job(send_daily_recommendation, trigger="cron", hour=18, minute=30, start_date=datetime.now())
    scheduler.start()