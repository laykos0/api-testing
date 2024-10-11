## Add Your Own Test Case
Now you can add your own test case. Try to write one similar to the example provided! You can use either `nano` or `vim` to edit the example test file. Choose your preferred text editor:

`nano tests/test_example.py`{{exec}}

`vim tests/test_example.py`{{exec}}

**Hint**: you could test if the divide endpoint returns correct status code when given a string as query parameter.

```
def test_divide_input_string():
    response = client.get("/divide?a=a&b=b")
    assert response.status_code == 422
``` 

Other test cases:
- Test if the divide endpoint responses with correct type of content.
- Test if the divide endpoint responses with correct answer.
- ...


