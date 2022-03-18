from unittest import result
from fastapi import FastAPI, Path

app = FastAPI()


"""
The same way you can declare more validations and metadata for query parameters with Query, 
you can declare the same type of validations and metadata for path parameters with Path.
"""

@app.get("/items/{item_id}")
async def read_items(item_id: int = Path(..., title="The ID of the item to get", description="desc")):
    results = {"item_id": item_id}
    return results

"""
Number validations: greater than or equal¶

With Query and Path (and other's you'll see later) you can declare string constraints, 
but also number constraints.

Here, with ge=1, item_id will need to be an integer number "greater than or equal" to 1.


    gt: greater than
    le: less than or equal

"""

@app.get("/validation_numbers/{num}")
async def get_number(num: int = Path(..., gt=1, le=100, description="Should be ge 1")):
    return num
