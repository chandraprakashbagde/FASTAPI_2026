from db import engine
from tables import *
from sqlalchemy import insert, update, select, delete, func



### Level 1 — INSERT

## Exercise 1 — Insert users
def create_users():
    with engine.connect() as conn:
        conn.execute(
            insert(users),
            [
                { "name": "Prakash", "email":"prakash@gmail.com", "age": "25"},
                { "name": "Rahul", "email":"Rahul@gmail.com", "age": "28"},
                { "name": "Amit", "email":"Amit@gmail.com", "age": "24"},
                { "name": "Sneha", "email":"Sneha@gmail.com", "age": "27"},
                { "name": "Neha", "email":"Neha@gmail.com", "age": "23"}
            ]
        )
        conn.commit()

## Exercise 2 — Insert posts
def create_posts():

    posts_data = [
        # {"user_id": 1, "title": "Introduction to Python", "content": "Python is a powerful programming language."},
        # {"user_id": 1, "title": "Learning SQL", "content": "SQL is used to manage relational databases."},
        # {"user_id": 2, "title": "Understanding SQLAlchemy", "content": "SQLAlchemy helps Python applications interact with databases."},
        # {"user_id": 2, "title": "FastAPI Basics", "content": "FastAPI is a modern framework for building APIs."},
        # {"user_id": 3, "title": "What is React?", "content": "React is a JavaScript library for building user interfaces."},
        # {"user_id": 3, "title": "Frontend Development", "content": "Frontend development focuses on the user interface."},
        # {"user_id": 1, "title": "Backend Development", "content": "Backend development handles business logic and databases."},
        # {"user_id": 2, "title": "Database Relationships", "content": "Relationships connect records between database tables."},
        # {"user_id": 3, "title": "REST API", "content": "REST APIs allow applications to communicate with each other."},
        {"user_id": 1, "title": "Full Stack Development", "content": "Full stack development covers both frontend and backend."}
    ]

    with engine.connect() as conn:
        conn.execute( insert(posts) , posts_data)
        conn.commit()

## Exercise 3 — Insert comments
def user_comment():
    comments_data = [
        {"post_id": 1, "user_id": 2, "content": "Great introduction to Python!"},
        {"post_id": 1, "user_id": 3, "content": "Python is one of my favorite languages."},
        {"post_id": 2, "user_id": 1, "content": "SQL is really important for backend development."},
        {"post_id": 2, "user_id": 3, "content": "I recently learned JOIN queries."},
        {"post_id": 3, "user_id": 2, "content": "SQLAlchemy makes database operations easier."},
        {"post_id": 3, "user_id": 1, "content": "I am currently learning SQLAlchemy Core."},
        {"post_id": 4, "user_id": 3, "content": "FastAPI is very fast and easy to work with."},
        {"post_id": 4, "user_id": 1, "content": "I am building my first FastAPI project."},
        {"post_id": 5, "user_id": 2, "content": "React makes building interactive UIs easier."},
        {"post_id": 5, "user_id": 3, "content": "Hooks are very useful in React."},
        {"post_id": 6, "user_id": 1, "content": "Frontend development requires good CSS knowledge."},
        {"post_id": 7, "user_id": 2, "content": "Backend development is interesting."},
        {"post_id": 8, "user_id": 3, "content": "Database relationships are very important."},
        {"post_id": 9, "user_id": 1, "content": "REST APIs connect frontend and backend."},
        {"post_id": 10, "user_id": 2, "content": "Full stack development requires multiple skills."}
    ]
    
    with engine.connect() as conn:
        conn.execute(
            insert(comments),
            comments_data
        )
        conn.commit()

## Exercise 4 — Insert addresses
def create_users_address():
    addresses_data = [
        {
            "user_id": 1,
            "city": "Nagpur",
            "country": "India"
        },
        {
            "user_id": 1,
            "city": "Pune",
            "country": "India"
        },
        {
            "user_id": 2,
            "city": "Mumbai",
            "country": "India"
        },
        {
            "user_id": 3,
            "city": "Delhi",
            "country": "India"
        },
        {
            "user_id": 3,
            "city": "Bangalore",
            "country": "India"
        },
        {
            "user_id": 3,
            "city": "Hyderabad",
            "country": "India"
        }
    ]

    with engine.connect() as conn:
        conn.execute(
            insert(addresses),
            addresses_data
        )
        conn.commit()


### Level 2 — SELECT

## Exercise 5 — Get all users
def get_all_users():
    with engine.connect() as conn:
        stmt = select(users)
        result = conn.execute(stmt).fetchall()
        return result

## Exercise 6 — Find user by id
def find_users_by_id(user_id:int):
    with engine.connect() as conn:
        stmt = select(users).where(users.c.user_id == user_id)
        result = conn.execute(stmt).fetchone()
        return result

## Exercise 7 — Find users by age
def find_user_by_age(age: int):
    with engine.connect() as conn:
        stmt = select(users).where( users.c.age == age)
        result = conn.execute(stmt).fetchone()
        return result
    
## Exercise 8 — Find users older than 25
def find_older_than_25():
    with engine.connect() as conn:
        stmt = select(users).where(users.c.age > 25)
        result = conn.execute(stmt).fetchall()
        return result


## Exercise 9 — Find users between two ages
def find_users_btween_two_ages(age1:int, age2:int):
    with engine.connect() as conn:
        stmt = select(users).where(users.c.age > age1, users.c.age < age2)
        result = conn.execute(stmt).fetchall()
        return result


### Level 3 — UPDATE

## Exercise 10 — Update username
def update_username(user_id:int, name:str):
    with engine.connect() as conn:
        stmt = update(users).where(user_id).values(name=name)
        conn.execute(stmt)
        conn.commit()

## Exercise 11 — Update email
def update_email(user_id:int, email:str):
    with engine.connect() as conn:
        stmt = update(users).where(user_id).values(email=email)
        conn.execute(stmt)
        conn.commit()

## Exercise 12 — Increase everyone's age
def increase_age_by_one():
    with engine.connect() as conn:
        stmt = update(users).values(age=users.c.age + 1)
        conn.execute(stmt)
        conn.commit()


### Level 4 — DELETE
def delete_user_by_id(user_id: int):
    with engine.connect() as conn:
        stmt = delete(users).where( users.c.user_id == user_id )
        conn.execute(stmt)
        conn.commit()

## Exercise 13 — Delete a user