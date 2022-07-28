

from ast import For
from fastapi import FastAPI, Form


app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(),password: str = Form()):
    return {"username" : username}

@app.post("/sign/")
async def sign(username: str = Form(),password : str = Form()):
    return 
