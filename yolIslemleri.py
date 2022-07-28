

from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name : str
    description: Union[str,None] = None
    price: float
    tax : Union[float,None] = None
    tags : set[str] = set()
    

@app.get("/items",response_model=Item,summary="Create an item",description="Create an item with all the information, name, description, price, tax and set of")
async def create_item(item_id:int,item:Item):
    return {"item_id": item_id,"item":item}