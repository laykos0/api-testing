## Fixing the API 

Let's **fix** the **broken endpoint** by editing the API source code. Open the file `main.py` using your preferred text editor:

`nano src/main.py`{{exec}} or

`vim src/main.py`{{exec}}

Now, **modify** the code for `GET /divide` endpoint to **handle division by zero** appropriately.

## Expected Behavior

The expected behavior of how division by zero should be handled to avoid the `ZeroDivisionError` is illustrated in the flowchart below.

<p align="center">
  <img src="./feature.png" width="350px">
</p>

According to the flowchart, the `/divide` endpoint should **check the value of b** and handle the case in which `b` has a value of `0`, returning a custom response `{"result": "infinity"}`.



**Hint**: Use a conditional statement (`if`).