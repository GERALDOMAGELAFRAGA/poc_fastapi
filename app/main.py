from fastapi import FastAPI, Form, Header
from enum import Enum
from typing import Annotated

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.post("/form/lp1")
async def form_lp1(
    name: Annotated[str, Form()], 
    phone: Annotated[str, Form()], 
    allow_origin: Annotated[str | None, Header()]=None):
    return {'name': name, 'phone': phone, "Access-Control-Allow-Origin": allow_origin}


@app.get("/")
async def root():
    return {'message':'Hello World'}

@app.get("/users/me")
async def read_user_me():
    return {'user_id':'the current user'}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {'user_id': user_id}

@app.get("/items/")
async def read_item_skip(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {'item_id':item_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path":file_path}


