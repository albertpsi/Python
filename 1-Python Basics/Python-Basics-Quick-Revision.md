# Python Basics Quick Revision

Based on:

- `1.0-Basics.ipynb`
- `1.1-Variables.ipynb`
- `1.2-Datatypes.ipynb`
- `1.3-operators.ipynb`

## 1. Syntax and Semantics

### Core idea

- Syntax means the rules for writing valid Python code.
- Semantics means what the code actually does when it runs.

### Key points for revision

- Python is case-sensitive: `name` and `Name` are different identifiers.
- Indentation defines code blocks in Python.
- Statements like `if`, `for`, `while`, `def`, and `class` end with `:`.
- Use brackets or `\` for line continuation when a statement is long.
- Triple quotes allow multi-line strings.

### Common mistakes

- Missing indentation after `if`, `for`, `while`, or `def`
- Forgetting `:` after a block header
- Assuming Python ignores uppercase/lowercase differences

---

## 2. Variables

### Core idea

- Variables store references to values.
- Python is dynamically typed, so you do not declare the type explicitly.

### Key points for revision

- Valid names start with a letter or `_`.
- Variable names can contain letters, digits, and underscores.
- Invalid names include spaces, hyphens, and names starting with digits.
- Reassignment is allowed, and the type can change at runtime.

### Example

```python
age = 26
name = "Sai"
is_student = False
```

### Interview note

- Variables hold references to objects, not raw memory values in the low-level sense.

---

## 3. Data Types

### Core idea

- Data types define the kind of value a variable stores and what operations are valid on it.

### Common built-in types

- `int`: whole numbers
- `float`: decimal numbers
- `str`: text
- `bool`: `True` or `False`

### Key points for revision

- Use `type(obj)` to inspect a value's type.
- Type conversion is explicit in many cases: `int()`, `float()`, `str()`, `bool()`.
- Mixing incompatible types can raise errors such as `TypeError`.
- Floating-point numbers can show precision limitations.

### Example

```python
result = "20" + str(10)  # "2010"
```

### Interview note

- Python `float` values are binary floating-point numbers, so some decimal values are approximated internally.

---

## 4. Operators

### Main categories

- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `and`, `or`, `not`

### Key points for revision

- `/` returns true division.
- `//` returns floor division.
- `%` returns the remainder.
- `**` is exponentiation.
- Comparison operators return boolean results.
- Logical operators combine or invert boolean expressions.

### Example

```python
a = 7
b = 3

print(a / b)   # 2.333...
print(a // b)  # 2
print(a % b)   # 1
```

---

## Quick Comparison Table

| Topic | What to remember |
| --- | --- |
| Syntax | Correct structure, indentation, and punctuation |
| Semantics | Meaning and behavior of the code |
| Variables | Named references to values |
| Data types | Define valid operations on values |
| Operators | Perform arithmetic, comparison, and boolean logic |

---

## Frequently Asked Interview Questions (Short Answers)

1. **Why is indentation important in Python?**

- It defines blocks of code instead of curly braces.

2. **Is Python case-sensitive?**

- Yes. `total` and `Total` are different names.

3. **What is dynamic typing?**

- The variable type is decided at runtime and can change after reassignment.

4. **What is the difference between `/` and `//`?**

- `/` gives normal division, `//` gives floor division.

5. **Why does Python show extra digits in some float values?**

- Because floats are stored in binary and many decimal numbers cannot be represented exactly.

---

## Last-Minute Revision Checklist

- Remember that Python is case-sensitive.
- Revise indentation and `:` after block statements.
- Practice valid variable naming rules.
- Know the common built-in types and explicit type conversion.
- Be clear on `/`, `//`, `%`, and `**`.
