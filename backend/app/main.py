from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import api_router
from app.db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):

    await init_db(app)
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Research Due Diligence System"}


