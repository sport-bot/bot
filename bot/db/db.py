from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
# from config import DATABASE_URL
from bot.db.models.UserModel import Base, User

DATABASE_URL = "postgresql+asyncpg://postgres:Tos_11235@localhost:5432/fitness_bot"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(engine)

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)