from pydantic import BaseModel


class About(BaseModel):
    name: str
    email: str
    bio: str
    github: str


class Project(BaseModel):
    id: int | None = None
    name: str
    description: str
    source: str | None = None
    live: str | None = None
    is_self_hosted: bool = False
