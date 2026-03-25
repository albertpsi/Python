# Loops and Conditional Statements Quick Revision

Based on:

- `2.1-Conditional Statements.ipynb`
- `2.2-Loops.ipynb`

## 1. Conditional Statements

### Core idea

- Conditional statements control which block of code runs based on a condition.

### Main forms

- `if`: run code when a condition is true
- `elif`: check another condition if earlier ones fail
- `else`: run fallback code when all previous conditions fail

### Key points for revision

- Conditions should evaluate to `True` or `False`.
- Each block must be indented correctly.
- Nested conditionals are allowed.
- Use comparison and logical operators inside conditions.

### Example

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 2. `for` Loops

### Core idea

- A `for` loop iterates over items in a sequence or iterable.

### Common patterns

- Loop through `range()`
- Loop through strings
- Loop through lists, tuples, sets, and dictionaries

### `range()` forms

- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`

### Example

```python
for i in range(5):
    print(i)
```

---

## 3. `while` Loops

### Core idea

- A `while` loop runs as long as its condition remains true.

### Key points for revision

- Initialize the loop variable before the loop if needed.
- Update the loop variable inside the loop to avoid infinite loops.
- `while` is useful when the number of iterations is not known in advance.

### Example

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## 4. Loop Control Statements

### `break`

- Exits the loop immediately.

### `continue`

- Skips the rest of the current iteration and moves to the next one.

### `pass`

- Does nothing and acts as a placeholder.

### Example

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 5. Nested Loops

### Core idea

- A nested loop is a loop inside another loop.
- The inner loop runs fully for each iteration of the outer loop.

### Use cases

- Pattern printing
- Matrix traversal
- Pair combinations

---

## 6. Practice Patterns from This Section

### Frequently used examples

- Age check with `if` / `elif` / `else`
- Leap year checker
- Sum of natural numbers
- Prime number checker

### Interview note

- Prime checks are commonly optimized by reducing unnecessary iterations.

---

## Quick Comparison Table

| Topic | Best use |
| --- | --- |
| `if` / `elif` / `else` | Decision making |
| `for` loop | Fixed or iterable-based repetition |
| `while` loop | Condition-based repetition |
| `break` | Exit loop early |
| `continue` | Skip one iteration |
| `pass` | Placeholder for future code |

---

## Frequently Asked Interview Questions (Short Answers)

1. **When should you use `for` instead of `while`?**

- Use `for` when iterating over a known iterable or range.

2. **When is `while` a better choice?**

- When the loop should continue until a condition changes and the count is not fixed.

3. **What is the difference between `break` and `continue`?**

- `break` stops the loop; `continue` skips the current iteration.

4. **What does `pass` do?**

- Nothing. It is used as a syntactic placeholder.

5. **Why are indentation errors common in conditional logic?**

- Because Python uses indentation to decide which statements belong to each block.

---

## Last-Minute Revision Checklist

- Revise the structure of `if`, `elif`, and `else`.
- Memorize the three common `range()` forms.
- Remember to update variables in `while` loops.
- Practice `break`, `continue`, and `pass`.
- Be ready to write leap year, sum, and prime-check programs.
