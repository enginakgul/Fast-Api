

from fastapi import FastAPI



app = FastAPI()

@app.get("/items/",tags= ["items"])
async def read_items():
    return [{"name":"Foo","price":54}]

@app.get("/users/",tags=["users"])
async def read_users():
    return [{"username":"johndoe"}]

@app.get("/elements/",tags = ["itemss"])
async def read_elements():
    return [{"item_id":"Foo"}]