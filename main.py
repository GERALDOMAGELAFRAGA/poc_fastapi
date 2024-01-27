from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {'message':'Hello World'}

@app.get("/users/me")
async def read_user_me():
    return {'user_id':'the current user'}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {'user_id': user_id}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {'item_id':item_id}