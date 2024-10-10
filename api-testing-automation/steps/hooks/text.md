`cd .git/hooks`{{exec}}

`touch pre-commit`{{exec}}

`echo '#!/bin/sh \n echo hello' > pre-commit`{{exec}}

`chmod +x pre-commit`{{exec}}
