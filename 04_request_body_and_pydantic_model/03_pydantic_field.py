from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class Product(BaseModel):
    title: str = Field(
        title="Product name",
        description="Name of the product",
        max_length=100,
        min_length=10,
        pattern="^[A-Za-z0-9]+$"
    )
    price: float = Field(
        title="Product price",
        description="Price of the product",
        
    )
    description: str

@app.post("/product")
async def create_product(product: Annotated[Product, Body(embed=True)]):
    return product