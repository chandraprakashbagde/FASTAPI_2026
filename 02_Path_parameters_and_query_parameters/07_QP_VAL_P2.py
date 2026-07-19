from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Dict, TypedDict, Annotated
 
app = FastAPI()

class Product(TypedDict):
    id : int;
    title:str;
    price:int;
    description: str;

products:List[Product] = [
    {
        "id": 1,
        "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "price": 109.95,
        "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday"
    },
    {
        "id": 2,
        "title": "Mens Casual Premium Slim Fit T-Shirts ",
        "price": 22.3,
        "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket."
    },
    {
        "id": 3,
        "title": "Mens Cotton Jacket",
        "price": 55.99,
        "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day."
    }
]

## Old way (Not recommended)
# @app.get("/products")
# async def get_products(search: str | None = Query(default=None)):
#     if search:
#         filteredProducts = []
#         search_lower = search.lower()
#         for prod in products:
#             if search_lower in prod["title"].lower():
#                 filteredProducts.append(prod)

#         return filteredProducts

#     return products

## Multiple query params, ALias, Deprecating parameters, Meta data
@app.get("/products")
async def get_products(
    search: 
        Annotated[
            list[str]| None, 
            Query(alias="testsearch", deprecated=True, title="Search Products")
        ]=None
    ):
    
    if search:

        filteredProducts = []

        for prod in products:

            for s in search:
                print(s)
                if s.lower() in prod["title"].lower():

                    filteredProducts.append(prod)

        return filteredProducts
    
    return products
