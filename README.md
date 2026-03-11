# Python Revision Hub

This README combines the available revision notes across the `Python` folder into one quick-glance document.

Use this file when you want:
- a fast revision pass before practice or interviews
- one place to see all major topic summaries
- direct links to the full revision notes for each topic

## Available Revision Files

| Topic | Detailed Revision File |
| --- | --- |
| Data Structures | [Data-Structures-Quick-Revision.md](./3-Data%20Structures/Data-Structures-Quick-Revision.md) |
| Functions | [Functions-Quick-Revision.md](./4-Functions/Functions-Quick-Revision.md) |
| Importing Modules | [Importing-Modules-Quick-Revision.md](./5-Importing%20Modules/Importing-Modules-Quick-Revision.md) |
| File Handling | [File-Handling-Quick-Revision.md](./6-File%20Handling/File-Handling-Quick-Revision.md) |
| Exceptions | [Exceptions-Quick-Revision.md](./7-Exceptions/Exceptions-Quick-Revision.md) |
| Multithreading and Multiprocessing | [REVISION.md](./11-MultiThreadding/REVISION.md) |
| Memory Management | [REVISION.md](./12-Memory%20Management/REVISION.md) |

## 1. Data Structures

Source: [Data-Structures-Quick-Revision.md](./3-Data%20Structures/Data-Structures-Quick-Revision.md)

### Quick glance
- `list`: ordered, mutable, allows duplicates
- `tuple`: ordered, immutable, allows duplicates
- `set`: unordered, mutable, unique values only
- `dict`: key-value mapping, keys must be unique and immutable

### Must-remember points
- Use `list` for sequence processing and updates.
- Use `tuple` for fixed records and unpacking.
- Use `set` for fast membership checks and duplicate removal.
- Use `dict` for mapping, counting, and structured key-value data.

### Frequently revised operations
- Lists: `append()`, `insert()`, `remove()`, `pop()`, slicing, sorting
- Tuples: packing, unpacking, `count()`, `index()`
- Sets: union, intersection, difference, subset, superset
- Dicts: `get()`, `items()`, `keys()`, `values()`, comprehensions, merge

### Interview points
- List vs tuple: mutability
- Set membership is usually faster than list membership
- `d[key]` vs `d.get(key)`
- Shallow copy vs reference copy

## 2. Functions

Source: [Functions-Quick-Revision.md](./4-Functions/Functions-Quick-Revision.md)

### Quick glance
- Functions improve reuse, modularity, and readability.
- `lambda` is useful for small one-line logic.
- `map()` transforms items.
- `filter()` selects items based on a condition.

### Must-remember points
- Functions can use positional arguments, default arguments, `*args`, and `**kwargs`.
- A Python function can return one value, multiple values, or `None`.
- `lambda` supports only a single expression.
- `map()` and `filter()` return lazy iterators in Python 3.

### Common usage patterns
- `def` for reusable or multi-step logic
- `lambda` for short inline operations
- `map()` for element-wise transformation
- `filter()` for condition-based selection

### Interview points
- `def` vs `lambda`
- `map()` vs list comprehension
- `filter()` vs list comprehension
- `*args` vs `**kwargs`

## 3. Importing Modules

Source: [Importing-Modules-Quick-Revision.md](./5-Importing%20Modules/Importing-Modules-Quick-Revision.md)

### Quick glance
- A module is a single `.py` file.
- A package is a folder of related modules.
- Imports help organize and reuse code.

### Common import styles
- `import math`
- `from math import sqrt`
- `import numpy as np`
- Avoid `from module import *` in real projects

### Useful standard library topics
- `math` for numeric operations
- `random` for random values
- `os` for file and directory operations
- `shutil` for higher-level file copying and moving
- `json` for serialization
- `csv` for CSV handling
- `datetime` for dates and times
- `re` for regular expressions

### Interview points
- Module vs package
- Alias imports
- Why wildcard imports are discouraged
- `json.dumps()` vs `json.loads()`

## 4. File Handling

Source: [File-Handling-Quick-Revision.md](./6-File%20Handling/File-Handling-Quick-Revision.md)

### Quick glance
- File handling includes reading, writing, appending, and path management.
- Prefer `with open(...)` so files are closed automatically.

### Must-remember file modes
- `'r'`: read
- `'w'`: write and overwrite
- `'a'`: append
- `'rb'` / `'wb'`: binary read/write

### Common operations
- `read()` for full content
- Loop line-by-line for large files
- `write()` and `writelines()` for output
- Use binary mode for images and raw bytes

### Path utilities
- `os.path.exists()`
- `os.path.isfile()`
- `os.path.isdir()`
- `os.path.abspath()`
- `os.path.join()`

### Interview points
- `'w'` vs `'a'`
- text vs binary mode
- why `with open(...)` is preferred
- `exists()` vs `isfile()`

## 5. Exceptions

Source: [Exceptions-Quick-Revision.md](./7-Exceptions/Exceptions-Quick-Revision.md)

### Quick glance
- Exceptions are runtime errors that interrupt normal program flow.
- Exception handling keeps programs stable and user-friendly.

### Core structure
- `try`: risky code
- `except`: matching error handling
- `else`: runs only if no exception occurs
- `finally`: always runs

### Must-remember points
- Catch specific exceptions before generic `Exception`.
- Use `finally` for cleanup logic.
- Use `with open(...)` to reduce manual cleanup needs.

### Common exceptions
- `ZeroDivisionError`
- `ValueError`
- `NameError`
- `FileNotFoundError`

### Interview points
- `else` vs `finally`
- Why broad `Exception` should be last
- Multiple `except` blocks in one `try`

## 6. Multithreading and Multiprocessing

Source: [REVISION.md](./11-MultiThreadding/REVISION.md)

### Quick glance
- Multithreading is best for I/O-bound tasks.
- Multiprocessing is best for CPU-bound tasks.
- `ThreadPoolExecutor` and `ProcessPoolExecutor` are higher-level APIs.

### Threading summary
- Threads share the same memory space.
- Good for waiting tasks such as API calls, scraping, and file I/O.
- Key methods: `Thread(...)`, `start()`, `join()`

### Multiprocessing summary
- Processes have separate memory spaces.
- Good for computation-heavy tasks.
- Key methods: `Process(...)`, `start()`, `join()`
- On Windows, protect process code with `if __name__ == "__main__":`

### Pool summary
- `ThreadPoolExecutor`: modern thread pool API for I/O-bound work
- `ProcessPoolExecutor`: modern process pool API for CPU-bound work
- `multiprocessing.Pool()`: older multiprocessing-specific pool API

### Interview points
- Threading vs multiprocessing
- ThreadPoolExecutor vs ProcessPoolExecutor
- `multiprocessing.Pool()` vs `ProcessPoolExecutor()`
- GIL effect on CPU-bound threading

## 7. Memory Management

Source: [REVISION.md](./12-Memory%20Management/REVISION.md)

### Quick glance
- Python mainly uses reference counting and garbage collection.
- Reference counting handles immediate cleanup.
- Garbage collection handles unreachable circular references.

### Core ideas
- Variables hold references, not the object data itself.
- `del` removes a reference name, not always the object immediately.
- Circular references may survive until garbage collection runs.

### Important tools
- `sys.getrefcount()` to inspect references
- `gc.enable()` / `gc.disable()` to control garbage collection
- `gc.collect()` to trigger collection manually
- `gc.get_stats()` to inspect GC activity
- `tracemalloc` to profile memory usage

### Memory-efficient practices
- Prefer local variables where appropriate
- Avoid unnecessary circular references
- Use generators for large sequences
- Profile memory when debugging heavy usage

### Interview points
- Reference counting vs garbage collection
- Why circular references need GC
- How generators save memory
- Why `del` does not always destroy an object immediately

## Last-Minute Combined Checklist

- Know when to use `list`, `tuple`, `set`, and `dict`.
- Be comfortable with function parameters, `lambda`, `map()`, and `filter()`.
- Revise import styles and key standard library modules.
- Remember file modes and always prefer `with open(...)`.
- Be clear on `try`, `except`, `else`, and `finally`.
- Use threads for I/O-bound tasks and processes for CPU-bound tasks.
- Remember that Python memory management uses both reference counting and garbage collection.

## Quick Navigation

- [Data Structures](./3-Data%20Structures/Data-Structures-Quick-Revision.md)
- [Functions](./4-Functions/Functions-Quick-Revision.md)
- [Importing Modules](./5-Importing%20Modules/Importing-Modules-Quick-Revision.md)
- [File Handling](./6-File%20Handling/File-Handling-Quick-Revision.md)
- [Exceptions](./7-Exceptions/Exceptions-Quick-Revision.md)
- [Multithreading and Multiprocessing](./11-MultiThreadding/REVISION.md)
- [Memory Management](./12-Memory%20Management/REVISION.md)
