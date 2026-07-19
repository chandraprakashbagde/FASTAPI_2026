from fastapi import FastAPI;

app = FastAPI()


#fetch all products
@app.get("/products")
async def get_all_products():
    return {
        "message": "All Products fetched"
    }

# GET
# fetch prodcut by id
@app.get("/products/{product_id}")
async def get_product_by_id(product_id:int):
    return {
        "message": "Single product fetched.",
        "id":product_id
    }

# POST
## Add new Record
@app.post("/products")
async def add_new_product(product: dict):
    return {
        "message": "New product has been created.",
        "product": product
    }

# PUT
## Update complete record
@app.put("/products/{product_id}")
async def update_product(product: dict):
    return {
        "message":"Complete prodcut updated.",
        "product":product
    }

# PATCH
## Update few columns
@app.patch("/products/{product_id}")
async def update_product_partially(product: dict):
    return {
        "message":"Update few product information",
        "product": product
    }

# DELETE
## Delete record
@app.delete("/products/{delete}")
async def delete_product(product_id:int):
    return {
        "message": f"product with id {product_id} has been deleted"
    }