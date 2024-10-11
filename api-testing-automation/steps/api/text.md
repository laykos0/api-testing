First, let's take a look at the provided API script.

`cat src/main.py`{{exec}}

Now, start the provided example API using Uvicorn, to not affect on our terminal, leave it running in the background.

`uvicorn src.main:app --reload --port 8000 &`{{exec}}

Since the API is running, you can try to send request to it. 

Here is an example:

`curl "http://127.0.0.1:8000/divide?a=6&b=3"`{{exec}}

This command sends a HTTP request to the API's divide endpoint, with two query parameters, *a = 6* and *b = 3*. The expected response is **{"result":2}**.