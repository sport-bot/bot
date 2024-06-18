import random
from aiogram.enums.parse_mode import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from aiogram.utils.i18n import gettext as _


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

        await bot.send_message(chat_id=users[i].tg_id, text=_('''
<b>Breakfast - {breakfast_name}</b>

You need: {breakfast_ingredients}

<i>Protein:</i> {breakfast_protein}
<i>Fat:</i> {breakfast_fat}
<i>Carbs:</i> {breakfast_carbs}
<b>Total: {breakfast_calories} cal</b>


<b>Lunch - {lunch_name}</b>

You need: {lunch_ingredients}

<i>Protein:</i> {lunch_protein}
<i>Fat:</i> {lunch_fat}
<i>Carbs:</i> {lunch_carbs}
<b>Total: {lunch_calories} cal</b>


<b>Dinner - {dinner_name}</b>

You need: {dinner_ingredients}

<i>Protein:</i> {dinner_protein}
<i>Fat:</i> {dinner_fat}
<i>Carbs:</i> {dinner_carbs}
<b>Total: {dinner_calories} cal</b>
''').format(
    breakfast_name=breakfast.name,
    breakfast_ingredients=breakfast.ingredients,
    breakfast_protein=breakfast.protein,
    breakfast_fat=breakfast.fat,
    breakfast_carbs=breakfast.carbs,
    breakfast_calories=breakfast.calories,
    
    lunch_name=lunch.name,
    lunch_ingredients=lunch.ingredients,
    lunch_protein=lunch.protein,
    lunch_fat=lunch.fat,
    lunch_carbs=lunch.carbs,
    lunch_calories=lunch.calories,
    
    dinner_name=dinner.name,
    dinner_ingredients=dinner.ingredients,
    dinner_protein=dinner.protein,
    dinner_fat=dinner.fat,
    dinner_carbs=dinner.carbs,
    dinner_calories=dinner.calories,
), parse_mode=ParseMode.HTML)


def schedule_daily_meals():
    scheduler = AsyncIOScheduler(timezone="Europe/Kiev")
    scheduler.add_job(send_daily_meals, trigger="cron", hour=9, minute=00, start_date=datetime.now())
    scheduler.start()