Now you can add your own test case. Try to write one similar to the example!

`nano tests/test_example.py`{{exec}}

`vim tests/test_example.py`{{exec}}

Hint: you could test if the divide endpoint return correct status code with string as request input.

```
def test_divide_input_string():
    response = client.get("/divide?a=a&b=b")
    assert response.status_code == 422
``` 

Other test cases:
- Test if the divide endpoint responses with correct type of content.
- Test if the divide endpoint responses with correct answer.
- ...


