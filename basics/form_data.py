"""
When you need to receive form fields instead of JSON, you can use Form.
"""

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}

