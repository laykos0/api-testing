`cd .git/hooks`{{exec}}

`touch pre-commit`{{exec}}

`chmod +x pre-commit`{{exec}}

`vi pre-commit`{{exec}}

`nano > pre-commit`{{exec}}

`echo '#!/bin/sh pytest test_main.py' > pre-commit`{{exec}}

`#!/bin/sh`{{copy}}
`pytest tests`{{copy}}
