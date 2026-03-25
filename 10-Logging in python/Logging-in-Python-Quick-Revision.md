# Logging in Python Quick Revision

Based on:

- `10.1-Logging.ipynb`
- `10.2-Logging with multiple Loggers.ipynb`
- `10.3-Test.py`

## 1. Why Logging Matters

### Core idea

- Logging records events that happen while a program runs.
- It is better than using `print()` for debugging and monitoring real applications.

### Common uses

- Debugging issues
- Tracking execution flow
- Recording warnings and errors
- Keeping operational history in log files

---

## 2. Log Levels

### Standard levels

- `DEBUG`: detailed developer information
- `INFO`: normal runtime events
- `WARNING`: something unexpected but not fatal
- `ERROR`: operation failed
- `CRITICAL`: serious failure

### Key point

- Set the logger level so only messages of that level and above are shown.

---

## 3. Basic Configuration

### Common setup

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

### Key points for revision

- `level` controls the minimum severity that gets logged.
- `format` controls how each log line looks.
- `datefmt` customizes timestamp formatting.

---

## 4. Handlers

### Core idea

- Handlers decide where log messages go.

### Common handlers used here

- `logging.FileHandler("app.log")` for saving logs to a file
- `logging.StreamHandler()` for printing logs to the console

### Example idea

- One logger configuration can write the same message to both the console and a file.

---

## 5. Multiple Loggers

### Core idea

- Different modules can use different named loggers.

### Example

```python
logger_one = logging.getLogger("module_one")
logger_two = logging.getLogger("module_two")
```

### Why it helps

- Makes logs easier to filter
- Shows which module produced each message
- Supports larger applications cleanly

---

## 6. Logging Errors Safely

### Common pattern

```python
try:
    return x / y
except ZeroDivisionError:
    logger.error("Attempted to divide by zero")
```

### Key point

- Log errors with enough context to understand what failed.

---

## 7. Reconfiguration Note

### Important idea

- `logging.shutdown()` closes handlers, but it does not fully reset logger configuration by itself.
- If logging seems not to reconfigure, existing handlers may still be attached.

### Practical takeaway

- Reconfigure carefully, especially in notebooks and repeated runs.

---

## Best Practices Checklist

- Use `logging` instead of `print()` in real applications.
- Choose the correct level: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
- Add timestamps and logger names in the format string.
- Use file and stream handlers when you need both persistence and console visibility.
- Use separate named loggers for larger projects.

---

## Frequently Asked Interview Questions (Short Answers)

1. **Why use logging instead of print?**

- Logging gives severity levels, formatting, filtering, and file output.

2. **What does `basicConfig()` do?**

- It provides a quick way to configure the root logger.

3. **What is a handler in logging?**

- A handler sends log messages to a destination such as a file or console.

4. **Why use multiple loggers?**

- To separate logs by module or feature.

5. **What are the standard logging levels?**

- `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
