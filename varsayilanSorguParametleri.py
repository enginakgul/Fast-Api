
from typing import Union


from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}{q}")
async def read_item(item_id: str, q: Union[str,None]=None):
    if q:
        return {"item_id": item_id, "q":q}
    return {"item_id":item_id}


