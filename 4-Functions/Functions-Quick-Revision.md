# Python Functions Quick Revision

Based on:

- `4.1-Functions.ipynb`
- `4.2-Lambda Function.ipynb`
- `4.3-Map Functions.ipynb`
- `4.4-Filter Function.ipynb`

## 1. Functions (`def`)

### Core idea

- A function is a reusable block of code for a specific task.
- It improves readability, modularity, and reuse.

### Syntax

```python
def function_name(parameters):
    """Optional docstring"""
    # function body
    return value  # optional
```

### Key points for revision

- Function call executes function: `function_name(args)`.
- Parameters can be:
  - Positional
  - Default values (`name="Guest"`)
  - Variable-length positional (`*args`)
  - Variable-length keyword (`**kwargs`)
- Rule: positional arguments must come before keyword arguments in a call.
- A function can return:
  - Single value
  - Multiple values (as tuple)
  - Nothing (`None` implicitly)

### Practical patterns

```python
# even/odd check

def is_even(num):
    return num % 2 == 0

# default parameter

def greet(name="Guest"):
    print(f"Hello {name}")

# variable-length args

def multiply(*args):
    result = 1
    for n in args:
        result *= n
    return result, len(args)
```

### Real-world examples from notebook

- Temperature conversion function with unit validation.
- Password strength checker based on length.
- Shopping cart total using `**kwargs` and type-checking.
- Palindrome checker using cleanup + reverse slicing.
- Word frequency counter from file (example used `sample.txt`).

---

## 2. Lambda Functions (`lambda`)

### Core idea

- Small anonymous function used for short one-line logic.
- Can take many inputs but only one expression.

### Syntax

```python
lambda arguments: expression
```

### Key points for revision

- `lambda` creates a function object.
- Best for short throwaway logic (especially with `map()` / `filter()`).
- For complex multi-step logic, prefer normal `def`.

### Examples

```python
add = lambda x, y: x + y
even = lambda num: num % 2 == 0
```

### C# vs Python quick note

- C#: `(x) => x + 1`
- Python: `lambda x: x + 1`
- Python lambda is expression-only (no statement blocks).

---

## 3. `map()` Function

### Core idea

- Applies a function to every item of iterable(s).
- Returns a `map` object (iterator), often converted to list.

### Syntax

```python
map(function, iterable1, iterable2, ...)
```

### Key points for revision

- `map()` is for transformation (input list -> transformed list).
- Use `list(map(...))` to see full output quickly.
- Works with named functions and lambdas.
- With multiple iterables, function must accept matching number of args.

### Common patterns

```python
# using def

def square(num):
    return num * num

list(map(square, [1, 2, 3, 4]))

# using lambda
numbers = [1, 2, 3, 4, 5]
list(map(lambda x: x * x, numbers))

# multiple iterables
n1 = [1, 2, 3]
n2 = [4, 5, 6]
list(map(lambda x, y: x + y, n1, n2))

# type conversion
str_num = ['1', '2', '3']
list(map(int, str_num))
```

### Interview note

- `map()` transforms each element.
- If your function is not element-wise (e.g., expects scalar but got list), call will fail.

---

## 4. `filter()` Function

### Core idea

- Selects only elements where condition is `True`.
- Returns a `filter` object (iterator).

### Syntax

```python
filter(function, iterable)
```

### Key points for revision

- `function` should return boolean (`True`/`False`).
- Keep elements that satisfy condition; drop others.
- Usually consumed as `list(filter(...))`.
- `filter()` accepts one iterable.

### Common patterns

```python
# named function

def even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
list(filter(even, numbers))

# lambda
list(filter(lambda x: x > 5 and x % 2 == 0, [1,2,3,4,5,6,7,8,9,10]))

# filtering list of dicts
people = [
    {'name': 'Krish', 'age': 32},
    {'name': 'Sai', 'age': 24},
    {'name': 'Rahul', 'age': 27}
]
list(filter(lambda p: p['age'] > 25, people))
```

### Common pitfall

- `filter(lambda x, y: ..., a, b)` is invalid.
- For multiple iterables, use `map()`/`zip()` patterns instead.

---

## Quick Comparison Table

| Topic    | Purpose                | Output Type | Best Use Case                         |
| -------- | ---------------------- | ----------- | ------------------------------------- |
| `def`    | Define reusable logic  | Function    | Complex or reusable operations        |
| `lambda` | One-line anonymous fn  | Function    | Short inline logic                    |
| `map()`  | Transform each element | Iterator    | Apply same transformation to iterable |
| `filter()` | Keep matching items  | Iterator    | Condition-based selection             |

---

## Frequently Asked Interview Questions (Short Answers)

1. **`def` vs `lambda`?**

- `def` is named and supports multi-line logic.
- `lambda` is anonymous and expression-only.

2. **Can lambda have multiple statements?**

- No, only one expression.

3. **What does `map()` return in Python 3?**

- A lazy iterator (`map` object).

4. **What does `filter()` return in Python 3?**

- A lazy iterator (`filter` object).

5. **`map()` vs list comprehension?**

- Both transform data.
- List comprehension is often more readable for simple logic.

6. **`filter()` vs list comprehension?**

- Both filter data.
- List comprehension can be clearer for combined conditions.

7. **What are `*args` and `**kwargs`?**

- `*args`: variable positional args as tuple.
- `**kwargs`: variable keyword args as dict.

8. **Can function return multiple values?**

- Yes, Python returns them as a tuple.

9. **What is default argument in function?**

- Parameter value used when caller does not pass that argument.

10. **Can `filter()` take multiple iterables?**

- No, it takes one iterable.

---

## Interview Coding Questions with Answers

### 1) Check if number is even

```python
def is_even(num):
    return num % 2 == 0

print(is_even(24))  # True
```

### 2) Add two numbers using lambda

```python
add = lambda x, y: x + y
print(add(5, 3))  # 8
```

### 3) Square a list using `map()`

```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print(squares)  # [1, 4, 9, 16]
```

### 4) Convert list of numeric strings to ints

```python
str_num = ['1', '2', '3', '4']
nums = list(map(int, str_num))
print(nums)  # [1, 2, 3, 4]
```

### 5) Filter even numbers

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6, 8]
```

### 6) Filter numbers greater than 5

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(filter(lambda x: x > 5, nums))
print(result)  # [6, 7, 8, 9]
```

### 7) Multiply variable number of inputs

```python
def multiply(*args):
    result = 1
    for n in args:
        result *= n
    return result

print(multiply(2, 3, 4))  # 24
```

### 8) Compute total cost with `**kwargs`

```python
def calculate_total_cost(**kwargs):
    total = 0
    for item, price in kwargs.items():
        if isinstance(price, (int, float)):
            total += price
    return total

print(calculate_total_cost(apple=1.5, bread=2.0, milk=3.0))  # 6.5
```

---

## Last-Minute Revision Checklist

- Know function syntax, calls, and return behavior.
- Be clear on default args, `*args`, and `**kwargs`.
- Know when to use `def` vs `lambda`.
- Remember `map()` transforms, `filter()` selects.
- Convert iterators to list when you need immediate output.
- Practice 5-10 quick examples with lambda + map/filter.
