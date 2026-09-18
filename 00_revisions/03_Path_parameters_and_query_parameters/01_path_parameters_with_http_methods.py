from fastapi import FastAPI

app = FastAPI()


## get all products
## GET METHOD
@app.get("/products")
async def all_products():
    return {
        "response":"All Products"
    }

## get single product by id
@app.get("/product/{product_id}")
async def getSingleProduct(product_id: int):
    return {
        "message":"Product fetched successfully.",
        "product_id":product_id
    }


## POST Request
## Create or Insert Product
@app.post("/products")
async def create_product(new_product: dict):
    return {
        "message":"Product created successfull.",
        "product":new_product
    }

## PUT Request
## Update data completely
@app.put("/product/{product_id}")
async def update_product(product_id: int, product: dict):
    return {
                "message":"Product updated successfull.",
                "product":{
                    "product_id":product_id,
                    "product":product
                }
            }

## PATCH Request
## Update Partial Data
@app.patch("/product/{product_id}")
async def update_product(product_id: int, product: dict):
    return {
            "message":"Product updated successfull.",
            "product":{
                "product_id":product_id,
                "product":product
            }
        }

## DELETE REQUEST
## Delele record
@app.delete("/product/{product_id}")
async def delete_product(product_id: int):
    return {
        "message":"Product deleted successfully",
        "id":product_id
    }