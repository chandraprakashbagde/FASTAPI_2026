from db import engine
from sqlalchemy import select, desc, asc, func
from relationship import users, posts


## Order By
def get_order_by_user():
    with engine.connect() as conn:
        stmt = select(users).order_by(desc(users.c.name))
        result = conn.execute(stmt).fetchall();
        return result

## Group By
def get_users_post_count(user_id: int):
    with engine.connect() as conn:
        stmt = select(posts.c.user_id, func.count(posts.c.post_id).label("total_posts")).where(posts.c.user_id == user_id).group_by(posts.c.user_id)
        result = conn.execute(stmt).fetchall()
        return result