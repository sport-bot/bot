from sqlalchemy import BigInteger, String, Integer, Float, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[str] = mapped_column(BigInteger, index=True)
    name: Mapped[str] = mapped_column(String(50))
    gender: Mapped[str] = mapped_column(String(10))
    age: Mapped[int] = mapped_column(Integer)
    weight: Mapped[float] = mapped_column(Float)
    height: Mapped[int] = mapped_column(Integer)
    fitness_level: Mapped[str] = mapped_column(String(16))
    lang: Mapped[str] = mapped_column(String(10), default="en")
    goal: Mapped[str] = mapped_column(String(16))
    free_days_left: Mapped[int] = mapped_column(Integer, default=30)
    subscription_days_left: Mapped[int] = mapped_column(Integer, default=0)
    is_admin: Mapped[bool] = mapped_column(Boolean)


