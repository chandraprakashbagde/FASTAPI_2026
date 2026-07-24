from fastapi import FastAPI, Path, Query, Cookie, Header, Body
from typing import Annotated

app = FastAPI()

## PASSING SINGLE HEADER PARAM
# @app.get("/products")
# async def get_products(user_agent: Annotated[str | None, Header()]):
#     return {
#         "passed header": user_agent
#     }
## curl -H 'User-Agent: CHROME 2019' 'http://localhost:8000/products'   


##Handling duplicate user 
@app.get("/products")
async def get_products(x_product_token: Annotated[list[str] | None, Header()] = None):
    return {
        "passed header": x_product_token
    }
## curl -H 'X-Product-Token: TOKEN 1' -H 'X-Product-Token: TOKEN 2''http://localhost:8000/products'