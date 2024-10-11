Now switch to the Git hooks directory.
`cd .git/hooks`{{exec}}

Create the pre-commit file.
`touch pre-commit`{{exec}}

Make the file executable.
`chmod +x pre-commit`{{exec}}

Use your favorite editor to open the file and modify it.

`vi pre-commit`{{exec}}

`nano > pre-commit`{{exec}}

And add this line to the file.

`pytest tests`{{copy}}

Or just add to the file directly here.
`echo 'pytest tests' > pre-commit`{{exec}}
