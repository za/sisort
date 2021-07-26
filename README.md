sisort
======
sandbox isort

Create virtualenvironment
```
$ virtualenv .env
```

Then we need to install pre-commit
```
(.env) $ pip install pre-commit
```

Initiate git:
```
$ git init
```

Add a pre-commit configuration
```
$ vim .pre-commit-config.yaml
```

in this example I copied from Django project.

Run:
```
$ pre-commit install
```

Reference: https://pre-commit.com/

Create a simple python script importing datetime module:
```
(.env) $ vim src/abrakadabra/views.py

from datetime import timedelta
from datetime import datetime


def index():
    pass
```

isort will complaining because we should import datetime first
then timedelta (importing module should be in alphabetical order).

When we're trying to commit, we will see this:
```
(.env) $ gc

(.env) ➜  sisort git:(master) ✗ gc
isort....................................................................Failed
- hook id: isort
- files were modified by this hook

Fixing /home/za/git/sisort/src/abrakadabra/views.py
```

isort will automatically make the change:
```
(.env) ➜  sisort git:(master) ✗ gapa    
diff --git a/src/abrakadabra/views.py b/src/abrakadabra/views.py
index 08b8a38..b9a73c9 100644
--- a/src/abrakadabra/views.py
+++ b/src/abrakadabra/views.py
@@ -1,5 +1,4 @@
-from datetime import timedelta
-from datetime import datetime
+from datetime import datetime, timedelta
```
