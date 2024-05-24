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


tasks= []


@app.get('/')
async def read():
    return {"hello":"world"}


if __name__=="__main__":
    import uvicorn

uvicorn.run(app,host="0.0.0.0",port="8000")

