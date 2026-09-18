from db import engine
from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("user_id", Integer, primary_key=True, unique=True, nullable=False),
    Column("name", String(50), unique=True, nullable=False),
    Column("email", String(50), unique=True, nullable=False),
    Column("age", Integer,nullable=False),
)

posts = Table(
    "posts",
    metadata,
    Column("post_id", Integer, primary_key=True, unique=True, nullable=False),
    Column("user_id", Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False),
    Column("title", String(50), unique=True, nullable=False),
    Column("content", String(50), unique=True, nullable=False),
)

comments = Table(
    "comments",
    metadata,
    Column("comment_id", Integer, primary_key=True, unique=True, nullable=False),
    Column("post_id", Integer, ForeignKey("posts.post_id", ondelete="CASCADE"), nullable=False),
    Column("user_id", Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False),
    Column("content", String(50), unique=True, nullable=False),
)

addresses = Table(
    "addresses",
    metadata,
    Column("address_id", Integer, primary_key=True, unique=True, nullable=False),
    Column("user_id", Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False),
    Column("city", String(50), nullable=False),
    Column("country", String(50), nullable=False),
)

def create_table():
    metadata.create_all(engine)