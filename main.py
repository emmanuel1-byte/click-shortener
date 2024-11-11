from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.models import *
from src.utils.database import create_db_and_tables
from src.routers.user_route import auth
from src.routers.url_shortener_route import url_shortner


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth)
app.include_router(url_shortner)


@app.get("/")
def read_root():
    return {"message": "API is running"}
