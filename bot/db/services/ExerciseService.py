from bot.db.db import async_session
from bot.db.models.ExerciseModel import Exercise
from sqlalchemy import select, update, delete


async def create_exercise(name: str, description: str, video_id: str, level: str, types: list[str]):
    async with async_session() as session:
        session.add(Exercise(name=name, description=description, video_id=video_id, level=level, types=types))
        await session.commit()
