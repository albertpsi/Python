# MultiProcessing - Process Pool Executor
### Process Pool Executor is a high-level interface for managing a pool of worker processes. It provides a convenient way to execute tasks in parallel across multiple processes, which can be particularly beneficial for CPU-bound tasks that require intensive computation.
### The Process Pool Executor is part of the concurrent.futures module in Python and allows you to easily submit tasks to a pool of worker processes and retrieve their results asynchronously.
### It abstracts away the complexities of managing processes and provides a simple interface for parallel execution, making it easier to write concurrent code that can take advantage of multiple CPU cores.

from concurrent.futures import ProcessPoolExecutor
from time import sleep, time

def square_number(number):
    sleep(2)  # Simulate a time-consuming task
    return f"Process: {number}^2 = {number**2}"
numbers = [1, 2, 3, 4, 5,6,7,8,9,10]

if __name__ == "__main__":

    time_start = time()

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)

    time_finish = time() - time_start
    print(f"Total execution time: {time_finish:.2f} seconds")