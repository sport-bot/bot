from bot.db.db import async_session
from bot.db.models.MealRecommendationModel import MealRecommendation
from sqlalchemy import select, update, delete


async def create_meal_recommendation(name: str, recommendation: str, type: str, lang: str):
    async with async_session() as session:
        session.add(MealRecommendation(name=name, recommendation=recommendation, type=type, lang=lang))
        await session.commit()

async def get_all_recommendations():
    async with async_session() as session:
        return (await session.scalars(select(MealRecommendation))).all()