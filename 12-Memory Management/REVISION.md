# Revision Notes: Memory Management

## 12.1 Python Memory Management

### What memory management means
- Memory management is the process of allocating, using, and freeing memory while a program runs.
- Python handles most memory management automatically.
- The main mechanisms are reference counting and garbage collection.

## Reference Counting

### What it is
- Every Python object keeps track of how many references point to it.
- When the reference count becomes zero, the object can be destroyed immediately.

### Important idea
- Variables do not store the object itself.
- Variables store references to objects.

### Example flow
```python
import sys

a = []
print(sys.getrefcount(a))

b = a
print(sys.getrefcount(a))

del b
print(sys.getrefcount(a))
```

### Key point
- `sys.getrefcount(obj)` usually shows one extra reference because the object is also passed into the function call itself.

## Garbage Collection

### Why Python needs it
- Reference counting alone cannot clean up circular references.
- Circular references happen when objects point to each other.

### Example
```python
obj1.ref = obj2
obj2.ref = obj1
```

### What the garbage collector does
- Python has a cyclic garbage collector to detect and remove unreachable reference cycles.
- The `gc` module gives control over this behavior.

### Useful functions
- `gc.enable()` enables garbage collection.
- `gc.disable()` disables garbage collection.
- `gc.collect()` manually runs garbage collection.
- `gc.get_stats()` shows garbage collection statistics.

## Circular References

### What they are
- A circular reference exists when two or more objects reference each other.
- Even if you delete the variable names, the objects may still remain alive because they still reference one another.

### Important idea
- `del obj` deletes the variable name, not the object directly.
- The object is removed only when it becomes unreachable and can be collected.

### Key point
- In modern Python, cyclic garbage collection can usually clean unreachable cycles, even when `__del__()` exists.

## Memory Management Best Practices

1. **Use Local Variables**
   Local variables usually have a shorter lifetime than global variables, so they are released sooner.

2. **Avoid Circular References**
   Circular references can delay cleanup and make memory usage harder to reason about.

3. **Use Generators**
   Generators produce one value at a time instead of storing all values in memory at once.

4. **Delete Unused Objects**
   Use `del` when you want to remove references that are no longer needed.

5. **Profile Memory Usage**
   Use tools like `tracemalloc` to understand how memory is being used.

## Generators and Memory Efficiency

### Why generators help
- Lists store all items in memory at once.
- Generators create values one by one when needed.

### Example
```python
def squares(n):
    for i in range(n):
        yield i * i
```

### Key point
- Generators are memory-efficient for large datasets and streaming data.

## Memory Profiling

### Why profiling matters
- Profiling helps find memory-heavy code and possible leaks.
- It is useful when programs become slow or consume too much RAM.

### `tracemalloc`
- `tracemalloc.start()` starts tracking memory allocations.
- `tracemalloc.get_traced_memory()` returns current and peak memory usage.
- `tracemalloc.stop()` stops tracking.

### Example pattern
```python
import tracemalloc

tracemalloc.start()

# code here

current, peak = tracemalloc.get_traced_memory()
print(current, peak)

tracemalloc.stop()
```

## Reference Counting vs Garbage Collection

### Reference Counting
- Immediate cleanup when reference count becomes zero
- Fast and simple
- Cannot handle circular references by itself

### Garbage Collection
- Detects and removes unreachable cycles
- Runs periodically or manually
- Complements reference counting

## Quick Rules

- Use `sys.getrefcount()` to understand references.
- Use `gc.collect()` to manually trigger collection for demos or debugging.
- Do not rely on `del` alone to break circular references.
- Prefer generators when processing large sequences.
- Use `tracemalloc` when checking memory usage.

## Interview-Style Summary

- Python memory management mainly uses reference counting and garbage collection.
- Reference counting destroys objects when the count becomes zero.
- Circular references need garbage collection.
- `del` removes a reference, not always the object.
- Generators save memory by yielding values one at a time.
- `tracemalloc` is useful for memory profiling.
