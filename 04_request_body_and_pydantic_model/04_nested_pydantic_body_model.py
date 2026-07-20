from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated
app = FastAPI()

# Sub model
class Category(BaseModel):
    name: str = Field(
        title="Category Name",
        description="Name of the category"
    )

    description:str | None = Field(
        default=None,
        title="Category Description",
        description="Description of a category"
    )

class Product(BaseModel):
    id:int = Field(
        ge=1
    )
    title: str = Field(
        min_length=3,
        max_length=100,
    )
    price: float = Field(ge=1)

    ##Single Category
    #category: Category | None = Field(default=None)
    
    ##Multiple Category
    category: list[Category]

@app.post("/products")
async def create_product(product: Annotated[Product, Body(embed=True)]):
    return product