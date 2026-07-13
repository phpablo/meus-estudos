from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List

app = FastAPI()

class Task(BaseModel):
  id: int
  title: str
  description: Optional[str] = None
  done: bool = False

tasks_db = []

@app.get("/tasks",response_model=List[Task])