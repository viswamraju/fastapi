"""
Response Status Code¶

You can define the (HTTP) status_code to be used in the response of your path operation.

You can pass directly the int code, like 404.
"""

from enum import Enum
from fastapi import FastAPI, status

app = FastAPI()

@app.get("/items/{name}", status_code=status.HTTP_200_OK)
async def get_item(name: str):
    return {"name": name}

"""
Use tags to group APIS in documentation /open api schema
"""

@app.get("/items1/{name}", status_code=status.HTTP_200_OK, tags=["tag1"])
async def get_item(name: str):
    return {"name": name}

@app.get("/items2/{name}", status_code=status.HTTP_200_OK, tags=["tag1"])
async def get_item(name: str):
    return {"name": name}

@app.get("/items3/{name}", status_code=status.HTTP_200_OK, tags=["tag2"])
async def get_item(name: str):
    return {"name": name}

@app.get("/items4/{name}", status_code=status.HTTP_200_OK, tags=["tag3"])
async def get_item(name: str):
    return {"name": name}

"""
Tags with Enums¶

If you have a big application, you might end up accumulating several tags, and you would want to make sure you always use the same tag for related path operations.

In these cases, it could make sense to store the tags in an Enum.

FastAPI supports that the same way as with plain strings:

summary="Get users as list", description="Returns the users info" in path operation

Response description,

response_description="All available items"

Deprecate a path operation,  deprecated=True


"""

class Tags(Enum):
    items = "items"
    users = "users"

@app.get("/users", tags=[Tags.users], summary="Get users as list", description="Returns the users info")
async def get_users():
    return {"users": ["user1", "user2"]}

@app.get("/items", tags=[Tags.items], response_description="All available items", deprecated=True)
async def get_items():
    """
        Get items
        - Get all item
        - Connect to db 
        - fetch all items
        - returns all items
    """
    return {"items": ["item1", "item2"]}
