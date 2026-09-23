from _01_1_SA_CORE import engine, users;
from sqlalchemy import insert, update, delete, select

import asyncio

async def create_users(name: str, email: str):
    async with engine.connect() as conn:
        stmt = insert(users).values(name=name, email=email)
        await conn.execute(stmt)
        await conn.commit()

async def get_users_by_id(id: int):
    async with engine.connect() as conn:
        stmt = select(users.c.name).where(users.c.id == id)
        result = await conn.execute(stmt)
        return result.first()
    
#  + users.c.email
async def update_user_email(id: int, new_email: str):
    async with engine.connect() as conn:
        stmt = update(users).values( email = new_email ).where(users.c.id == id)
        await conn.execute(stmt)
        await conn.commit()

async def delete_user(id: int):
    async with engine.connect() as conn:
        stmt = delete(users).where(users.c.id == id)
        await conn.execute(stmt)
        await conn.commit()

## --------------------------------------------------------------------------------
async def main():

    await create_users(name="Chandraprakash Bagade", email="chandraprakashbagde@gmail.com")

    # user = await get_users_by_id(1)
    # print(user)
    # await update_user_email(id=1, new_email="new")
    # await delete_user(1)

asyncio.run(main())