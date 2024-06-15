from sqlalchemy import String, ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Exercise(Base):
    __tablename__ = 'exercises'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(250))
    video_id: Mapped[str] = mapped_column(String(100))
    level: Mapped[str] = mapped_column(String(20))
    types: Mapped[list[str]] = mapped_column(ARRAY(String))



