from sqlalchemy import String, ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Exercise(Base):
    __tablename__ = 'exercises'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    technik_description: Mapped[str] = mapped_column(String)
    low_level_description: Mapped[str] = mapped_column(String(250), nullable=True)
    regular_level_description: Mapped[str] = mapped_column(String(250), nullable=True)
    high_level_description: Mapped[str] = mapped_column(String(250), nullable=True)
    video_id: Mapped[str] = mapped_column(String(100), nullable=True)
    type: Mapped[str] = mapped_column(String(20))
