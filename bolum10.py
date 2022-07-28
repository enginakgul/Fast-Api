

from typing import Union
from fastapi import Body, FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str 
    description: Union[str,None] = None
    price : float
    tax : Union[float,None] = None
    """class Config:
        schema_extra = {"example":{"name":"Foo","description":"A very nice Item","price":16.25,"tax":1.67}}"""



app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id:int,item:Item = Body(...,
        examples={
            "normal": {
            "summary" : "A normal example",
            "description" : "A __normal__ item works _correctly_",
                "value":{
                    "name":"Foo",
                    "description": "A very nice Item",
                    "price":16.25,
                    "tax" : 1.67,
                },
            },
            "converted":{
                "summary": "An example with converted data",
                "description": "FastAPI can convert price 'string' to", 
                "value":{"name":"Bar","price":16.25},
            },
            "invalid":{
                "summary": "Invalid data is rejected with an error",
                "description": "Hello youtubers",
                "value": {"name":"Baz", "price":12.57},
            },
        })):
    results = {"item_id": item_id, "item": Item}
    return results

