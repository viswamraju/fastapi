
from typing import Optional
from fastapi import Body, FastAPI, Path
from pydantic import BaseModel, Field

"""
The same way you can declare additional validation and metadata in path operation 
function parameters with Query, Path and Body, 
you can declare validation and metadata inside of Pydantic models using Pydantic's Field.
"""

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = Field(None, title="Description of the item", max_length=300)
    price: float = Field(..., gt=0, description="must be greater then zero")
    tax: Optional[float] = None



@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="Item ID"),
    item: Item = Body(..., embed=True)
):
    results = {"item_id": item_id, "item": item}
    return results