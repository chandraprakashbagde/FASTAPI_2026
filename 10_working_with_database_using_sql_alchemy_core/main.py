# from fastapi import FastAPI
from tables import create_tables
from services import (
    create_users, create_post, get_user_by_id, 
    get_all_users, get_posts_by_user, update_user_email, 
    delete_user_by_id, delete_posts_by_id, 
    get_users_order_by,get_post_count_per_user,
    get_posts_with_author)

#Creating all tables
create_tables()

# app = FastAPI()

# @app.get("/")
# async def main():
#     return "Hello"

## Create user
# create_users(
#   "Mohit", 
#   email="Mohit@gmail.com"
# )
# create_users(
#   "chandraprakash", 
#   email="chandraprakashbcca@gmail.com"
# )

# Create new post for users
# delete_posts_by_id(user_id=2)
# create_post(2, "Post 1", "test 5")
# create_post( 2, "Post 2", "test 6")
# create_post(2, "Post 3", "test 7")

## Read data by id
# print(get_user_by_id(1))

## Get all data
# print(get_all_users())
# print(get_posts_by_user(2))

## Update user email
# update_user_email(2, "test@gmail.com")
# delete_user_by_id(2)

## get post count
# print(get_post_count_per_user())

print(get_posts_with_author())
