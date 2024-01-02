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


def get_project(project_id: int):
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM projects WHERE id=%s", (project_id,))
    data = cursor.fetchone()
    db.close()
    return Project(**data)  # type: ignore


def create_project(project: Project):
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO projects (name, description, source, live) VALUES (%s, %s, %s, %s)",
        (project.name, project.description, project.source, project.live),
    )
    db.commit()
    project.id = cursor.lastrowid
    db.close()
    return project


def delete_project(project_id: int):
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("DELETE FROM projects WHERE id=%s", (project_id,))
    db.commit()
    db.close()


def get_about():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT name, email, bio, github, linkedin FROM self")
    data = {key: val for key, val in cursor.fetchone().items()}  # type: ignore
    db.close()
    return About(**data)
