from fastapi import FastAPI

app = FastAPI()

## Single Paramerter
@app.get("/products")
async def get_products(category:str):
    return {
        "category": category
    }

## Multiple parameters
@app.get("/products")
async def get_products(limit:int ,category:str | None=None):
    return {
        "category": category
    }
