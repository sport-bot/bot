from bot.db.db import async_session
from bot.db.models.UserModel import User
from sqlalchemy import select, update, delete


async def get_user(tg_id: int):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == tg_id))

async def get_all_users():
    async with async_session() as session:
        return (await session.scalars(select(User))).all()

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

        if name: user.name = name
        if gender: user.gender = gender
        if age: user.age = age
        if weight: user.weight = weight
        if height: user.height = height
        if fitness_level: user.fitness_level = fitness_level
        if goal: user.goal = goal

        await session.commit()

async def decrease_free_days(tg_id: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            print("User with tg", tg_id, "not found")
            return None
        
        user.free_days_left -= 1

        await session.commit()

async def decrease_subscription_days(tg_id: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            print("User with tg", tg_id, "not found")
            return None
        
        user.subscription_days_left -= 1

        await session.commit()