"""
Continuing with the previous example, it will be common to have more than one related model.

This is especially the case for user models, because:

    The input model needs to be able to have a password.
    The output model should not have a password.
    The database model would probably need to have a hashed password.

"""


from typing import Dict, List, Optional, Union, Any
from fastapi import Body, FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Optional[str] = None

def fake_password_hasher(raw_password: str) -> str:
    return "supersecret" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved. .. not really")
    return user_in_db

@app.post("/user", response_model=UserOut)
async def create_user(user_in: UserIn = Body(...)):
    user_saved = fake_save_user(user_in)
    return user_saved

"""
Reduce duplication¶

Reducing code duplication is one of the core ideas in FastAPI.

As code duplication increments the chances of bugs, security issues, code desynchronization issues (when you update in one place but not in the others), etc.

And these models are all sharing a lot of the data and duplicating attribute names and types.
"""

class UserBase(BaseModel):
    username: str
    email: EmailStr
    fullname: Optional[str] = None

class UserIn1(UserBase):
    password: str

class UserOut1(UserBase):
    pass

class UserInDB1(UserBase):
    hashed_password: str


def fake_password_hasher_1(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user_1(user_in: UserIn1):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB1(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db

@app.post("/user1", response_model=UserOut1)
async def create_user_1(user_in: UserIn1):
    user_saved = fake_save_user_1(user_in)
    return user_saved

"""
Union or anyOf¶

You can declare a response to be the Union of two types, that means, that the response would be any of the two.

It will be defined in OpenAPI with anyOf.
"""

class BaseItem(BaseModel):
    description: str
    type: str

class CarItem(BaseItem):
    type = "car"

class PlaneItem(BaseItem):
    type = "plane"
    size: int

items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

@app.get("/items/{item_id}", response_model=Union[CarItem, PlaneItem])
async def read_item(item_id: str):
    return items[item_id]


"""
send list of items

"""

class Item(BaseModel):
    name: str
    description: Optional[str] = None

items = [
    {"name": "item1", "description": "desc1"},
    {"name": "item2"}
]

@app.get("/items", response_model=List[Item])
async def get_items():
    return items

"""
Sending dictionary with types
"""

@app.get("/keyword_weights", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}


