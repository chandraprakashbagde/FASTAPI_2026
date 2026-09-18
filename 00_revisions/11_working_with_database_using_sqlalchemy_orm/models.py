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

    # One To One : Users to Profile
    profile: Mapped["Profile"] = relationship("Profile", uselist=False, back_populates="users", cascade="all, delete")

    # Many To Many
    address: Mapped[list["Address"]] = relationship("Address", back_populates="users")

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

# Profile
class Profile:
    __tablename__ = "profile"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    bio: Mapped[str] = mapped_column(String(100), nullable=False)

    users: Mapped["Users"] = relationship("Users", back_populates="profile")


# Address
class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(255), nullable=False)
    dist: Mapped[str] = mapped_column(String(50), nullable=False)
    contry: Mapped[str] = mapped_column(String(50), nullable=False)

    users: Mapped[list["Users"]] = relationship("Users", back_populates="address")

    def __rep__(self):
        return f"<Address(id={self.id}, street={self.street}, dist={self.dist}, contry={self.contry})" 


user_address_assocciation = Table(
    "user_address_assocciation",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True, nullable=False),
    Column("address_id", Integer, ForeignKey("address.id"), primary_key=True, nullable=False)
)


def create_tables():
    Base.metadata.create_all(bind=engine)

def drop_tables():
    Base.metadata.drop_all(bind=engine)