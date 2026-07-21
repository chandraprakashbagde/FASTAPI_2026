from fastapi import FastAPI, Cookie, Path, Query, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

# class ProductCookies(BaseModel):
#     session_id: str 
#     prefferred_category:str
#     tracking_id: str

# @app.get("/products/recomendations")
# async def get_recommendations(cookies: Annotated[ProductCookies, Cookie()]):
#     response = { "session_id" : cookies.session_id }

#     if cookies.prefferred_category:
#         response["message"] = f"Showing recommendations for { cookies.prefferred_category }"
#     else:
#         response["message"] = f"Default recommendations for { cookies.session_id}"

#     return response



## Forbidden extra cookies values
class ProductCookies(BaseModel):
    session_id: str 
    prefferred_category:str
    tracking_id: str

    model_config = {
        "extra":"forbid"
    }

@app.get("/products/recomendations")
async def get_recommendations(cookies: Annotated[ProductCookies, Cookie()]):
    response = { "session_id" : cookies.session_id }

    if cookies.prefferred_category:
        response["message"] = f"Showing recommendations for { cookies.prefferred_category }"
    else:
        response["message"] = f"Default recommendations for { cookies.session_id}"
    if cookies.tracking_id:
        response["tracking_id"] = cookies.tracking_id

    return response