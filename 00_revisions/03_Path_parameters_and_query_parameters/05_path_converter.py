from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{filepath:path}")