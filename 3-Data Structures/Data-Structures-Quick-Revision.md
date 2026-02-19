# Python Data Structures Quick Revision

Based on:

- `3.1-List.ipynb`
- `3.2-Tuples.ipynb`
- `3.3-Sets.ipynb`
- `3.4-Dictionaries.ipynb`

## 1. Lists (`list`)

### Core idea

- Ordered, mutable, allows duplicates.
- Can store mixed types (possible, but avoid in clean production data).

### Key points for revision

- Creation: `[]`, `list()`
- Indexing: `lst[0]`, negative indexing: `lst[-1]`
- Slicing: `lst[start:stop:step]`
- Mutating methods:
  - `append(x)`: add at end
  - `insert(i, x)`: add at index
  - `remove(x)`: remove first matching value
  - `pop([i])`: remove and return by index (default last)
  - `clear()`: remove all items
- Useful operations: `len(lst)`, `x in lst`, `lst.count(x)`, `lst.index(x)`
- Sorting:
  - `lst.sort()`: in-place
  - `sorted(lst)`: returns new list
- Reversing:
  - `lst.reverse()` (in-place)
  - `lst[::-1]` (new reversed copy)

### List comprehension patterns

```python
# basic
squares = [x * x for x in range(6)]

# with condition
evens = [x for x in range(10) if x % 2 == 0]

# nested
pairs = [(i, j) for i in [1, 2] for j in ['a', 'b']]
```

---

## 2. Tuples (`tuple`)

### Core idea

- Ordered, immutable, allows duplicates.
- Good for fixed records and function returns.

### Key points for revision

- Creation: `()`, `tuple()`
- Single item tuple needs comma: `(10,)`
- Access: indexing and slicing same as list
- Supports concatenation and repetition: `t1 + t2`, `t * 3`
- Methods:
  - `count(x)`
  - `index(x)`
- Packing/unpacking:

```python
person = ("Alice", 30)
name, age = person

nums = (1, 2, 3, 4, 5)
first, *middle, last = nums
```

### Interview note

- List is mutable; tuple is immutable.
- Tuples are hashable only if all elements are hashable.

---

## 3. Sets (`set`)

### Core idea

- Unordered collection of unique elements.
- Best for fast membership checks and set algebra.

### Key points for revision

- Creation: `{1, 2, 3}`, empty set: `set()`
- Duplicates automatically removed.
- Add/remove:
  - `add(x)`
  - `remove(x)` -> raises `KeyError` if missing
  - `discard(x)` -> no error if missing
  - `pop()` -> removes an arbitrary element
  - `clear()`
- Membership: `x in s`, `x not in s`
- Set operations:
  - Union: `a | b` or `a.union(b)`
  - Intersection: `a & b` or `a.intersection(b)`
  - Difference: `a - b` or `a.difference(b)`
  - Symmetric difference: `a ^ b`
- Relationship checks:
  - `a.issubset(b)`
  - `a.issuperset(b)`

### Interview note

- Average membership complexity in set is `O(1)`, list is `O(n)`.

---

## 4. Dictionaries (`dict`)

### Core idea

- Key-value mapping.
- Keys must be unique and immutable; values can be any type.

### Key points for revision

- Creation: `{}`, `dict()`
- Access:
  - `d[key]` -> raises `KeyError` if missing
  - `d.get(key, default)` -> safe access
- Update/add: `d[key] = value`
- Delete:
  - `del d[key]`
  - `d.pop(key[, default])`
- Views:
  - `d.keys()`
  - `d.values()`
  - `d.items()`
- Iteration:

```python
for k, v in d.items():
    print(k, v)
```

- Comprehensions:

```python
squares = {x: x * x for x in range(5)}
evens = {x: x * x for x in range(10) if x % 2 == 0}
```

- Merge dictionaries:

```python
merged = {**d1, **d2}  # d2 overrides duplicate keys
```

### Copy behavior (important)

- `copy_ref = d` -> same object (alias/reference).
- `copy_obj = d.copy()` -> new outer dict (shallow copy).

---

## Quick Comparison Table

| Type  | Ordered                            | Mutable | Duplicates            | Access Pattern | Typical Use                     |
| ----- | ---------------------------------- | ------- | --------------------- | -------------- | ------------------------------- |
| List  | Yes                                | Yes     | Yes                   | Index          | Sequence processing             |
| Tuple | Yes                                | No      | Yes                   | Index          | Fixed records, function returns |
| Set   | No                                 | Yes     | No                    | Membership     | Deduplication, fast lookup      |
| Dict  | Yes (insertion order, Python 3.7+) | Yes     | Keys: No, Values: Yes | Key            | Mapping/config/counting         |

---

## Frequently Asked Interview Questions (Short Answers)

1. **List vs Tuple?**

- List is mutable and usually heavier.
- Tuple is immutable and suitable for fixed, read-only records.

2. **`append()` vs `extend()` in list?**

- `append(x)` adds one element.
- `extend(iterable)` adds each element from iterable.

3. **`remove()` vs `pop()` in list?**

- `remove(x)` removes first matching value.
- `pop(i)` removes by index and returns removed value.

4. **Why use set for membership tests?**

- Average `O(1)` lookup due to hashing.

5. **`remove()` vs `discard()` in set?**

- `remove` throws error if item absent.
- `discard` does nothing if item absent.

6. **Can a list be a dictionary key?**

- No, list is mutable and unhashable.
- Tuple can be a key if all its elements are hashable.

7. **`d[key]` vs `d.get(key)`?**

- `d[key]` raises `KeyError` if missing.
- `d.get(key)` safely returns `None` or default.

8. **What is shallow copy in dict/list?**

- Outer object copied, nested objects still shared.

9. **How to remove duplicates while preserving order?**

- `list(dict.fromkeys(nums))`

10. **Difference between set and dict?**

- Set stores only unique values.
- Dict stores key-value pairs.

---

## Interview Coding Questions with Answers

### 1) Remove duplicates from a list while preserving order

```python
nums = [3, 1, 3, 2, 1, 5]
result = list(dict.fromkeys(nums))
print(result)  # [3, 1, 2, 5]
```

### 2) Count frequency of elements in a list (manual way)

```python
nums = [1, 2, 2, 3, 3, 3]
freq = {}
for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1
print(freq)  # {1: 1, 2: 2, 3: 3}
```

### 3) Find common elements between two lists

```python
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = list(set(a) & set(b))
print(common)  # [3, 4] (order may vary)
```

### 4) Split list into train/test (80/20)

```python
data = list(range(20))
split = int(0.8 * len(data))
train, test = data[:split], data[split:]
print(len(train), len(test))  # 16 4
```

### 5) Invert a dictionary (unique values case)

```python
d = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in d.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

### 6) Merge two dictionaries with key conflict handling

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
merged = {**d1, **d2}
print(merged)  # {'a': 1, 'b': 99, 'c': 3}
```

### 7) Safe access in dictionary

```python
student = {"name": "Sai", "age": 21}
print(student.get("grade", "Not Available"))
# Not Available
```

### 8) Demonstrate tuple immutability

```python
t = (1, 2, 3)
# t[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Correct approach: create new tuple
t = (10,) + t[1:]
print(t)  # (10, 2, 3)
```

---

## Last-Minute Revision Checklist

- Know when to use each structure (`list`, `tuple`, `set`, `dict`).
- Practice list/dict comprehensions.
- Be clear on mutability and copy behavior (`=`, `.copy()`, deep copy concept).
- Memorize set operations and dictionary safe-access patterns.
- Be ready to write frequency-count and deduplication code quickly.
