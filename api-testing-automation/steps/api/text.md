`cat src/main.py`{{exec}}

Now, start the provided example API using Uvicorn, to not affect on our terminal, leave it running in the background.
`uvicorn src.main:app --reload --port 8000 &`{{exec}}

Since the API is running, we can try to send request to it. Here we send a HTTP request to the API's root endpoint.
`curl http://127.0.0.1:8000/`{{exec}}
