from sqlalchemy import String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(AsyncAttrs, DeclarativeBase):
    pass

class MealRecommendation(Base):
    __tablename__ = 'meal_recommendations'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    recommendation: Mapped[str] = mapped_column(String)
    lang: Mapped[str] = mapped_column(String(10), default='en')
    type: Mapped[str] = mapped_column(String(30))
    