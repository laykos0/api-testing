Now switch to the Git hooks directory.
`cd .git/hooks`{{exec}}

Create the file pre-commit.
`touch pre-commit`{{exec}}

Make the file executable.
`chmod +x pre-commit`{{exec}}

Use your favorite editor to open the file and modify it.
`vi pre-commit`{{exec}}

`nano > pre-commit`{{exec}}

Or just add to the file directly here.
`echo '#!/bin/sh \n pytest tests' > pre-commit`{{exec}}

`#!/bin/sh`{{copy}}
`pytest tests`{{copy}}
