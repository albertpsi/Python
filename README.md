# Python Revision Hub

This README combines the revision notes across the `Python` folder into one quick-glance document.

Use this file when you want:
- a fast revision pass before practice or interviews
- one place to see all major topic summaries
- direct links to the full revision notes for each topic

## Available Revision Files

| Topic | Detailed Revision File |
| --- | --- |
| Python Basics | [Python-Basics-Quick-Revision.md](./1-Python%20Basics/Python-Basics-Quick-Revision.md) |
| Loops and Conditional Statements | [Loops-and-Conditional-Statements-Quick-Revision.md](./2-Loops%20and%20Conditional%20Statements/Loops-and-Conditional-Statements-Quick-Revision.md) |
| Data Structures | [Data-Structures-Quick-Revision.md](./3-Data%20Structures/Data-Structures-Quick-Revision.md) |
| Functions | [Functions-Quick-Revision.md](./4-Functions/Functions-Quick-Revision.md) |
| Importing Modules | [Importing-Modules-Quick-Revision.md](./5-Importing%20Modules/Importing-Modules-Quick-Revision.md) |
| File Handling | [File-Handling-Quick-Revision.md](./6-File%20Handling/File-Handling-Quick-Revision.md) |
| Exceptions | [Exceptions-Quick-Revision.md](./7-Exceptions/Exceptions-Quick-Revision.md) |
| OOPs | [OOPs-Quick-Revision.md](./8-OOPS/OOPs-Quick-Revision.md) |
| Advance Python | [Advance-Python-Quick-Revision.md](./9-Advance%20Python/Advance-Python-Quick-Revision.md) |
| Logging in Python | [Logging-in-Python-Quick-Revision.md](./10-Logging%20in%20python/Logging-in-Python-Quick-Revision.md) |
| Multithreading and Multiprocessing | [REVISION.md](./11-MultiThreadding/REVISION.md) |
| Memory Management | [REVISION.md](./12-Memory%20Management/REVISION.md) |
| Data Analysis | [Data-Analysis-Quick-Revision.md](./13-Data%20Analysis/Data-Analysis-Quick-Revision.md) |

## 1. Python Basics

Source: [Python-Basics-Quick-Revision.md](./1-Python%20Basics/Python-Basics-Quick-Revision.md)

### Quick glance
- Python is case-sensitive and uses indentation to define code blocks.
- Variables are dynamically typed references to values.
- Common data types include `int`, `float`, `str`, and `bool`.
- Core operators include arithmetic, comparison, and logical operators.

### Interview points
- syntax vs semantics
- dynamic typing
- float precision
- `/` vs `//`

## 2. Loops and Conditional Statements

Source: [Loops-and-Conditional-Statements-Quick-Revision.md](./2-Loops%20and%20Conditional%20Statements/Loops-and-Conditional-Statements-Quick-Revision.md)

### Quick glance
- `if`, `elif`, and `else` are used for decision making.
- `for` loops are best for iterables and ranges.
- `while` loops are best when repetition depends on a changing condition.
- `break`, `continue`, and `pass` modify loop flow.

### Interview points
- `for` vs `while`
- `break` vs `continue`
- nested loops
- leap year and prime number logic

## 3. Data Structures

Source: [Data-Structures-Quick-Revision.md](./3-Data%20Structures/Data-Structures-Quick-Revision.md)

### Quick glance
- `list`: ordered, mutable, allows duplicates
- `tuple`: ordered, immutable, allows duplicates
- `set`: unordered, mutable, unique values only
- `dict`: key-value mapping with unique keys

### Interview points
- list vs tuple
- set lookup speed
- `d[key]` vs `d.get(key)`
- shallow copy vs reference copy

## 4. Functions

Source: [Functions-Quick-Revision.md](./4-Functions/Functions-Quick-Revision.md)

### Quick glance
- Functions improve reuse, modularity, and readability.
- `lambda` is useful for small one-line logic.
- `map()` transforms items.
- `filter()` selects items based on a condition.

### Interview points
- `def` vs `lambda`
- `map()` vs list comprehension
- `filter()` vs list comprehension
- `*args` vs `**kwargs`

## 5. Importing Modules

Source: [Importing-Modules-Quick-Revision.md](./5-Importing%20Modules/Importing-Modules-Quick-Revision.md)

### Quick glance
- A module is a single `.py` file.
- A package is a folder of related modules.
- Imports help organize and reuse code.
- Alias imports improve readability in common cases such as `import numpy as np`.

### Interview points
- module vs package
- alias imports
- wildcard imports
- `json.dumps()` vs `json.loads()`

## 6. File Handling

Source: [File-Handling-Quick-Revision.md](./6-File%20Handling/File-Handling-Quick-Revision.md)

### Quick glance
- File handling includes reading, writing, appending, and path management.
- Prefer `with open(...)` so files are closed automatically.
- Remember text and binary modes.
- Path utilities from `os.path` are important in real programs.

### Interview points
- `'w'` vs `'a'`
- text vs binary mode
- why `with open(...)` is preferred
- `exists()` vs `isfile()`

## 7. Exceptions

Source: [Exceptions-Quick-Revision.md](./7-Exceptions/Exceptions-Quick-Revision.md)

### Quick glance
- Exceptions are runtime errors that interrupt normal program flow.
- `try`, `except`, `else`, and `finally` are the main handling blocks.
- Catch specific exceptions before generic `Exception`.
- Use `finally` or context managers for cleanup.

### Interview points
- `else` vs `finally`
- specific vs broad exceptions
- multiple `except` blocks
- cleanup patterns

## 8. OOPs

Source: [OOPs-Quick-Revision.md](./8-OOPS/OOPs-Quick-Revision.md)

### Quick glance
- OOPs is based on classes and objects.
- Core pillars are inheritance, polymorphism, encapsulation, and abstraction.
- Magic methods customize object behavior.
- Operator overloading lets custom objects work with operators like `+`.

### Interview points
- class vs object
- method overriding
- `super()`
- `_name` vs `__name`

## 9. Advance Python

Source: [Advance-Python-Quick-Revision.md](./9-Advance%20Python/Advance-Python-Quick-Revision.md)

### Quick glance
- Iterators return one item at a time using `iter()` and `next()`.
- Generators use `yield` for lazy value generation.
- Decorators add reusable behavior around functions.
- Closures help decorators remember outer-scope values.

### Interview points
- iterable vs iterator
- generator vs list
- `yield`
- closures and decorators

## 10. Logging in Python

Source: [Logging-in-Python-Quick-Revision.md](./10-Logging%20in%20python/Logging-in-Python-Quick-Revision.md)

### Quick glance
- Logging tracks application events, warnings, and errors.
- Standard levels are `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
- `basicConfig()` sets up default logging behavior.
- Handlers can send logs to both console and files.

### Interview points
- logging vs `print()`
- log levels
- handlers
- multiple named loggers

## 11. Multithreading and Multiprocessing

Source: [REVISION.md](./11-MultiThreadding/REVISION.md)

### Quick glance
- Multithreading is best for I/O-bound tasks.
- Multiprocessing is best for CPU-bound tasks.
- `ThreadPoolExecutor` and `ProcessPoolExecutor` are higher-level APIs.
- On Windows, process code should be protected by `if __name__ == "__main__":`.

### Interview points
- threading vs multiprocessing
- thread pools vs process pools
- GIL impact
- process startup safety on Windows

## 12. Memory Management

Source: [REVISION.md](./12-Memory%20Management/REVISION.md)

### Quick glance
- Python mainly uses reference counting and garbage collection.
- Circular references need garbage collection.
- `del` removes a reference name, not always the object immediately.
- `tracemalloc` helps profile memory usage.

### Interview points
- reference counting vs garbage collection
- circular references
- generators and memory efficiency
- `del` behavior

## 13. Data Analysis

Source: [Data-Analysis-Quick-Revision.md](./13-Data%20Analysis/Data-Analysis-Quick-Revision.md)

### Quick glance
- NumPy provides fast arrays and vectorized numerical operations.
- Important array concepts are `shape`, `ndim`, and `reshape()`.
- Boolean masking helps filter data efficiently.
- Statistical helpers like `mean`, `median`, and `std` are common in analysis work.

### Interview points
- NumPy vs Python lists
- vectorization
- indexing and slicing
- boolean masking

## Last-Minute Combined Checklist

- Revise Python syntax, variables, data types, and operators.
- Practice conditional logic, loops, and loop-control statements.
- Know when to use `list`, `tuple`, `set`, and `dict`.
- Be comfortable with function parameters, `lambda`, `map()`, and `filter()`.
- Revise import styles and key standard library modules.
- Remember file modes and always prefer `with open(...)`.
- Be clear on `try`, `except`, `else`, and `finally`.
- Review OOPs pillars, magic methods, and operator overloading.
- Practice iterators, generators, and decorators.
- Remember logging levels, handlers, and named loggers.
- Use threads for I/O-bound tasks and processes for CPU-bound tasks.
- Remember that Python memory management uses both reference counting and garbage collection.
- Revise NumPy array creation, reshaping, vectorization, and masking.

## Quick Navigation

- [Python Basics](./1-Python%20Basics/Python-Basics-Quick-Revision.md)
- [Loops and Conditional Statements](./2-Loops%20and%20Conditional%20Statements/Loops-and-Conditional-Statements-Quick-Revision.md)
- [Data Structures](./3-Data%20Structures/Data-Structures-Quick-Revision.md)
- [Functions](./4-Functions/Functions-Quick-Revision.md)
- [Importing Modules](./5-Importing%20Modules/Importing-Modules-Quick-Revision.md)
- [File Handling](./6-File%20Handling/File-Handling-Quick-Revision.md)
- [Exceptions](./7-Exceptions/Exceptions-Quick-Revision.md)
- [OOPs](./8-OOPS/OOPs-Quick-Revision.md)
- [Advance Python](./9-Advance%20Python/Advance-Python-Quick-Revision.md)
- [Logging in Python](./10-Logging%20in%20python/Logging-in-Python-Quick-Revision.md)
- [Multithreading and Multiprocessing](./11-MultiThreadding/REVISION.md)
- [Memory Management](./12-Memory%20Management/REVISION.md)
- [Data Analysis](./13-Data%20Analysis/Data-Analysis-Quick-Revision.md)
