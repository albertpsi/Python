# This example shows two ways to perform concurrent web scraping for I/O-bound work.
# The first approach uses the low-level threading module directly.
# The second approach uses ThreadPoolExecutor, which is usually simpler for this kind of task.

# Import threading so we can manually create and manage threads.
import threading
# Import time so we can measure how long each approach takes to finish.
import time
# Import ThreadPoolExecutor so we can manage a pool of worker threads more easily.
from concurrent.futures import ThreadPoolExecutor

# Import requests so the program can download web pages over HTTP.
import requests
# Import BeautifulSoup so the downloaded HTML can be parsed into text.
from bs4 import BeautifulSoup

# Store the target URLs in a list so both approaches can process the same pages.
urls = [
    # First page to fetch.
    "https://docs.langchain.com/oss/python/langchain/overview/",
    # Second page to fetch.
    "https://docs.langchain.com/oss/python/langgraph/overview/",
    # Third page to fetch.
    "https://docs.langchain.com/oss/python/learn/",
]


# Define a worker function that downloads one page and prints basic information about it.
def fetch_content(url):
    # Send an HTTP GET request to the given URL.
    response = requests.get(url)
    # Raise an exception if the server returns an HTTP error such as 404 or 500.
    response.raise_for_status()
    # Parse the HTML response body with Python's built-in HTML parser.
    soup = BeautifulSoup(response.content, "html.parser")
    # Print the URL and the number of characters in the extracted page text.
    print(f"Fetched {url}, length: {len(soup.text)} characters")


# Define a function that runs the scraping task by creating one Thread object per URL.
def run_with_manual_threads():
    # Print a label so the output clearly shows which approach is running.
    print("Starting web scraping with manual threads...")
    # Create an empty list so we can keep references to all started threads.
    threads = []
    # Record the start time before launching any worker threads.
    start_time = time.time()

    # Loop through each URL so we can create a separate thread for that page.
    for url in urls:
        # Create a thread that will call fetch_content with the current URL.
        thread = threading.Thread(target=fetch_content, args=(url,))
        # Save the thread object so we can wait for it later.
        threads.append(thread)
        # Start the thread so the HTTP request begins running concurrently.
        thread.start()

    # Loop through the stored thread objects after they have all been started.
    for thread in threads:
        # Wait for each thread to finish before ending this function.
        thread.join()

    # Calculate the elapsed time for the manual-threading approach.
    end_time = time.time() - start_time
    # Print the total execution time for the manual-threading approach.
    print(f"Manual threading execution time: {end_time:.2f} seconds")


# Define a function that runs the same scraping task using a thread pool.
def run_with_thread_pool():
    # Print a label so the output clearly shows which approach is running.
    print("Starting web scraping with thread pool executor...")
    # Record the start time before submitting any work to the thread pool.
    start_time = time.time()

    # Create a thread pool with one worker per URL for this small fixed example.
    # This is fine here because the list is short, but large URL lists should use a sensible cap instead.
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        # Submit each URL to the pool by mapping the worker function across the URL list.
        executor.map(fetch_content, urls)

    # Calculate the elapsed time for the thread-pool approach.
    end_time = time.time() - start_time
    # Print the total execution time for the thread-pool approach.
    print(f"Thread pool execution time: {end_time:.2f} seconds")


# Run the examples only when this file is executed directly.
# This guard prevents the demo code from running automatically if the file is imported elsewhere.
if __name__ == "__main__":
    # Run the manual-threading version first so you can compare it with the pool version.
    run_with_manual_threads()
    # Print a blank line to make the console output easier to read.
    print()
    # Run the ThreadPoolExecutor version second.
    run_with_thread_pool()
