Show the example test

`cat tests/test_example.py`{{exec}}

We see that test cases are simply requesting the root endpoint the example endpoint, the test cases are through when we get the responses with status code = 200, indicating the request was successful.

Now run the example test

`pytest tests/test_example.py`{{exec}}

However, the test for the example endpoint failed, due to a ZeroDIvisionError.
