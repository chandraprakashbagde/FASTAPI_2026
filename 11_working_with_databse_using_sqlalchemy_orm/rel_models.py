from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer, Table, Column
from db import engine

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    # One-to-Many: User to Post
    posts: Mapped[list["Post"]] = relationship("Post", 
        back_populates="user", 
        cascade="all, delete"
    )

    #One-to-Many: User to post
    profile: Mapped["Profile"] = relationship(
        "Profile", 
        back_populates="user", 
        cascade="all, delete",
        uselist=False
    )

    #Many-To-Many: User to address
    address:Mapped[list["Address"]] = relationship(
        "Address",
        back_populates="user",
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email}, phone={self.phone})>"

## Post Model -  One to Many
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(String(100), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Posts(id={self.id}, title={self.title})>"

## Post Model - One to One
class Profile(Base):
    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(50), nullable=False)

    user:Mapped["User"] = relationship("User", back_populates="profile")

    def __repr__(self):
        return f"<Profile(id={self.id}, user_id={self.user_id})"

## Address - Many To Many
class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    city:Mapped[str] = mapped_column(String(50), nullable=False)
    country:Mapped[str] = mapped_column(String(50), nullable=False)

    user:Mapped[list["User"]] = relationship("User", back_populates="address")

    def __repr__(self):
        return f"<Address(id={self.id}, user_id={self.user_id}, city={self.city}, country={self.country})>"

## User and Address Association
user_address_association = Table(
    "user_address_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("address_id", Integer, ForeignKey("address.id"), primary_key=True),
)

def create_table():
    Base.metadata.create_all(engine)

def drop_table():
    Base.metadata.create_all(engine)