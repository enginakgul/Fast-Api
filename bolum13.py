

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field


app = FastAPI()

"""class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name : Union[str,None] = None

class UserIn(UserBase):
    password: str
    
class UserOut(UserBase):
    pass

@app.post("/user/", response_model= UserIn)
async def create_user(user:UserIn):
    return user

@app.post("/users/",response_model=UserOut)
async def user_out(user:UserOut):
    return user"""

class UserBase(BaseModel):
    username: str = Field(..., example = "Engin")
    email: EmailStr = Field(..., example = "engin@hotmsil.com")
    full_name: Union[str,None]=Field(None,example = "ejofdlkmf")

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str    
def fake_password_hasher(raw_password: str):
    return "supersecret"+ raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(),hashed_password = hashed_password)
    print("User saved! .... not really")
    return user_in_db

@app.post("/user/",response_model= UserOut)
async def create_user(user_in:UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

