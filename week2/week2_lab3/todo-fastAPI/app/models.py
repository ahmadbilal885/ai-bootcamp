from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
    completed: bool


class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    title: str
    completed: bool