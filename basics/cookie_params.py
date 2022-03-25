from typing import Optional
from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get("/items")
async def get_items(ads_id: Optional[str] = Cookie(None)):
    print(ads_id)
    return {"ads_id": ads_id}