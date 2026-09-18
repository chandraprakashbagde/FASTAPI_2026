from db import engine
from relationship import users, posts
from sqlalchemy import insert, update, select, delete


## Create new user
def create_user(name:str, email:str, phone:str):
    with engine.connect() as conn:
        stmt = insert(users).values(name=name, email=email, phone=phone)
        conn.execute(stmt)
        conn.commit()

## Create new post
def create_post(user_id:int, title:str, content:str):
    with engine.connect() as conn:
        stmt = insert(posts).values(user_id=user_id, title=title, content=content)
        conn.execute(stmt)
        conn.commit()

## fetch single user by id
def get_user_by_id(user_id:int):
    with engine.connect() as conn:
        stmt = select(users).where(users.c.user_id == user_id)
        result = conn.execute(stmt).first()
        return result

## Fetch All users 
def fetch_all_users():
    with engine.connect() as conn:
        stmt = select(users)
        result = conn.execute(stmt).fetchall()
        return result

## Get POSTS by users
def get_posts_by_users(user_id: int):
    with engine.connect() as conn:
        stmt = select(posts).where(posts.c.user_id == user_id)
        result = conn.execute(stmt).fetchall()
        return [dict(row._mapping) for row in result]

## UPDATE user information
def update_user_email(user_id:int, email:str):
    with engine.connect() as conn:
        stmt = update(users).where(users.c.user_id == user_id).values(email=email)
        conn.execute(stmt)
        conn.commit()


## Delete user 
def delete_user(user_id: int):
    with engine.connect() as conn:
        stmt = delete(users).where(users.c.user_id == user_id)
        conn.execute(stmt)
        conn.commit()