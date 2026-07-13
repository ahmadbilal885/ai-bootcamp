from fastapi import APIRouter, HTTPException
from app.database import todos
from app.models import Todo, TodoCreate, TodoUpdate

router = APIRouter()


# Create Todo
@router.post("/todos")
def create_todo(todo: TodoCreate):

    new_todo = Todo(
        id=len(todos) + 1,
        title=todo.title,
        completed=False
    )

    todos.append(new_todo)

    return new_todo


# Get All Todos
@router.get("/todos")
def get_all_todos():
    return todos


# Get Todo by ID
@router.get("/todos/{id}")
def get_todo(id: int):

    for todo in todos:
        if todo.id == id:
            return todo

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# Update Todo
@router.put("/todos/{id}")
def update_todo(id: int, updated_todo: TodoUpdate):

    for todo in todos:

        if todo.id == id:

            todo.title = updated_todo.title
            todo.completed = updated_todo.completed

            return todo

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# Delete Todo
@router.delete("/todos/{id}")
def delete_todo(id: int):

    for index, todo in enumerate(todos):

        if todo.id == id:

            todos.pop(index)

            return {
                "message": "Task deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )