## Fixing the error in the API

Let's fix the broken feature

`nano src/main.py`{{exec}} or

`vim src/main.py`{{exec}}

Here is a flowchart illustrating expected behavior of how division by zero should be handled to avoid the `ZeroDivisionError`.

<p align="center">
  <img src="./feature.png" width="350px">
</p>

**Hint**: Use a conditional statement (`if`).