from sqlalchemy import BigInteger, String, Integer, Float, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(50))
    gender: Mapped[str] = mapped_column(String(10))
    age: Mapped[int] = mapped_column(Integer)
    weight: Mapped[float] = mapped_column(Float)
    height: Mapped[int] = mapped_column(Integer)
    fitness_level: Mapped[str] = mapped_column(String(16))
    goal: Mapped[str] = mapped_column(String(16))
    is_admin: Mapped[bool] = mapped_column(Boolean)


