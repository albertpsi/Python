### Multithreading With Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def Print_numbers(number):
    time.sleep(1)  # Simulate a time-consuming task
    print(f"Number: {number}")

number=[1, 2, 3, 4, 5,6,7,8,9,10]

time_start = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(Print_numbers, number)

for result in results:
    result

time_finish = time.time() - time_start
print(f"Total execution time: {time_finish:.2f} seconds")