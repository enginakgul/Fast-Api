

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel



class Item(BaseModel):
    name: str
    description: Union[str,None]=None
    price:float
    tax: Union[float,None]=None
    
app = FastAPI()

class User(BaseModel):
    username : str
    fullName: Union[str,None] = None

@app.post("/items/")
async def create_item(item_id: int, q: Union[str,None] = None, item: Union[Item, None ] =None,user:Union[User,None]=None):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user":user})
    return results



