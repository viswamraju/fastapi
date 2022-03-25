
from typing import Optional
from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the Item to get", ge=0, lt=1000),
    q: Optional[str] = None,
    item: Optional[Item] = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

"""
In the previous example, the path operations would expect a JSON body with the attributes of an Item, like:

{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}

But you can also declare multiple body parameters, e.g. item and user:
"""

class User(BaseModel):
    name: str
    place: str

@app.put("/mitems/{item_id}")
async def mul_body_params(
    *,
    item_id: int = Path(..., title="Item ID", ge=0, lt=1000),
    q: Optional[str]= Query(None),
    item: Optional[Item] = None,
    user: Optional[User] = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    return results

"""
The same way there is a Query and Path to define extra data for query and path parameters, 
FastAPI provides an equivalent Body.
"""

@app.put("/bitems/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: int = Body(...)
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

"""
    Embed a single body parameter¶

Let's say you only have a single item body parameter from a Pydantic model Item.

By default, FastAPI will then expect its body directly.

But if you want it to expect a JSON with a key item and inside of it the model contents, as it does when you declare extra body parameters, you can use the special Body parameter embed:

item: Item = Body(..., embed=True)

In this case FastAPI will expect a body like:

{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}

instead of:

{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
"""

@app.put("/emitems/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


