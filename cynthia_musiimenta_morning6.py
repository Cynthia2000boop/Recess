# context managers , maltithreading and maltiprocessing
# context manager is an object  that defines a temporary context for  a block of code
"""def open__file(filename):
    File = open(filename"r")
def __enter__():
    return File
def __exit__(self, exc_type, exc_value,exc_tb):
File.close()
return __enter__(),__exit__()


with open("cynthia.txt") as f:
    contents=f.read()"""

"""import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_traceback):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f"The time for this execution was {execution_time} seconds elapsed")


with Timer():
    time.sleep(2)"""

   # multithreading and multiprocessing

   # techniques that can be used to improve  performance of a python program
   # multithreading is a technique where multiple threads are created with a single process.
   # multiprocessing is a technique where multiple threads are created


"""import threading


def task(name):
    print(f"running task {name}")


threads = []
for i in range(5):
    t = threading.Thread(target=task, args=(f"thread({i})",))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()"""

# multiprocesssing example


"""import multiprocessing

def process(name):
    print(f"processing task {name}")

if __name__ == '__main__':
    # Create a pool of processes
    pool = multiprocessing.Pool(processes=5)

    # Submit multiple tasks to the pool
    for i in range(6):
        pool.apply_async(process, args=(f"process {i}",))

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()"""



# multithreading and multiprocessing together
"""import threading
import multiprocessing

def task(name):
    print(f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")

# Create multiple threads
threads = []
for i in range(4):
    t = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
"""


"""
assignment
(a) show a context manager for file handling that automatically opens and closes a file
(b) show a context manager for managing a database connection
(c) show a multithreading and multiprocessing for different amounts of time
"""

class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()

filename = "cynthia.txt"
with FileHandler(filename, "r") as file:
    contents = file.read()
    print(contents)

# context manager with databases
import sqlite3

class DatabaseManager:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.database_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.connection.close()

# Usage example
database_name = "mydb"
with DatabaseManager(database_name) as db:
    # Perform database operations using the connection `db`
    cursor = db.cursor()
    cursor.execute("SELECT * FROM MyGuests ")
    result = cursor.fetchall()
    for row in result:
        print(row)

# The database connection is automatically closed when exiting the context

# multithreading and multiprocessing
import threading
import multiprocessing
import time

def perform_task(task_name, duration):
    print(f"Task {task_name} started.")
    time.sleep(duration)
    print(f"Task {task_name} completed.")

if __name__ == '__main__':
    # Multithreading example
    threads = []
    for i in range(5):
        t = threading.Thread(target=perform_task, args=(f"Thread {i}", i+1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Multiprocessing example
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=perform_task, args=(f"Process {i}", i+1))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
