from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id : int;
    title:str;
    price:int;
    description: str;
class ProdTitleUpdt(BaseModel):
    id: int
    title:str

products = [
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

## Fetch All Products
@app.get("/products")
async def get_products():
    return {
        "data": products
    }

## Fetch Single Product
@app.get("/products/{product_id}")
async def get_by_id(product_id:int):
    for product in products:
        if product["id"] == product_id:
            return product
        
## Create New Product
@app.post("/product")
async def add_new_product(product: Product):
    
    products.append(product.model_dump())

    return {
        "message": "Product created successfully!",
        "product": product.model_dump()
    }

@app.put("/products")
async def update_product(product: Product):
    for index, prod in enumerate(products):
        if prod["id"] == product.id:
            products[index] = product.model_dump()
            return {
                "status": "Updated",
                "product": product.model_dump()
            }
        

@app.patch("/products")
async def upadate_product_title(prodtitleupdt: ProdTitleUpdt):
    return {
        "message": "Product title has been updated !"
    }
