from db import connect_db
from models import About, Project


def get_projects():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM projects")
    data = cursor.fetchall()
    projects = [Project(**p) for p in data]  # type: ignore
    db.close()
    return projects


def get_about():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT name, email, bio, github, linkedin FROM self")
    data = {key: val for key, val in cursor.fetchone().items()}  # type: ignore
    db.close()
    return About(**data)
