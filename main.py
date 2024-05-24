from fastapi import FastAPI
from pydantic import BaseModel
from typing import List,Optional
from uuid import UUID,uuid4
app = FastAPI()


class Task(BaseModel):
    id: Optional[UUID]=None
    title: str
    description:Optional[str]=None
    completed:bool=False


@app.post('/tasks/',response_class=Task)
def create_task(task:Task):
    task.id= uuid4
    tasks.apped(task)
    return task

tasks= []


@app.get('/tasks/',response_model=List[Task])
async def read_tasks():
    return {"hello":"world"}


@app.get("/tasks/{task_id}",response_model=Task)
def read_task(task_id:UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    return HTTPException(status_code=404,detail="Task not found")

if __name__=="__main__":
    import uvicorn

uvicorn.run(app,host="0.0.0.0",port="8000")

