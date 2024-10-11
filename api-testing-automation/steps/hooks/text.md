## Create pre-commit Hook File
First, switch to the Git hooks directory.

`cd .git/hooks`{{exec}}

Create the `pre-commit` file.

`touch pre-commit`{{exec}}

Change the permission to make it executable.

`chmod +x pre-commit`{{exec}}

## Edit the pre-commit File

Use your favorite editor to open the file and modify it. You can use either `vim` or `nano`:

`vim pre-commit`{{exec}}

`nano > pre-commit`{{exec}}

Add the following line to the `pre-commit` file to automatically run tests before each commit:

`pytest tests`{{copy}}

**Note**: Alternatively, you can just append the line to the file directly with `echo`.

`echo 'pytest tests' > pre-commit`{{exec}}
