from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

PRODUCTS = products = [
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

class Product(BaseModel):
    id:int
    title:str 
    price:float
    description: str
class ProdTitle(BaseModel):
    title: str

@app.get("/products")
async def fetch_all_products():
    return PRODUCTS

@app.get("/products/{product_id}")
async def get_by_id(product_id: int):

    for product in PRODUCTS:
        if product["id"] == product_id:
            return product

    return { "message" : f"product not found with ID {product_id}"}

@app.post("/products")
async def create_new_product(product: Product):
    prod = product.model_dump()
    PRODUCTS.append(prod)
    return {
        "message": f"Product '{prod["title"]}' added successfully."
    }

@app.put("/products/{product_id}")
async def update_product_info(product_id:int, product: Product):
    updated_prod = product.model_dump()
    for index, prod in enumerate(PRODUCTS):
        if prod["id"] == product_id:
            PRODUCTS[index] = updated_prod
            return {
                "message":"Product updated successfully."
            }

@app.patch("/products/{product_id}")
async def update_product_title(product_id: int, prodInfo: ProdTitle):
    for index, prod in enumerate(PRODUCTS):
        if prod["id"] == product_id:
            PRODUCTS[index]["title"] = prodInfo.title
            return {
                "message":"Product title updated successfully."
            }

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    for index, prod in enumerate(PRODUCTS):
        if prod["id"] == product_id:
            return {
                "message":"Product title updated successfully."
            }