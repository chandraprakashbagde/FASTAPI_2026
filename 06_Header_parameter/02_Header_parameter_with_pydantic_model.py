from fastapi import FastAPI, Path, Query, Cookie, Header, Body
from pydantic import BaseModel, Field
from typing import Annotated


app = FastAPI()
class ProductHeaders(BaseModel):
    # model_config = { "extra" : "forbid" }
    authorization: str = Field(..., title="User Token", description="User token generated after logged in.")
    accept_languege:str = Field(..., title="User preffered languege")
    tracking_ids: list[str] | None = None


# @app.get("/products")
# async def get_products(headers: Annotated[ProductHeaders, Header()]):
#     return {
#         "headers": headers
#     }


## Combining body parameter and header paramenter

class Product(BaseModel):
    title:str
    price: float

@app.post("/products")
async def create_product(headers: Annotated[ProductHeaders, Header()], product: Annotated[Product, Body()]):
    return {
        "headers": headers,
        "product": product
    }
