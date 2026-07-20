from fastapi import FastAPI, Body, Query, Path
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Product(BaseModel):
    id: int
    title: str
    price: float
    description: str


class Seller(BaseModel):
    id:int
    first_name: str
    last_name: str

## Multiple Parameters
# @app.post("/products")
# async def create_product(product: Product, seller: Seller,):
#     return {
#         "product": product,
#         "seller": seller
#     }

## Singular values in body
# @app.post("/products")
# async def create_product(
#         product: Product, 
#         seller: Seller,
#         sec_key: Annotated[str | None, Body(min_length=100)] = None,
#         ):

#     return {
#         "product": product,
#         "seller": seller,
#         "sec_key":sec_key
#     }

## Embedding single value in body

#Without embed
# @app.post("/products")
# async def create_product(product: Product):
#     return { product }

#With embed
@app.post("/products")
async def create_product(product: Annotated[Product, Body(embed=True)]):
    return { product }

