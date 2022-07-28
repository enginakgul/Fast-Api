
import time
from fastapi import FastAPI,Request


app = FastAPI()

@app.middleware("http")
async def add_procces_time_header(request: Request,call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-time"] = str(process_time)
    return response

    