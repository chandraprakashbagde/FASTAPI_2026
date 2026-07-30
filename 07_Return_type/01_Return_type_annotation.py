from fastapi import FastAPI, Body, Path, Query, Cookie, Header
from pydantic import BaseModel,EmailStr
from typing import Annotated


app = FastAPI()

## Without return type
# @app.get("/products")
# async def getAllProducts():
#     return [
#         {
#             "status" : "OK"
#         },
#         {
#             "status" : "200"
#         },
#     ]


## With return type annotation
class Product(BaseModel):
    id:int 
    name:str 
    price:float
    stock: int | None = None

class ProductOut(BaseModel):
    name:str
    price:float
## Passing all values
# @app.post("/products")
# async def getAllProducts(product: Annotated[Product, Body()]) -> Product:
#     return product

## Miss some values
# @app.post("/products")
# async def getAllProducts(product: Annotated[Product, Body()]) -> Product:
#     return {
#         "id":product.id,
#         "name":product.name,
#         "price":product.price
#     }


## Return a list= list and List produced same openSchema and validation behavior
# @app.post("/products")
# async def getAllProducts(product: Annotated[Product, Body()]) -> list[Product]:
#     return [{
#         "id":2,
#         "name":product.name,
#         "price":product.price
#     }]


## Manage input and output return type
@app.post("/products")
async def getAllProducts(product: Annotated[Product, Body()]) -> ProductOut:
    return product

## Use return types by inheritance
class BaseUser(BaseModel):
    fullname:str
    email:EmailStr

class User(BaseUser):
    password: str 

@app.post("/users")
async def create_user(user: User) -> BaseUser:
    return user