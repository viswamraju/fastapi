from cgi import print_exception
from sys import flags
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict

"""
Request body + path parameters¶

You can declare path parameters and request body at the same time.

FastAPI will recognize that the function parameters that match path 
parameters should be taken from the path, and that function parameters 
that are declared to be Pydantic models should be taken from the request body.
"""

# @app.put("/items/{item_id}")
# async def get_item(item_id: int, item: Item):
#     return({"item_id": item_id, **item.dict()})

"""
Request body + path + query parameters¶

You can also declare body, path and query parameters, all at the same time.

FastAPI will recognize each of them and take the data from the correct place.
"""

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str]= None):
    result = {"item_id": item_id, **item.dict()}
    print(q)
    if q:
        result.update({'q': q})
    return result
