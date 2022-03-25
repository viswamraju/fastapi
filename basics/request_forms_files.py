"""
You can define files and form fields at the same time using File and Form.
"""

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

@app.post("/register")
async def request_form_file(
    *,
    username: str = Form(...),
    password: str = Form(...),
    file: UploadFile = File(...)
):
    file_content = await file.read()
    return {
        "username": username,
        "password": password,
        "file_name": file_content
    }