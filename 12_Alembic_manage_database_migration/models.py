from db import engine
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass 

## Users table

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] =  mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False) 
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    phone: Mapped[str] = mapped_column(Integer)

    def __repr__(self):
        return f"<User( id={self.id}, name={self.name}, email={self.email} )>"


# f