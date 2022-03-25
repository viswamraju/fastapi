"""

The same way you can specify a response model, you can also declare the 
HTTP status code used for the response with the 
parameter status_code in any of the path operations:
"""

from fastapi import FastAPI, status

app = FastAPI()

@app.post("/items", status_code=201)
async def create_item(name: str):
    return {"name": name}

@app.post("/items1", status_code=status.HTTP_201_CREATED)
async def create_item_1(name: str):
    return {"name": name}
