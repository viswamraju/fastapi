
from typing import Dict, List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl


app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list = []

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

"""
List fields with type parameter

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []

If we want unique tags
    tags: Set[str] = set()

Nested models

"""

class Image1(BaseModel):
    url: HttpUrl
    name: str

class Item1(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    image: Optional[List[Image1]] = None

@app.put("/nmitems/{item_id}")
async def update_item(item_id: int, item: Item1):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image1]):
    return images


"""
Bodies of arbitrary dicts
"""

@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
