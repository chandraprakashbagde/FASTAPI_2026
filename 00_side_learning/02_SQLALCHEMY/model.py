from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Column, Table
from db import engine

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)

Base.metadata.create_all(engine)