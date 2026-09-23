from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker,AsyncAttrs

from sqlalchemy import  Integer, String, select, update

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

import asyncio

DATABASE_URL = "sqlite+aiosqlite:///./sqlite.db"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


## Models

class Base(AsyncAttrs, DeclarativeBase):
    pass

## user
class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False);
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<Users( id={self.id}, name={self.name}, email={self.email} )>"


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


## End Models

## Crud
async def create_users(name: str, email: str):
    async with async_session() as session:
        usr = Users(name=name, email=email)
        session.add(usr)
        await session.commit()

async def get_user_by_id(id: int):
    async with async_session() as session:
        usr = await session.get(Users, id)
        return usr

async def get_all_users():
    async with async_session() as session:
        stmt = select(Users)
        users = await session.scalars(stmt)
        return users.all()

async def update_user_email(id: int, email: str):
    async with async_session() as session:
        user = await session.get(Users, id)
        if user:
            user.email = email;
            await session.commit()

        # with core

async def delete_users_email(id: int):
    async with async_session() as session:
        usr = await session.get(Users, id)
        if usr:
            await session.delete(usr)
            await session.commit()

            



## End Crud

async def main():
    # await create_tables()
    # await create_users(name="Chandraprakash", email="chandraprakashbcca@gmail.com")
    # await create_users(name="Ayushi Sharma", email="aushis@gmail.com")
    
    # usr = await get_user_by_id(2)
    # print(usr)

    # users = await get_all_users()
    # print(users)

    await update_user_email(id=1, email="test@newdom1aisn.com")



asyncio.run(main())    
