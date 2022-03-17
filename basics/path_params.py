from email import message
from fastapi import FastAPI

# App instance
app = FastAPI()

# path params in path
# The value of the path parameter name and greet will be passed to your function as the argument 
@app.get("/greet/{name}/{greet}")
async def greet(name, greet):
    return f"{greet}, {name}"

# path params with type
# In this case, item_id is declared to be an int. 
# While using this api if we pass other than integer we will get error
# So, with that type declaration, FastAPI gives you automatic request "parsing".
@app.get("/items/{item_id}")
async def items(item_id: int):
    return {"item": item_id}


"""
When creating path operations, you can find situations where you have a fixed path.

Like /users/me, let's say that it's to get data about the current user.

And then you can also have a path /users/{user_id} to get data about a specific user by some user ID.

Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}:

Otherwise, the path for /users/{user_id} would match also for /users/me, "thinking" that it's receiving a parameter user_id with a value of "me".
"""

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


"""
Pre defined values in path param
If you have a path operation that receives a path parameter, but you want the possible 
valid path parameter values to be predefined, you can use a standard Python Enum.
Create an Enum class¶

Import Enum and create a sub-class that inherits from str and from Enum.

By inheriting from str the API docs will be able to know that the values must 
be of type string and will be able to render correctly.

Then create class attributes with fixed values, which will be the available valid values:
"""

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, "message": "Deep learning FTW!"}
    if model_name.value == "lenet":
        return {'model_name': model_name, "message": "LeCNN all the images"}
    return {'model_name': model_name, "message": "Have some residuals"}

"""
Path parameters containing paths¶

Let's say you have a path operation with a path /files/{file_path}.

But you need file_path itself to contain a path, like home/johndoe/myfile.txt.

So, the URL for that file would be something like: /files/home/johndoe/myfile.txt.

Using an option directly from Starlette you can declare a path parameter 
containing a path using a URL like:

/files/{file_path:path}

In this case, the name of the parameter is file_path, and the last part, :path, 
tells it that the parameter should match any path.
"""

@app.get("/files/{file_path:path}")
async def file_path(file_path: str):
    return {"file_path": file_path}
