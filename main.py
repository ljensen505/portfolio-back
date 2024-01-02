import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import queries
from __version__ import __version__
from helpers import origins
from models import About, Project

load_dotenv(override=True)
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    available_routes = [
        "/",
        "/about",
        "/projects",
    ]
    return {
        "welcome": "backend api for lucasjensen.me",
        "version": __version__,
        "routes": available_routes,
    }


@app.get("/about", status_code=status.HTTP_200_OK)
async def about() -> About:
    try:
        return queries.get_about()
    except Exception as e:
        print(f"err getting about: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"database error: {e}",
        )


@app.get("/projects", status_code=status.HTTP_200_OK)
async def projects() -> list[Project]:
    try:
        return queries.get_projects()
    except Exception as e:
        print(f"err getting projects: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"database error: {e}",
        )


@app.get("/projects/{project_id}", status_code=status.HTTP_200_OK)
async def project(project_id: int) -> Project:
    try:
        return queries.get_project(project_id)
    except Exception as e:
        print(f"err getting projects: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"database error: {e}",
        )


@app.post("/projects", status_code=status.HTTP_201_CREATED)
async def post_project(project: Project) -> Project:
    try:
        return queries.create_project(project)
    except Exception as e:
        print(f"err creating project: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"database error: {e}",
        )


@app.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: int):
    try:
        return queries.delete_project(project_id)
    except Exception as e:
        print(f"err deleting project: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"database error: {e}",
        )
