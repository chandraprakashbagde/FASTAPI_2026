from db import engine
from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey

metadata =  MetaData()

users = Table(
    "users",
    metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("name", String(100), nullable=False, unique=True),
    Column("email", String(100), nullable=False, unique=True),
    Column("phone", String(10), nullable=False, unique=True)
)

## ONE TO MANY (USERS TO POSTS)- One user can have multiple posts
posts = Table(
    "posts",
    metadata,
    Column("post_id", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("user_id", Integer, ForeignKey("users.user_id", ondelete="CASCADE")),
    Column("title", String(50), nullable=False),
    Column("content", String(200), nullable=False)
)

## ONE TO ONE (USERS TO PROFILE)- One User can have only one profile
profile = Table(
    "profile",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("user_id", Integer, ForeignKey("users.user_id", ondelete="CASCADE")),
    Column("bio", String(50)),
)

address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("Street", String(50), nullable=False),
    Column("Country", String(200), nullable=False)
)


## MANY TO MANY
users_address_association = Table(
    "users_address_association",
    metadata,
    Column("user_id", Integer, ForeignKey("users.user_id"), primary_key=True),
    Column("address_id", Integer, ForeignKey("address.id"), primary_key=True),
)


def create_table():
    metadata.create_all(engine)