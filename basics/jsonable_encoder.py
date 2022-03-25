from datetime import datetime
from typing import Optional
from fastapi import Body, FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    timestamp: datetime
    description: Optional[str] = None

fake_db = {}

@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(...)):
    print(type(item.timestamp))
    # json_compatible_item_data = jsonable_encoder(item)
    # fake_db[item_id] = json_compatible_item_data
    fake_db[item_id] = item
    return fake_db

