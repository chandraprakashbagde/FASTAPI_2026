from db import engine
from sqlalchemy import select
from relationship import posts, users

## Fetch posts with author name
def get_posts(id: int):
    with engine.connect() as conn:
        stmt = select(
            posts.c.post_id,
            posts.c.title,
            users.c.name.label("author_name")
        ).join(users, posts.c.user_id == users.c.user_id).where(posts.c.user_id==id)

        result = conn.execute(stmt).fetchall()

        return result;

