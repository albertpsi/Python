# Python Importing Modules Quick Revision

Based on:

- `5.1-Import modules & packages.ipynb`
- `5.2-Standard Library.ipynb`

## 1. Modules and Packages

### Core idea

- A **module** is a single `.py` file containing reusable code.
- A **package** is a folder of related modules (typically with `__init__.py`).
- Imports help you organize code and avoid rewriting logic.

### Common import styles

```python
import math
from math import sqrt, pi
import numpy as np
from package import maths
from package.maths import addition
```

### Key points for revision

- `import module` -> use as `module.name` (example: `math.sqrt(16)`).
- `from module import name` -> use directly (`sqrt(16)`).
- `import module as alias` -> short names (`numpy as np`).
- `from module import *` works, but avoid it in real projects (namespace pollution).
- Custom package imports depend on correct folder structure + Python path.

---

## 2. Standard Library Essentials

### `array`

```python
import array as arr
nums = arr.array('i', [1, 2, 3])
```

- Efficient typed arrays.
- Type code decides stored data type (`'i'`, `'f'`, `'d'`, etc.).

### `math`

```python
import math
math.sqrt(16)
math.sin(math.pi / 2)
```

- Numeric functions and constants.

### `random`

```python
import random
random.randint(1, 10)
random.choice(['apple', 'banana', 'cherry'])
```

- Random number/item generation.

### `os` + `time`

```python
import os
import time
os.getcwd()
os.mkdir('test_directory')
time.sleep(1)
os.rmdir('test_directory')
```

- OS-level directory/file tasks and timing delays.

### `shutil`

```python
import shutil
shutil.copy('source_file.txt', 'destination_file.txt')
```

- High-level file operations like copy/move.

### `json`

```python
import json
s = json.dumps({'name': 'Alice', 'age': 30})
data = json.loads(s)
```

- Serialize Python objects to JSON and parse back.

### `csv`

```python
import csv
```

- Read/write CSV with `csv.writer` and `csv.reader`.

### `datetime`

```python
from datetime import datetime, timedelta
now = datetime.now()
yesterday = now - timedelta(days=1)
```

- Date/time calculations.

### `re`

```python
import re
re.search(r'fox', 'The quick brown fox')
```

- Pattern matching with regular expressions.

---

## Quick Comparison Table

| Style | Meaning | Example |
| ----- | ------- | ------- |
| `import m` | Import full module | `import math` |
| `from m import x` | Import specific members | `from math import sqrt` |
| `import m as a` | Import with alias | `import numpy as np` |
| `from m import *` | Import all public members | `from math import *` |

---

## Frequently Asked Interview Questions (Short Answers)

1. **Module vs package?**

- Module = one `.py` file.
- Package = collection of modules in a folder.

2. **Why use alias like `np`?**

- Improves readability and avoids long names.

3. **Why avoid `from x import *`?**

- It pollutes namespace and can cause naming conflicts.

4. **`json.dumps()` vs `json.loads()`?**

- `dumps`: Python object -> JSON string.
- `loads`: JSON string -> Python object.

5. **When use `shutil` instead of `os`?**

- For high-level operations like full file copy/move.

6. **How to import from a custom package?**

- Ensure proper package structure and run script from a path where package is discoverable.

---

## Last-Minute Revision Checklist

- Know all common import syntaxes.
- Understand module vs package distinction.
- Practice alias imports (`as`).
- Revise common standard library modules: `math`, `random`, `os`, `shutil`, `json`, `csv`, `datetime`, `re`.
- Avoid wildcard imports in production code.
