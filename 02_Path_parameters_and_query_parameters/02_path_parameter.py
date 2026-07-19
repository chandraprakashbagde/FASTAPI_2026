from fastapi import FastAPI;
from enum import Enum

app = FastAPI()

# @app.get("/products/get-by-id/{product_id}")
# async def get_product_by_id(product_id: int):
#     return {
#         "message":f"Product fetched successfully {product_id}"
#     }

# ## Order matters
# @app.get("/products/get_single_prodct")
# async def fetch_single_product():
#     return {
#         "message":"Single Product fetched."
#     }

# @app.get("/products/{product_name}")
# async def get_product_by_name(product_name: str):
#     return {
#         "message":"Single Product Fetched",
#         "product_name":product_name
#     }

## Pre-defined values
class ProductCategory(Enum):
    books = "books"
    clothing = "clothing"
    electronics = "electronics"

# @app.get("/products/{category}")
# async def get_products_category(category: ProductCategory):
#     return {
#         "category": category.value
#     }

## Working with enumerations
@app.get("/products/{category}")
async def get_products_category(category: ProductCategory):
    if category == ProductCategory.books:
        return {
            "message":"Books are awesome....!"
        }
    elif category.value == "clothing":
        return {
            "message":"Fashion trends here!"
        }
    elif category == ProductCategory.electronics:
        return {
            "message":"Latest gadgets available"
        }
    

## Working with path converter
@app.get("/products/images/{file_path:path}")
async def get_product_image(file_path: str):
    return {
        "You requested file at path": file_path
    }