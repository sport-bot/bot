from bot.db.db import async_session
from bot.db.models.MotivationFraseModel import MotivationFrase
from sqlalchemy import select, update, delete


async def create_motivation_frase(text: str, author: str):
    async with async_session() as session:
        session.add(MotivationFrase(text=text, author=author))
        await session.commit()

async def get_all():
    async with async_session() as session:
        return (await session.scalars(select(MotivationFrase))).all()
