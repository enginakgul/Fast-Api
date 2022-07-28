


from datetime import datetime, timedelta,time
from typing import Union
from uuid import UUID
from fastapi import FastAPI, Body


app = FastAPI()

@app.put("/items")
async def  read_items(
    item_id: UUID,
    start_datetime : Union[datetime, None] = None,
    end_datetime : Union[datetime,None] = None,
    repeat_at : Union[time,None] = Body(default = None),
    procces_after : Union[timedelta,None] = None,
):
    start_procces = start_datetime + procces_after
    duration  = end_datetime - start_procces
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "procces_after":procces_after,
        "start_procces": start_procces,
        "duration" : duration,
    }