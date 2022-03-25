"""
You can define files to be uploaded by the client using File.

If you declare the type of your path operation function parameter as bytes, FastAPI will read the file for you and you will receive the contents as bytes.

Have in mind that this means that the whole contents will be stored in memory. This will work well for small files.

But there are several cases in which you might benefit from using UploadFile.

UploadFile has the following attributes:

    filename: A str with the original file name that was uploaded (e.g. myimage.jpg).
    content_type: A str with the content type (MIME type / media type) (e.g. image/jpeg).
    file: A SpooledTemporaryFile (a file-like object). This is the actual Python file that you can pass directly to other functions or libraries that expect a "file-like" object.

UploadFile has the following async methods. They all call the corresponding file methods underneath (using the internal SpooledTemporaryFile).

    write(data): Writes data (str or bytes) to the file.
    read(size): Reads size (int) bytes/characters of the file.
    seek(offset): Goes to the byte position offset (int) in the file.
        E.g., await myfile.seek(0) would go to the start of the file.
        This is especially useful if you run await myfile.read() once and then need to read the contents again.
    close(): Closes the file.

As all these methods are async methods, you need to "await" them.

For example, inside of an async path operation function you can get the contents with:

contents = await myfile.read()

If you are inside of a normal def path operation function, you can access the UploadFile.file directly, for example:

contents = myfile.file.read()

async Technical Details
"""

from typing import List, Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    return {"filename": file.filename}

"""
Optional file upload
"""

@app.post("/files1")
async def create_file(file: Optional[bytes] = File(None)):
    if not file:
        return {"message": "no file"}
    else:
        return {"file_size": len(file)}

@app.post("/uploadfile1")
async def upload_file_optional(file: Optional[UploadFile] = File(None, description="File to upload")):
    if not file:
        return {"message": "No file to upload"}
    else:
        return {"file_name": file.filename}


"""
Multiple file uploads
"""

@app.post("/files2")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}

@app.post("/uploadfiles2")
async def upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}

@app.get("/")
async def main():
    content = """
    <body>
<form action="/files2/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles2/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)