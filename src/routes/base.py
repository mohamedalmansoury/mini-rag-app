from fastapi import FastAPI , APIRouter
from dotenv import load_dotenv
import os

load_dotenv(".env")

base_router = APIRouter(
    prefix = "/api/v1",
    tags = ["api_v1"]
)

@base_router.get("/")

async def welcome():
    x = {"App name" :  os.getenv("APP_NAME"),
         "App version" :  os.getenv("APP_VERSION")
    } 
    return x
