

from fastapi import Body, FastAPI
from pydantic import BaseModel


app = FastAPI()

class ItemName(BaseModel):
    name:str
    



@app.post("/items/",status_code=201)

async def create_item(name:ItemName = Body(..., embed = False)):
    return {"name": name}


