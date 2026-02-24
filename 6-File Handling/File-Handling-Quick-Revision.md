# Python File Handling Quick Revision

Based on:

- `6.1-File Operation.ipynb`
- `6.2-filePath.ipynb`

## 1. File Open Modes

### Core idea

- File handling = reading, writing, appending, and managing file paths safely.
- Prefer `with open(...)` so files auto-close even if errors happen.

### Important modes

- `'r'`: read (file must exist)
- `'w'`: write (creates/overwrites)
- `'a'`: append (creates if missing)
- `'w+'`: write + read (overwrites first)
- `'rb'` / `'wb'`: binary read/write

---

## 2. Reading Text Files

```python
with open('example.txt', 'r') as file:
    content = file.read()
```

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

### Key points

- `read()` gets full content.
- Looping line-by-line is memory friendly for large files.
- `strip()` removes trailing newline/spaces.

---

## 3. Writing and Appending

```python
with open('example.txt', 'w') as file:
    file.write('First line\n')
```

```python
with open('example.txt', 'a') as file:
    file.writelines(['Second\n', 'Third\n'])
```

### Key points

- `'w'` replaces old content.
- `'a'` keeps old content and adds at end.
- `writelines()` does not add `\n` automatically; include it yourself.

---

## 4. Binary File Handling

```python
with open('example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02')

with open('example.bin', 'rb') as file:
    data = file.read()
```

- Use binary modes for images, audio, serialized data, etc.

---

## 5. Copying File Content

```python
with open('example.txt', 'r') as src:
    content = src.read()

with open('destination.txt', 'w') as dst:
    dst.write(content)
```

- Simple text copy pattern from source to destination.

---

## 6. File Paths with `os`

```python
import os
os.getcwd()
os.listdir('.')
os.path.exists('example.txt')
os.path.isfile('example.txt')
os.path.isdir('new_folder')
os.path.abspath('example.txt')
os.path.join(os.getcwd(), 'new_folder', 'example.txt')
```

### Directory creation

```python
os.mkdir('new_folder')
os.makedirs('new_folder', exist_ok=True)
```

- `makedirs(..., exist_ok=True)` avoids error if folder already exists.

---

## Quick Comparison Table

| Task | Method |
| ---- | ------ |
| Read full file | `file.read()` |
| Read line-by-line | `for line in file` |
| Overwrite file | mode `'w'` |
| Append content | mode `'a'` |
| Binary write/read | `'wb'` / `'rb'` |
| Join paths safely | `os.path.join(...)` |

---

## Frequently Asked Interview Questions (Short Answers)

1. **Why use `with open(...)`?**

- It closes files automatically and safely.

2. **Difference between `'w'` and `'a'`?**

- `'w'` overwrites, `'a'` appends.

3. **When use binary mode?**

- For non-text data like images or raw bytes.

4. **`os.path.exists()` vs `os.path.isfile()`?**

- `exists` checks any path; `isfile` confirms regular file.

5. **Why use `os.path.join()`?**

- Cross-platform-safe path construction.

---

## Last-Minute Revision Checklist

- Remember file modes and their effects.
- Use `with` for all file operations.
- Know text vs binary handling.
- Practice source-to-destination copy code.
- Revise `os` path utilities: `exists`, `isfile`, `isdir`, `abspath`, `join`.
