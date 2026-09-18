from db import engine
from sqlalchemy import MetaData, Table, Column, String, Integer

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("email", String(50), nullable=False, unique=True),
    Column("phone", String(10), nullable=False, unique=True),
)


def create_table():
    metadata.create_all(engine)