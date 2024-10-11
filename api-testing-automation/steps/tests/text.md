## Add Your Own Test Case
Now you can add your own test case. Try to write one similar to the example provided! 

You can use either `nano` or `vim` to edit the example test file. Choose your preferred text editor:

`nano tests/test_example.py`{{exec}} or

`vim tests/test_example.py`{{exec}}

**Note**: Make sure that the **name** of **your function** starts with `test_` (required by Pytest).

## Hint
You could test if the **divide endpoint** returns correct **status code** when given a **string** as **query parameter**.

```python
def test_divide_input_string():
    response = client.get("/divide?a=a&b=b")
    assert response.status_code == 422
``` 

Other possible test cases:
- Missing Query Parameters
- Correct Response Content Type
- Edge Cases (For example very large numbers)

## Run the Test Case
After adding your own test case you can run it by calling:

`pytest tests/test_example.py::$FUNCTION_NAME`{{copy}}

**Example**:
`pytest tests/test_example.py::test_root`{{exec}}

