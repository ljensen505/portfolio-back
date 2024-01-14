import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Security, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import queries
from __version__ import __version__
from helpers import origins
from models import About, Project
from utils import VerifyToken

load_dotenv()
app = FastAPI()
auth = VerifyToken()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    available_routes = [
        "/",
        "/about",
        "/projects",
        "/static/resume.pdf",
        "/static/favicon.png",
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
    project = queries.get_project(project_id)

    try:
        project = queries.get_project(project_id)

    except Exception as e:
        print(f"err getting projects: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"database error: {e}",
        )
    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"project with id {project_id} not found",
        )
    return project


@app.post("/projects", status_code=status.HTTP_201_CREATED)
async def post_project(project: Project, auth_result=Security(auth.verify)) -> Project:
    try:
        return queries.create_project(project)
    except Exception as e:
        print(f"err creating project: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"database error: {e}",
        )


@app.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: int, auth_result=Security(auth.verify)):
    project = queries.get_project(project_id)
    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"project with id {project_id} not found",
        )
    try:
        return queries.delete_project(project_id)
    except Exception as e:
        print(f"err deleting project: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"database error: {e}",
        )
