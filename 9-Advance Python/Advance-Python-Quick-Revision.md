# Advance Python Quick Revision

Based on:

- `9.1-Iterators.ipynb`
- `9.2-Generators.ipynb`
- `9.3-Decorators.ipynb`

## 1. Iterators

### Core idea

- An iterator is an object that returns one item at a time.

### Key points for revision

- Use `iter(obj)` to create an iterator from an iterable.
- Use `next(iterator)` to get the next value.
- When values are exhausted, Python raises `StopIteration`.
- Lists, tuples, sets, strings, and dictionaries are iterable.

### Example

```python
nums = [1, 2, 3]
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
```

---

## 2. Generators

### Core idea

- A generator is an easy way to build an iterator using `yield`.

### Key points for revision

- Generators produce values lazily, one at a time.
- They are memory-efficient for large data.
- Generator functions pause at `yield` and resume on the next `next()` call.
- They are useful for streaming file data or large sequences.

### Example

```python
def square(n):
    for i in range(n):
        yield i * i
```

### Real use case

- Reading a large file line by line without loading it fully into memory

---

## 3. Decorators

### Core idea

- A decorator is a function that takes another function, adds behavior, and returns a new function.

### Concepts behind decorators

- Functions are first-class objects in Python.
- Closures let an inner function remember variables from the outer function.
- Decorators are built on top of functions and closures.

### Example

```python
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
```

### Common use cases

- Logging
- Timing
- Authentication checks
- Input validation

---

## Iterator vs Generator

| Topic | Iterator | Generator |
| --- | --- | --- |
| Creation | `iter()` or custom iterator class | Function with `yield` |
| State handling | Managed manually | Managed automatically by Python |
| Memory use | Efficient | Very efficient |
| Best use | General iteration protocol | Lazy sequence generation |

---

## Frequently Asked Interview Questions (Short Answers)

1. **What is the difference between iterable and iterator?**

- An iterable can produce an iterator. An iterator is the object that yields items one by one.

2. **What does `next()` do?**

- It returns the next item from an iterator.

3. **Why are generators memory-efficient?**

- They create values on demand instead of storing the whole sequence at once.

4. **What is a closure?**

- A nested function that remembers variables from its enclosing scope.

5. **What is the main purpose of a decorator?**

- To add reusable behavior around an existing function without changing its core logic.

---

## Last-Minute Revision Checklist

- Revise `iter()` and `next()`.
- Remember that exhausted iterators raise `StopIteration`.
- Practice writing generator functions with `yield`.
- Understand why generators help with large files and big datasets.
- Be clear on functions, closures, and decorators.
