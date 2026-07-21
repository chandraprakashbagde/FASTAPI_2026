from fastapi import FastAPI, Cookie, Path, Query
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

@app.get("/products/recomendations")
async def get_all_products(session_id: Annotated[str | None, Cookie()] = None):
    if session_id:
        return {
            "message": "Showing recommendations based on session_id"
        }
    return {
        "message":"No session id provided"
    }