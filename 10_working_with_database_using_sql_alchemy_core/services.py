from db import engine
from tables import users, posts
from sqlalchemy import insert, update, select, delete, asc, desc, func

## Insert or create users
def create_users(name: str, email: str):
    with engine.connect() as conn:
        stmt = insert(users).values(name=name, email=email)
        conn.execute(stmt)
        conn.commit()

## Insert or create post
def create_post(user_id:int, title: str, content: str):
    with engine.connect() as conn:
        stmt = insert(posts).values(user_id=user_id, title=title, content=content)
        conn.execute(stmt)
        conn.commit()

## Get user by id
def get_user_by_id(user_id: int):
    with engine.connect() as conn:
        stmt = select(users).where(users.c.id == user_id)
        result = conn.execute(stmt).first()
        return result

## Get all data
def get_all_users():
    with engine.connect() as conn:
        stmt = select(users)
        result = conn.execute(stmt).fetchall()
        return result

## Get posts by user
def get_posts_by_user(user_id: int):
    with engine.connect() as conn:
        stmt = select(posts).where(posts.c.user_id == user_id)
        result = conn.execute(stmt).fetchall()
        return result
    
## Update user email
def update_user_email(user_id: int, new_email: str):
    with engine.connect() as conn:
        stmt = update(users).where(users.c.id == user_id).values(email=new_email)
        conn.execute(stmt)
        conn.commit()

## Delete user 
def delete_user_by_id(user_id: int):
    with engine.connect() as conn:
        stmt = delete(users).where(users.c.id == user_id)
        conn.execute(stmt)
        conn.commit()

## Delete posts
def delete_posts_by_id(user_id: int):
    with engine.connect() as conn:
        stmt = delete(posts).where(posts.c.user_id == user_id)
        conn.execute(stmt)
        conn.commit()

## Order by
def get_users_order_by():
    with engine.connect() as conn:
        stmt = select(users).order_by(desc(users.c.name))
        result = conn.execute(stmt).fetchall()
        return result

## Gropu posts by users (Count how many posts each users has)
def get_post_count_per_user():
    with engine.connect() as conn:
        stmt = select(
            posts.c.user_id, func.count(posts.c.id).label("total+posts")
            ).group_by(posts.c.user_id)
        result = conn.execute(stmt).fetchall()
        return result

## Join 
def get_posts_with_author():
    with engine.connect() as conn:
        stmt = select(
            users.c.name.label("author_name"),
            posts.c.id,
            posts.c.title,
        ).join(users, posts.c.user_id == users.c.id)

        result = conn.execute(stmt).fetchall()
        return result