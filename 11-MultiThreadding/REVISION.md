# Revision Notes: Multithreading and Multiprocessing

## 11.1 Multithreading

### What it is
- Multithreading runs multiple threads inside the same process.
- Threads share the same memory space.
- It is useful when the program spends time waiting, such as waiting for file I/O, API calls, or web requests.

### When to use it
- I/O-bound tasks
- Concurrent waiting tasks
- Lightweight background work

### Important methods
- `threading.Thread(target=...)` creates a new thread.
- `start()` begins thread execution.
- `join()` makes the main thread wait until the thread finishes.

### Key point
- Threads improve responsiveness for I/O-bound tasks.
- Threads do not usually speed up CPU-bound Python code because of the GIL.

## 11.2 Multiprocessing

### What it is
- Multiprocessing runs multiple processes instead of multiple threads.
- Each process has its own memory space.
- It is useful for CPU-bound tasks such as heavy calculations.

### When to use it
- Mathematical computation
- Image processing
- Data processing
- Parallel CPU-heavy tasks

### Important methods
- `multiprocessing.Process(target=...)` creates a new process.
- `start()` begins the process.
- `join()` waits for the process to finish.

### Key point
- Processes can use multiple CPU cores.
- On Windows, process code should be inside `if __name__ == "__main__":`.

## 11.3 ThreadPoolExecutor

### What it is
- `ThreadPoolExecutor` is a higher-level way to manage threads.
- Instead of creating threads manually, you create a pool of worker threads.

### Why use it
- Cleaner than manual `threading.Thread`
- Easier to scale
- Better for many similar I/O-bound tasks

### Common pattern
```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(task_function, items)
```

### Key point
- Use `ThreadPoolExecutor` when you have many similar I/O tasks.
- Prefer it over manual thread creation for cleaner code.

## 11.4 ProcessPoolExecutor

### What it is
- `ProcessPoolExecutor` is a higher-level way to manage worker processes.
- It is part of `concurrent.futures`.

### Why use it
- Cleaner API than low-level multiprocessing management
- Good for CPU-bound work
- Similar interface to `ThreadPoolExecutor`

### Common pattern
```python
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=3) as executor:
    results = executor.map(task_function, items)
```

### Key point
- Use `ProcessPoolExecutor` for CPU-bound work when you want a simple modern API.

## 11.5 Web Scraping Example

### What it teaches
- Web scraping is usually I/O-bound because the program waits for network responses.
- This makes threading a good fit.

### Two approaches used
- Manual threads with `threading.Thread`
- Thread pool with `ThreadPoolExecutor`

### Why threading works here
- While one request waits for the server, another thread can work on another request.

### Key point
- For small demos, `max_workers=len(urls)` is okay.
- For larger real-world scraping, use a sensible fixed limit instead of one thread per URL.

## 11.6 Factorial Multiprocessing Example

### What it teaches
- Factorial calculation is CPU-bound.
- CPU-bound tasks are better suited to multiprocessing than multithreading.

### Two approaches compared
- `multiprocessing.Pool(processes=3)`
- `ProcessPoolExecutor(max_workers=3)`

### Main difference
- `multiprocessing.Pool()` is the older multiprocessing-specific API.
- `ProcessPoolExecutor()` is the newer high-level API using `Future` objects.

### Practical difference
- `Pool()` commonly uses methods like `map()`, `starmap()`, `apply()`, and `apply_async()`.
- `ProcessPoolExecutor()` commonly uses `submit()`, `map()`, `result()`, and `as_completed()`.

### Key point
- Both use processes.
- The difference is mostly API style and convenience.

## Multithreading vs Multiprocessing

### Multithreading
- Best for I/O-bound tasks
- Threads share memory
- Lower overhead
- Limited for CPU-bound work in normal Python because of the GIL

### Multiprocessing
- Best for CPU-bound tasks
- Processes do not share memory by default
- Higher overhead than threads
- Can use multiple CPU cores properly

## ThreadPoolExecutor vs ProcessPoolExecutor

### ThreadPoolExecutor
- Uses threads
- Best for I/O-bound tasks
- Good for APIs, downloads, file reading, and scraping

### ProcessPoolExecutor
- Uses processes
- Best for CPU-bound tasks
- Good for heavy calculations and data processing

## multiprocessing.Pool() vs ProcessPoolExecutor()

### `multiprocessing.Pool()`
- Older API
- Good for classic multiprocessing code
- Uses pool-specific methods

### `ProcessPoolExecutor()`
- Newer API
- Easier to read and maintain
- Uses `Future` objects
- Similar style to `ThreadPoolExecutor`

## Quick Rules

- Use `threading` for simple thread demos.
- Use `ThreadPoolExecutor` for practical I/O-bound concurrent tasks.
- Use `multiprocessing.Process` for learning basic process creation.
- Use `multiprocessing.Pool()` for classic multiprocessing patterns.
- Use `ProcessPoolExecutor` for modern CPU-bound parallel code.

## Interview-Style Summary

- I/O-bound task: use threads or `ThreadPoolExecutor`
- CPU-bound task: use processes or `ProcessPoolExecutor`
- Threads share memory
- Processes have separate memory
- `join()` waits for completion
- `__name__ == "__main__"` is important for multiprocessing on Windows
- `ThreadPoolExecutor` and `ProcessPoolExecutor` are high-level APIs
- `multiprocessing.Pool()` is older than `ProcessPoolExecutor()`
