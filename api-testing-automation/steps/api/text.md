## Review Provided API 
First, let's take a look at the provided source code of the API to understand its structure and functionality:


`cat src/main.py`{{exec}}

The provided API is a simple FastAPI asynchronous application that defines two endpoints: 

- `/`: Returns a simple welcome message.
- `/divide`: Accepts query parameters, `a` and `b`, and returns result of dividing `a` by `b`.


## Start the Example API with Uvicorn
Now, start the example API using Uvicorn and leave it running in the background.

`uvicorn src.main:app --reload --port 8000 &`{{exec}}

- **`--reload`**: Enables auto-reloading of the server on code changes.
- **`--port 8000`**: Specifies the port for the server to listen on.
- **`&`** : Runs the command in the background, allowing to continue using the terminal.

## Test the Running API


Since the API is running,  you can send requests to it.

Here is an example how to test the `/divide` endpoint:

`curl "http://127.0.0.1:8000/divide?a=6&b=3"`{{exec}}

This command sends a **HTTP** request to the API's `/divide` endpoint, with two query parameters, **`a = 6`** and **`b = 3`**. The expected response is **`{"result":2}`**.