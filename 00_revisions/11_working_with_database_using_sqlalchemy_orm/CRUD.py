from crud_models import Users, Posts
from db import SessionLocal

# Insert or Create user
def create_users(name: str, email: str):
    with SessionLocal() as session:
        user = Users(name=name, email=name)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

# Insert or Create posts
def create_posts(user_id: int, title: str, content: str):
    with SessionLocal() as session:
        post = Posts(user_id=user_id, title=title, content=content)
        session.add(post)
        session.commit()