"""
You can declare the model used for the response with the parameter response_model in any of the path operations:

    @app.get()
    @app.post()
    @app.put()
    @app.delete()
    etc.

"""
from turtle import title
from typing import List, Optional
from fastapi import Body, FastAPI, Query
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    result = {"name": item.name, "desc": item.description, "price": item.price}
    return result

"""
Now, whenever a browser is creating a user with a password, the API will return the same password in the response.

In this case, it might not be a problem, because the user themself is sending the password.

But if we use the same model for another path operation, we could be sending our user's passwords to every client.

Here, even though our path operation function is returning the same input user that contains the password:

we declared the response_model to be our model UserOut, that doesn't include the password:
"""

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    fullname: Optional[str] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    fullname: Optional[str] = None


@app.post("/user", response_model=UserOut)
async def create_user(user_in: UserIn = Body(...)):
    return user_in

"""
Use the response_model_exclude_unset parameter¶

You can set the path operation decorator parameter response_model_exclude_unset=True:
"""

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []

items = [{"name": "item1", "price": 109.2}, {"name": "item2", "price": 107, "tags": ["tag1", "tag2"]}]
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def get_item(item_id: int = Query(..., title="ItemID", description="ItemID Desc", ge=0, lt=2)):
    return items[item_id]

