from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()

@app.get("/")
async def read_root():
    return {'responce': 'Hello World'}


@app.post('/posts')
async def post(retrieve: dict = Body(...)):
    print(retrieve)
    return {'new post': f' title {retrieve['title']}, content {retrieve['value']} '}