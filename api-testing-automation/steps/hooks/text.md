`cd .git/hooks`{{exec}}

`touch pre-commit`{{exec}}

`echo '#!/bin/sh pytest test_main.py' > pre-commit`{{exec}}

`chmod +x pre-commit`{{exec}}
