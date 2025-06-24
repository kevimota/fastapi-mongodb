from typing import Union
from fastapi import FastAPI, APIRouter
from .routers import env_data

app = FastAPI()

app.include_router(env_data.router)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

