from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()

#User Table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(length=50), nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("phone", Integer, nullable=False, unique=True)
)

# ONE TO MANY
posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
    Column("title", String(length=50), nullable=False),
    Column("comment", String, nullable=False),
)

# ONE TO ONE
profile = Table(
    "profile",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer,  ForeignKey("users.id", ondelete="CASCADE"), unique=True),
    Column("bio", String, primary_key=True),
    Column("address", String, primary_key=True),
)

# MANT TO MANY
address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("street", String, primary_key=True),
    Column("country", String, nullable=False),
)

## Table association
user_address_association = Table(
    "user_address_association",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("address_id", Integer, ForeignKey("address.id"))
)

#Address Table
# users = Table(
#     "address",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("street", String(length=50), nullable=False),
#     Column("state", String, nullable=False, unique=True),
#     Column("country", Integer, nullable=False, unique=True)
# )


#Create tables in database
def create_tables():
    metadata.create_all(engine)

#Drop tables in database
# def drop_tables():
#     metadata.drop_all(engine)