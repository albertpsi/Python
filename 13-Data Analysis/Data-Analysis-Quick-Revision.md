# Data Analysis Quick Revision

Based on:

- `13.1-numpy.ipynb`

## 1. NumPy Basics

### Core idea

- NumPy is the core library for numerical computing in Python.
- Its main object is the `ndarray`, which supports fast vectorized operations.

### `numpy.array()` vs `array.array()`

- `numpy.array()` supports multi-dimensional arrays and powerful numerical operations.
- `array.array()` is a simpler standard-library typed container, mostly for basic one-dimensional storage.

---

## 2. Creating Arrays

### Common functions

- `np.array([...])`
- `np.arange(start, stop, step)`
- `np.ones((rows, cols))`
- `np.zeros((rows, cols))`
- `np.eye(n)`

### Example

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3], [4, 5, 6]])
```

---

## 3. Shape, Dimension, and Reshaping

### Key points for revision

- `arr.shape` gives the array dimensions.
- `arr.ndim` gives the number of axes.
- `arr.reshape(r, c)` changes the structure when the total size matches.

### Interview note

- A 1D array and a 2D array with one column are not the same thing.

---

## 4. Indexing and Slicing

### Core idea

- NumPy supports fast indexing and slicing for one-dimensional and multi-dimensional arrays.

### Common patterns

- `arr[0]`
- `arr[1:4]`
- `matrix[0, 1]`
- `matrix[:, 2]`

---

## 5. Vectorized Operations and Universal Functions

### Core idea

- NumPy performs element-wise operations without explicit Python loops.

### Common examples

- `arr1 + arr2`
- `arr * 2`
- `np.sqrt(arr)`
- `np.exp(arr)`

### Why it matters

- Vectorized operations are shorter, faster, and easier to read than manual loops for numerical work.

---

## 6. Statistics and Scaling Basics

### Common operations

- `np.mean(data)`
- `np.median(data)`
- `np.std(data)`
- Normalization and standardization concepts

### Key point

- These operations are very common in data preprocessing and analysis.

---

## 7. Boolean Masking and Logical Operations

### Core idea

- Boolean masks filter array values based on conditions.

### Example

```python
data = np.array([1, 2, 3, 4, 5, 6])
mask = data >= 4
print(data[mask])  # [4 5 6]
```

### Logical operators

- `(data >= 5) & (data <= 8)`
- `(data < 3) | (data > 7)`

---

## Frequently Asked Interview Questions (Short Answers)

1. **Why use NumPy instead of plain Python lists for numerical work?**

- NumPy is faster, supports vectorized operations, and handles multi-dimensional arrays well.

2. **What does `shape` tell you?**

- The size of the array along each axis.

3. **What is vectorization?**

- Performing operations on whole arrays at once instead of looping element by element in Python.

4. **What is the use of `reshape()`?**

- It changes the arrangement of data without changing the actual values.

5. **What is boolean masking?**

- Filtering array elements using a condition that returns `True` or `False`.

---

## Last-Minute Revision Checklist

- Memorize basic array-creation functions.
- Revise `shape`, `ndim`, and `reshape()`.
- Practice indexing and slicing on 2D arrays.
- Remember vectorized operations and common universal functions.
- Be comfortable with `mean`, `median`, `std`, and boolean masking.
