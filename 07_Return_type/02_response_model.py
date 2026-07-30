from fastapi import FastAPI, Body, Path, Query, Cookie, Header
from pydantic import BaseModel,EmailStr
from typing import Annotated

app = FastAPI()


class BaseProduct(BaseModel):
    name: str 
    price: float

class Product(BaseProduct):
    id:int 
    stock: float

@app.post("/products", response_model=BaseProduct)
async def create_product(product: Annotated[Product, Body()]):
    return product
