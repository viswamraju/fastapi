"""
You can declare examples of the data your app can receive.

Here are several ways to do it.
"""


from doctest import Example
from typing import Optional
from fastapi import Body, FastAPI, Path
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 100,
                "tax": 3.2
            }
        }


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="Item ID", ge=0, lt=1000),
    item: Item
):
    results = {"item_id": item_id, "item": item}
    return results

"""
Using fields Additional Arguments
"""

class Item1(BaseModel):
    name: str = Field(..., example="Foo1")
    description: Optional[str] = Field(None, example="desc1")
    price: float = Field(..., example="10.0")
    tax: Optional[float] = Field(None, example="3.1")


@app.put("/items1/{item_id}")
async def update_item(item_id, item: Item1):
    return {"item_id": item_id, "item": item}


"""
Body with example
"""

@app.put("/items2/{item_id}")
async def update_item(
    item_id, 
    item: Item1 = Body(..., example={"name": "foo2", "desc": "desc2", "price": 19, "tax": 3.6})
):
    return {"item_id": item_id, "item": item}

"""
    Body with multiple examples
"""

@app.put("/items3/{item_id}")
async def update_item(
    item_id, 
    item: Item1 = Body(..., examples={
        "normal_data": {
            "summary": "example1",
            "description": "desc1",
            "value": {
                "name": "Foo1",
                "description": "desc1",
                "price": 52.6,
                "tax": 3.9
            }
        },
        "minimal_data": {
            "summary": "Minimal data",
            "description": "Desc2",
            "value": {
                "name": "Foo2",
                "price": 52.6
            }
        },
        "invalid_data": {
            "summary": "Invalid data",
            "description": "Desc3",
            "value": {
                "name": "Foo2",
                "price": "Baz"
            }
        }
    })
):
    return {"item_id": item_id, "item": item}



