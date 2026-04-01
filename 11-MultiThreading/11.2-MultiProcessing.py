## PRocesses that run in parallel
### CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## PArallel execution- Multiple cores of the CPU can be utilized to run multiple processes simultaneously, improving performance for CPU-bound tasks.
### Memory Isolation- Each process has its own memory space, which can help prevent issues related to shared memory and data corruption.
### Inter-Process Communication (IPC)- Processes can communicate with each other using various IPC mechanisms, such as pipes, queues, and shared memory, to exchange data and coordinate their actions.
### Process Creation- Processes can be created using the multiprocessing module in Python, which provides a simple interface for spawning processes and managing their execution.
### Process Synchronization- The multiprocessing module also provides synchronization primitives like locks, semaphores, and events to help coordinate the execution of processes and prevent race conditions.
### Process Pooling- The multiprocessing module allows you to create a pool of worker processes that can be used to execute tasks in parallel, which can help improve performance and reduce the overhead of creating and managing individual processes.    

import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1)  # Simulate a time-consuming task
        print(f"Process: {i}^2 = {i**2}")

def cube_number():
    for i in range(5):
        time.sleep(1.5)  # Simulate a time-consuming task
        print(f"Process: {i}^3 = {i**3}")

if __name__ == "__main__": # Entry point of the program
    # This is necessary to prevent the child processes from executing the code that creates new processes when they are spawned.
    # create 2 processes

    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube_number)

    start_time = time.time()

    # start the processes
    p1.start()
    p2.start()

    # wait for the processes to complete
    p1.join()
    p2.join()

    finish_time = time.time() - start_time
    print(f"Total execution time: {finish_time:.2f} seconds")
