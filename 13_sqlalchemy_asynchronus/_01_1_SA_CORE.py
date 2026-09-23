from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey
import asyncio

## DB
DATABASE_URL = "sqlite+aiosqlite:///./sqlite.db"
engine = create_async_engine(DATABASE_URL, echo=True)
## END DB



## Metadata
metadata = MetaData()

## Tables
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String("100"), nullable=False),
    Column("email", String(100), nullable=False)
)


## Tables


## Create Tables
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


## drop Tables
async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)



asyncio.run(create_tables())