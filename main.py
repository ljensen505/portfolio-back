import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from db import mydb
from models import About, Project
from queries import get_about, get_projects

load_dotenv(override=True)
app = FastAPI()

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8000",
    "https://localhost:8000",
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"welcome": "backend api for my portfolio"}


@app.get("/about", status_code=status.HTTP_200_OK)
async def about() -> About:
    try:
        return get_about()
    except Exception as e:
        print(f"err getting about: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"database error: {e}",
        )


@app.get("/projects", status_code=status.HTTP_200_OK)
async def projects() -> list[Project]:
    try:
        return get_projects()
    except Exception as e:
        print(f"err getting projects: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"database error: {e}",
        )
