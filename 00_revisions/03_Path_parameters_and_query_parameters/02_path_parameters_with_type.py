from fastapi import FastAPI

app = FastAPI()

@app.get("/products/{product_id}")
async def fetch_product_by_id(product_id: int):
    return {
        "message":"Single product fetched successfully.",   
        "product_id":product_id
    }