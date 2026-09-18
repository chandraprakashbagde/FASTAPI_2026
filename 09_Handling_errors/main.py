from fastapi import FastAPI, Form, Body, Query, Path, UploadFile, File,HTTPException
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

items = {
    "banana":"A yellow delight",
    "apple":"Eat apple a day, keep doctor away!"
}


@app.get("/items/{item_id}")
async def get_items(item_id: Annotated[str, Path()]):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Items Not Found",
            headers={"x-error-type":"Itemmissing"}
            )

    return items[item_id]