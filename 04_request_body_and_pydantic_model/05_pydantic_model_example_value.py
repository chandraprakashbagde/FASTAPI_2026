from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated
app = FastAPI()

## Using "example" key in Field
# class Product(BaseModel):
#     id:int = Field(
#         ge=1,
#         examples=["12222"]
#     )
#     title: str = Field(
#         min_length=3,
#         max_length=100,
#         examples=["Oppo K12X 5G"]
#     )
#     price: float = Field(ge=1, examples=["100.00"])

## Uisng json_scheema_extra
class Product(BaseModel):
    id:int = Field(ge=1)
    title: str = Field(min_length=3,max_length=100)
    price: float = Field(ge=1)

    model_config= {
        "json_schema_extra":{
            "examples": [
                {
                    "id":"12222",
                    "title":"Oppo K12X 5G",
                    "price":"100.00"
                },
                {
                    "id":"32",
                    "title":"33 K12X 5G",
                    "price":"1300.00"
                }
            ]
        }
    }


@app.post("/products")
async def create_product(product: Annotated[Product, Body(embed=True)]):
    return product