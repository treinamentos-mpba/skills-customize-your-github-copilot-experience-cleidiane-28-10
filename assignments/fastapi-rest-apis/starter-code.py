from typing import Dict, List, Optional

from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI(title="Tasks API")


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class Task(TaskCreate):
    id: int


# Armazenamento temporário em memória.
tasks: Dict[int, Task] = {}
next_task_id = 1


@app.get("/")
def read_root():
    pass


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    pass


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updates: TaskUpdate):
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    pass
