## Create pre-commit Hook 
First, switch to the **Git Hooks** directory.

`cd .git/hooks`{{exec}}

Create the `pre-commit` file.

`touch pre-commit`{{exec}}

Change the **permission** to make it **executable**.

`chmod +x pre-commit`{{exec}}

## Edit the pre-commit

Use your favorite editor to open the file and modify it. You can use either `vim` or `nano`:

`vim pre-commit`{{exec}} or

`nano pre-commit`{{exec}}

Add the following line to the `pre-commit` file to **automatically run tests** before **each commit**:

`pytest tests`{{copy}}

## Shortcut
Alternatively, you can just write the line to the file directly with `echo`.

`echo 'pytest tests' > pre-commit`{{exec}}
