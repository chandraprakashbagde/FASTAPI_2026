from db import engine
from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

# Users
class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    # One To Many : Users to Posts
    posts: Mapped[list["Posts"]] = relationship("Posts", back_populates="users", cascade="all, delete")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"


# Posts
class Posts(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    users: Mapped["Users"] = relationship("Users", back_populates="posts")

    def __repr__(self):
        return f"<Posts(id={self.id}, user_id={self.user_id}, title={self.title}, content={self.content})>"


def create_tables():
    Base.metadata.create_all(bind=engine)