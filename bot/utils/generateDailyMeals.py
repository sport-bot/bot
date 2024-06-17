import random
from aiogram.enums.parse_mode import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

from bot.setup import bot
from bot.db.models.UserModel import User
from bot.db.models.MealModel import Meal

import bot.db.services.MealService as mealService
import bot.db.services.UserService as userService


async def send_daily_meals():
    print("sending daily meal recommendation")
    users: list[User] = await userService.get_all_users()

    meals: list[Meal] = await mealService.get_all()

    breakfasts = [meal for meal in meals if meal.meal_time == "Breakfast"]
    lunches = [meal for meal in meals if meal.meal_time == "Lunch"]
    dinners = [meal for meal in meals if meal.meal_time == "Dinner"]

    for i in range(len(users)):
        breakfast = random.choice(breakfasts)
        lunch = random.choice(lunches)
        dinner = random.choice(dinners)

        await bot.send_message(chat_id=users[i].tg_id, text=f'''
<b>Breakfast - {breakfast.name}</b>

You need: {breakfast.ingredients}

<i>Protein:</i> {breakfast.protein}
<i>Fat:</i> {breakfast.fat}
<i>Carbs:</i> {breakfast.carbs}
<b>Total: {breakfast.calories} cal</b>


<b>Lunch - {lunch.name}</b>

You need: {lunch.ingredients}

<i>Protein:</i> {lunch.protein}
<i>Fat:</i> {lunch.fat}
<i>Carbs:</i> {lunch.carbs}
<b>Total: {lunch.calories} cal</b>


<b>Dinner - {dinner.name}</b>

You need: {dinner.ingredients}

<i>Protein:</i> {dinner.protein}
<i>Fat:</i> {dinner.fat}
<i>Carbs:</i> {dinner.carbs}
<b>Total: {dinner.calories} cal</b>
''', parse_mode=ParseMode.HTML)


def schedule_daily_meals():
    scheduler = AsyncIOScheduler(timezone="Europe/Kiev")
    scheduler.add_job(send_daily_meals, trigger="cron", hour=9, minute=00, start_date=datetime.now())
    scheduler.start()