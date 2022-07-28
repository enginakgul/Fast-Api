

from typing import Union
from fastapi import Cookie, FastAPI


app  = FastAPI()

@app.get("/items")
async def read_items(cookie_id: Union[str,None]):
    
    return {"cookie_id": cookie_id}
    