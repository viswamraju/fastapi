from typing import List, Optional
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"useragent": user_agent}

"""
    Duplicate headers
"""

@app.get("/items1/")
async def read_items(x_token: Optional[List[str]] = Header(None)):
    return {"X-Token values": x_token}