# Python Exceptions Quick Revision

Based on:

- `7.1-Exceptions.ipynb`

## 1. What Is an Exception?

### Core idea

- An exception is a runtime error that interrupts normal program flow.
- Exception handling prevents program crashes and gives controlled fallback behavior.

### Common exceptions in this notebook

- `ZeroDivisionError`
- `NameError`
- `ValueError`
- `FileNotFoundError`
- Generic `Exception`

---

## 2. `try` and `except`

### Basic pattern

```python
try:
    risky_code()
except SpecificError as ex:
    print(ex)
```

### Key points

- Put risky code in `try`.
- Catch specific exceptions first.
- Use `as ex` to inspect message/object.
- Multiple `except` blocks can be used.

---

## 3. Multiple Exceptions + Fallback

```python
try:
    num = int(input('Enter a number: '))
    result = 10 / num
except ValueError:
    print('Invalid integer input')
except ZeroDivisionError:
    print('Cannot divide by zero')
except Exception as ex:
    print('An error occurred:', ex)
```

- `Exception` is a broad catch; keep it last.

---

## 4. `else` and `finally`

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print('Error')
else:
    print('Result:', result)
finally:
    print('Execution completed')
```

### Behavior

- `else`: runs only if no exception in `try`.
- `finally`: always runs (cleanup logic).

---

## 5. File Handling with Exceptions

```python
try:
    file = open('example.txt', 'r')
    content = file.read()
except FileNotFoundError as ex:
    print('File not found:', ex)
except Exception as ex:
    print('File handling error:', ex)
finally:
    try:
        file.close()
    except Exception:
        pass
```

### Key points

- Handle `FileNotFoundError` separately for clearer error messages.
- Always close file (or use `with open(...)` to avoid manual close).

---

## Quick Comparison Table

| Block | Runs When |
| ----- | --------- |
| `try` | Always (main risky code) |
| `except` | Only if matching exception occurs |
| `else` | Only when no exception occurs |
| `finally` | Always, with or without exception |

---

## Frequently Asked Interview Questions (Short Answers)

1. **Why use exception handling?**

- To keep program stable and provide user-friendly error behavior.

2. **Why should broad `Exception` be last?**

- Otherwise it can swallow specific exceptions first.

3. **Difference between `else` and `finally`?**

- `else` only on success; `finally` always.

4. **Can one `try` have multiple `except` blocks?**

- Yes, and that is common.

5. **Best way to avoid file-close issues?**

- Use `with open(...)` context manager.

---

## Last-Minute Revision Checklist

- Memorize `try-except-else-finally` flow.
- Catch specific exceptions before generic `Exception`.
- Use meaningful messages for user input errors (`ValueError`, `ZeroDivisionError`).
- Handle missing files with `FileNotFoundError`.
- Prefer context managers (`with`) for file operations.
