"""
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation

This file compares two different process-based APIs in Python:
1. multiprocessing.Pool()
2. concurrent.futures.ProcessPoolExecutor()

Both approaches use multiple processes, so both are useful for CPU-bound work.
The main difference is the programming interface:
- multiprocessing.Pool() is the older multiprocessing-specific API.
- ProcessPoolExecutor() is the newer high-level API that works with Future objects.
"""

# Import multiprocessing so we can use multiprocessing.Pool().
import multiprocessing
# Import math so we can calculate factorial values.
import math
# Import sys so we can increase Python's integer-to-string digit limit for very large numbers.
import sys
# Import time so we can measure how long each approach takes.
import time
# Import ProcessPoolExecutor so we can compare it with multiprocessing.Pool().
from concurrent.futures import ProcessPoolExecutor, as_completed

# Increase the digit limit so converting large factorial values to strings does not raise an error.
sys.set_int_max_str_digits(1_000_000)


# Define a worker function that calculates the factorial of a number.
def calculate_factorial_summary(number):
    # Calculate the factorial value for the given number.
    result = math.factorial(number)
    # Count how many digits are in the factorial result.
    digits = len(str(result))
    # Return a small summary instead of printing the full factorial value.
    return number, digits


# Define a function that demonstrates the older multiprocessing.Pool() API.
def run_with_multiprocessing_pool(numbers):
    # Print a heading so the console output clearly shows which approach is running.
    print("Running with multiprocessing.Pool()...")
    # Record the start time for the Pool-based run.
    start_time = time.time()

    # Create a process pool with 3 worker processes.
    with multiprocessing.Pool(processes=3) as pool:
        # pool.map() sends all numbers to worker processes and returns results in input order.
        results = pool.map(calculate_factorial_summary, numbers)

    # Print the results returned by pool.map().
    for number, digits in results:
        # Show a short summary for each factorial result.
        print(f"Pool.map -> factorial({number}) has {digits} digits")

    # Measure how long the Pool-based run took.
    end_time = time.time() - start_time
    # Print the total execution time for multiprocessing.Pool().
    print(f"multiprocessing.Pool() execution time: {end_time:.2f} seconds")


# Define a function that demonstrates the newer ProcessPoolExecutor API.
def run_with_process_pool_executor(numbers):
    # Print a heading so the console output clearly shows which approach is running.
    print("Running with ProcessPoolExecutor(max_workers=3)...")
    # Record the start time for the executor-based run.
    start_time = time.time()

    # Create a process pool executor with 3 worker processes.
    with ProcessPoolExecutor(max_workers=3) as executor:
        # submit() returns Future objects, which is the main API difference from Pool().
        futures = [executor.submit(calculate_factorial_summary, number) for number in numbers]

        # as_completed() yields futures as soon as each task finishes, not necessarily in input order.
        for future in as_completed(futures):
            # Read the completed result from the Future object.
            number, digits = future.result()
            # Show a short summary for each completed task.
            print(f"Future completed -> factorial({number}) has {digits} digits")

    # Measure how long the executor-based run took.
    end_time = time.time() - start_time
    # Print the total execution time for ProcessPoolExecutor().
    print(f"ProcessPoolExecutor() execution time: {end_time:.2f} seconds")


# Run the comparison only when this file is executed directly.
# This guard is required on Windows for process-based parallel code.
if __name__ == "__main__":
    # Create a small list of CPU-heavy tasks to compare across both APIs.
    numbers = [5000, 6000, 7000]

    # Run the multiprocessing.Pool() example first.
    run_with_multiprocessing_pool(numbers)
    # Print a blank line to separate the two demos in the console.
    print()
    # Run the ProcessPoolExecutor() example second.
    run_with_process_pool_executor(numbers)
    # Print a short summary that explains the API difference.
    print()
    print("API difference summary:")
    print("multiprocessing.Pool() uses Pool-specific methods such as map() and apply_async().")
    print("ProcessPoolExecutor() uses Future objects through submit(), result(), and as_completed().")
