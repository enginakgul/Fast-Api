

from typing import Union
from tkinter.messagebox import NO
from fastapi import Body, FastAPI
from pydantic import BaseModel, HttpUrl

class Image(BaseModel):
    url : HttpUrl
    name : str


class Item(BaseModel):
    name: str
    description: Union[str,None] = None
    price : float
    tax : Union[str,None] = None
    tags : set[str] = set()
    image: Union[list[Image],None] = None


class Offer(BaseModel):
    name : str
    description: Union [str,None] = None
    price : float
    items : list[Item]
    


app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id:int, item:Item):
    results = {"item":[{"item_id": item_id},{"item": item}]}
    return results


@app.post ("/offers")
async def creat_offer(offer: Offer = Body(..., embed = True)):
    return offer

@app.put("/blahs")
async def create_some_blahs(blahs: dict[int,float]):
    return blahs