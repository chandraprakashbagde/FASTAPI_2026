from fastapi import FastAPI
from enum import Enum, EnumCheck

app = FastAPI()

class ProductCategory(str, Enum):
    books = "Books"
    electronics = "electronics"
    clothes = "clothes"

## Fetching product by product category
@app.get("/products/{product_category}")
async def get_product_by_category(product_category: ProductCategory):
    resp = {"category":product_category}

    if product_category == ProductCategory.books:
        resp["message"] = "Books are awesome"
    elif product_category == ProductCategory.clothes:
        resp["message"] = "Clothes are attractive"
    elif product_category == ProductCategory.electronics:
        resp["message"] = "Electronics are chip"

    return resp