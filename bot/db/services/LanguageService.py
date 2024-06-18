from bot.db.db import async_session
from bot.db.models.LanguageModel import Language
from sqlalchemy import select, update, delete


async def create_language(code: str):
    async with async_session() as session:
        session.add(Language(code=code))
        await session.commit()

async def get_all_languages():
    async with async_session() as session:
        return (await session.scalars(select(Language))).all()