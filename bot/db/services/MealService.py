from bot.db.db import async_session
from bot.db.models.MealModel import Meal
from sqlalchemy import select


async def create_meal(name: str, ingredients: str, meal_time: str, calories: float, protein: float, fat: float, carbs: float):
    async with async_session() as session:
        session.add(Meal(name=name, ingredients=ingredients, meal_time=meal_time, calories=calories, protein=protein, fat=fat, carbs=carbs))
        await session.commit()

async def get_all():
    async with async_session() as session:
        return (await session.scalars(select(Meal))).all()

