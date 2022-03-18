from typing import List, Optional
from fastapi import FastAPI, Query

app = FastAPI()

"""
Basic validation
just checks q is optional string
"""

@app.get("/items")
async def read_items(q: Optional[str] = None):
    result = {"item1": "foo", "item2": "bar"}
    if q:
        result.update({"q": q})
    return result

"""
Additional validation for query params.
We are going to enforce that even though q is optional, 
whenever it is provided, its length doesn't exceed 50 characters.
To achieve that, first import Query from fastapi:

q: Optional[str] = Query(None)

...makes the parameter optional, the same as:

q: Optional[str] = None

You can also add a parameter min_length:
Query(None, min_length=3, max_length=50, regex="^fixedquery$")

We can have other than than None as default value
Query("fixedquery", min_length=3)

So, when you need to declare a value as required while using Query, 
you can use ... as the first argument:

If you hadn't seen that ... before: 
it is a special single value, it is part of Python and is called "Ellipsis"

"""

@app.get("/items/qv")
async def read_items_qv(q: Optional[str] = Query(..., max_length=10)):
    result = {"item1": "foo", "item2": "bar"}
    if q:
        result.update({"q": q})
    return result

"""
Query parameter list / multiple values¶

When you define a query parameter explicitly with Query you can also 
declare it to receive a list of values, or said in other way, to receive multiple values.

For example, to declare a query parameter q that can appear multiple times in the URL, you can write:

with default multiple values
q: List[str] = Query(["foo", "bar"])

You can add more information about the parameter.

That information will be included in the generated OpenAPI and used by 
the documentation user interfaces and external tools.

title, description

q: Optional[str] = Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )

"""

@app.get("/items/ql")
async def read_items_qlist(q: Optional[List[str]] = Query(None, alias="q-item", deprecated=True, include_in_schema=True)):
    query_items = {"q": q}
    return query_items


"""
Alias parameters¶

Imagine that you want the parameter to be item-query.

Like in:

http://127.0.0.1:8000/items/?item-query=foobaritems

But item-query is not a valid Python variable name.

The closest would be item_query.

But you still need it to be exactly item-query...


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

We can also mark the query param as deprecated

Exclude from OpenAPI¶

To exclude a query parameter from the generated OpenAPI schema 
(and thus, from the automatic documentation systems), 
set the parameter include_in_schema of Query to False:
"""


