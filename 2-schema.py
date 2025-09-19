from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
class Structure(BaseModel):
    title: str
    value: str
    upload: bool = True
    rating: Optional[int] = None


app = FastAPI()
@app.get('/')
def read_root():
    return {'data': 'hello world'}

@app.post('/posts')
def create_post(post: Structure):
    print(post)
    print(post.dict())
    return {'data': post}