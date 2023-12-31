import os

import mysql.connector
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class About(BaseModel):
    name: str
    email: str
    bio: str
    github: str
    linkedin: str


def connect_db():
    load_dotenv()
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    database = os.getenv("DB_NAME")

    if any([host, user, password, database]) is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="err reading env vars",
        )

    print(host, user, password, database)

    return mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )


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

mydb = connect_db()


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"welcome": "backend api for my portfolio"}


@app.get("/about", status_code=status.HTTP_200_OK)
async def about() -> About:
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT name, email, bio, github, linkedin FROM self")
    data = {key: val for key, val in cursor.fetchone().items()}  # type: ignore

    if not data:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="database error"
        )

    return About(**data)


@app.get("/projects", status_code=status.HTTP_200_OK)
async def projects() -> list[dict]:
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM projects")
    data = [dict(proj) for proj in cursor.fetchall()]  # type: ignore
    if not data:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="err retrieving from db",
        )

    return data
