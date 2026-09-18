from db import engine
from sqlalchemy import Table, Column, String, Integer, MetaData, ForeignKey

metadata = MetaData()

## Users table
users = Table(
    "users",
    metadata,
    Column("id",Integer, nullable=False, primary_key=True, autoincrement=True),
    Column("name", String(length=50), nullable=False),
    Column("email", String, nullable=False, unique=True),
)

## Post table
posts = Table(
    "posts",
    metadata,
    Column("id", Integer, nullable=False , primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("title", String, nullable=False),
    Column("content", String, nullable=False)
)

def create_tables():
    metadata.create_all(engine)