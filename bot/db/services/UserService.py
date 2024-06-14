from bot.db.db import async_session
from bot.db.models.UserModel import User
from sqlalchemy import select, update, delete


async def get_user(tg_id: int):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == tg_id))


async def create_user(tg_id: int, name: str, gender: str, age: int, weight: float, height: int, fitness_level: str, goal: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, name=name, gender=gender, age=age, weight=weight, height=height, fitness_level=fitness_level, goal=goal))
            await session.commit()

async def update_user(tg_id: str, name: str, gender: str, age: int, weight: float, height: int, fitness_level: str, goal: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            print("User with tg", tg_id, "not found")
            return None

        user.name = name
        user.gender = gender
        user.age = age
        user.weight = weight
        user.height = height
        user.fitness_level = fitness_level
        user.goal = goal

        await session.commit()
