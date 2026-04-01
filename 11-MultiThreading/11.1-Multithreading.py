### Multithreading
## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_number():
    for i in range(5):
        print(f"Number:{i}")
        time.sleep(2) # Simulating a time-consuming task

def print_letter():
    for letter in 'ABCDE':
        print(f"Letter:{letter}")
        time.sleep(2) # Simulating a time-consuming task

print("Without threading:")

t= time.time()
print_number() # This will block the execution of print_letter() until print_number() is finished
print_letter()

print(f"Time taken without threading: {time.time() - t} seconds")

print("\nWith threading:")
# Using threading
t = time.time()
# Create threads for each function
thread1 = threading.Thread(target=print_number)
thread2 = threading.Thread(target=print_letter)

# Start the threads
thread1.start()
thread2.start()
# Wait for both threads to finish
thread1.join() # This will block the main thread until thread1 is finished, 
#once t1 is finished, it will move to thread2.join() and wait for thread2 to finish
thread2.join()
# once both the threads are finished, with join these threads will be terminated and the main thread will continue to execute the next line of code
print(f"Time taken with threading: {time.time() - t} seconds")