from db import connect_db
from models import About, Project


def get_projects() -> list[Project]:
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM projects")
    data = cursor.fetchall()
    projects = [Project(**p) for p in data]  # type: ignore
    db.close()
    return projects


def get_project(project_id: int) -> Project | None:
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM projects WHERE id=%s", (project_id,))
    data = cursor.fetchone()
    db.close()

    return None if data is None else Project(**data)  # type: ignore


def create_project(project: Project) -> Project:
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


def delete_project(project_id: int) -> None:
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("DELETE FROM projects WHERE id=%s", (project_id,))
    db.commit()
    db.close()


def get_about() -> About:
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT name, email, bio, github, linkedin FROM self")
    data = {key: val for key, val in cursor.fetchone().items()}  # type: ignore
    db.close()
    return About(**data)
