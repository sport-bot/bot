from sqlalchemy import String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Meal(Base):
    __tablename__ = 'meals'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    ingredients: Mapped[str] = mapped_column(String, nullable=False)
    meal_time: Mapped[str] = mapped_column(String(20))
    calories: Mapped[float] = mapped_column(Float)
    protein: Mapped[float] = mapped_column(Float, nullable=False)
    fat: Mapped[float] = mapped_column(Float, nullable=False)
    carbs: Mapped[float] = mapped_column(Float, nullable=False)
    lang: Mapped[str] = mapped_column(String(10), default='en')