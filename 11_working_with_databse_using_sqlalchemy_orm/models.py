from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Integer
from db import engine

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__= "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=50))
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(10), unique=True)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"

# Create Table
def create_table():
    Base.metadata.create_all(engine)

# Drop Table
def drop_table():
    Base.metadata.drop_all(engine)