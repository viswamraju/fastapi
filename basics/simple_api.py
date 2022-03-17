from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def index():
    return "pong"
    # You can return a dict, list, singular values as str, int, etc.