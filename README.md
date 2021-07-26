sisort
======
sandbox isort

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

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

Added flake8 in pre-commit-config.yaml

Now we can prevent the new commit from having (example) syntax error.
I believe we can configure this flake8.

```
➜  sisort git:(main) ✗ gc
isort....................................................................Passed
flake8...................................................................Failed
- hook id: flake8
- exit code: 1

src/abrakadabra/report.py:5:18: E999 SyntaxError: invalid syntax
```

So we can't commit until we fix this.

We can also have cleaner code if we have imported module but not being used:

```
➜  sisort git:(main) ✗ gc
isort....................................................................Passed
flake8...................................................................Failed
- hook id: flake8
- exit code: 1

src/abrakadabra/report.py:1:1: F401 'datetime' imported but unused
```

I believe there will be pros/cons of using pre-commit hook. It will make commit harder.
Applying this at the beginning of the project seems great, but we need to discuss with
the team if we're planning to apply this in ongoing project.