from typing import Optional
from fastapi import FastAPI

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

"""
When you declare other function parameters that are not part of the path parameters, 
they are automatically interpreted as "query" parameters.

http://localhost:8000/items?skip=1&limit=1

As query parameters are not a fixed part of a path, they can be optional and can have default values.

In the example below they have default values of skip=0 and limit=10.

"""
@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
     return fake_items_db[skip: skip + limit]


"""
The same way, you can declare optional query parameters, by setting their default to None:
"""

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

"""
Required query parameters¶

When you declare a default value for non-path parameters (for now, we have only seen query parameters), then it is not required.

If you don't want to add a specific value but just make it optional, set the default as None.

But when you want to make a query parameter required, you can just not declare any default value:

"""

@app.get("/items_/{item_id}")
async def read_item(item_id: str, needy: str):
    return {"item_id": item_id, "needy": needy}
    