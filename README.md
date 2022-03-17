# fastapi

### Creating virtual env

    pipenv shell   -- to create virtualenv for a package
    create requirements.txt

    pipenv install -r requirements.txt

### Running flask app

    uvicorn --reload simple_app:app

    http://localhost:8000/doc, http://localhost:8000/redoc

    http://127.0.0.1:8000/openapi.json

### we can use differnt http methods

    You can also use the other operations:
    @app.get()
    @app.post()
    @app.put()
    @app.delete()

    And the more exotic ones:

    @app.options()
    @app.head()
    @app.patch()
    @app.trace()
