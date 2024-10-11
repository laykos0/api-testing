## Review Provided API 
First, let's take a look at the provided API script to understand its structure and functionality:


`cat src/main.py`{{exec}}

## Start the Example API with Uvicorn
Now, start the provided example API using Uvicorn, to not affect on our terminal, leave it running in the background.

`uvicorn src.main:app --reload --port 8000 &`{{exec}}

- **`--reload`**: Enables auto-reloading of the server on code changes.
- **`--port 8000`**: Specifies the port for the server.
- **`&`** : Runs the command in the background, allowing to continue using the terminal.

## Test the Running API


Since the API is running,  you can send requests to it.

Here is an example how to test the `GET /divide` endpoint:

`curl "http://127.0.0.1:8000/divide?a=6&b=3"`{{exec}}

This command sends a **HTTP** request to the API's `/divide` endpoint, with two query parameters, **`a = 6`** and **`b = 3`**. The expected response is **`{"result":2}`**.