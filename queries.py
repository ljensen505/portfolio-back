from db import mydb
from models import About, Project


def get_projects():
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM projects")
    data = cursor.fetchall()
    projects = [Project(**p) for p in data]  # type: ignore

    return projects


def get_about():
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT name, email, bio, github, linkedin FROM self")
    data = {key: val for key, val in cursor.fetchone().items()}  # type: ignore

    return About(**data)
