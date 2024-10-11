## Fixing the error in the API

Let's fix the broken feature

`nano src/main.py`{{exec}} or

`vim src/main.py`{{exec}}

Here is a flowchart illustrating expected behavior of how division by zero should be handled to avoid the `ZeroDivisionError`.

<p align="center">
  <img src="./feature.png" width="350px">
</p>

In the flowchart, we see that the divide endpoint should check on b, and return different response based on the value of b.

**Hint**: Use a conditional statement (`if`).