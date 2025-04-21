from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI CRUD"}

#defining the model
class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

todos = []

# Create a new to-do item
@app.post("/todos/")
def create_todo(todo:"Todo"):
    todos.append(todo)
    return todo

#Read all to-do items
@app.get("/todos/")
def get_todos():
    return todos

#Display a specific to-do item by ID
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "To-do item not found!"}

#Updating existing to-do item
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return updated_todo
    return {"error": "To-do item not found!"}

#Deleting a to-do item
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "To-do item deleted!"}
    return {"error": "To-do item not found!"}