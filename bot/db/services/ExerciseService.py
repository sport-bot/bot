from bot.db.db import async_session
from bot.db.models.ExerciseModel import Exercise
from sqlalchemy import select, update, delete, func


async def create_exercise(name: str, technik_description: str, low_level_description: str, regular_level_description: str, high_level_description: str, video_id: str, type: str):
    async with async_session() as session:
        session.add(Exercise(name=name, technik_description=technik_description, low_level_description=low_level_description, regular_level_description=regular_level_description, high_level_description=high_level_description, video_id=video_id, type=type))
        await session.commit()

async def find_random_exercises(type: str, amount: int) -> list[Exercise]:
    async with async_session() as session:
        exercise = await session.scalars(
            select(Exercise)
            .where(Exercise.type == type)
            .order_by(func.random())
            .limit(amount)
        )
        return exercise.all()