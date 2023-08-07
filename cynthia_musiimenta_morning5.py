"""
regular expressions
generators and iterators
decorators
context managers
multithreading and multiprocessing
REGULAR EXPRESSIONS
\d: matches any digit
\w: matches alphanumeric character
/s: matches any white space character
.: matches any character accept a new line
*: matches zero or more occurences of the preceding
+ matches one or more occurrence of the proceding character or group
? matches zero or one occurrence of the proceding character or group
[] matched any character within square brackets
[^] matches any character not within square brackets
^ matches the start of the line
$ matches the end of the line


"""
# example1 demonstrating regex | match first word, match group of words,match all numbers
"""import re
text = " hello my name is  cynthia . i am a programmer with 15 years experience"
# match first word
match = re.search(r"\b\w+\b",text)
if match:
    print("Matches:", match.group())
matches = re.findall(r"\d+", text)
print("matches",matches)
mam= re.search(r"^", text)
print("matches:", mam)"""
# example2 validate email format or email address
import re

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return True
    else:
        return False

email1 = "musiimentacynthia@gmail.com"
email2 = "musiimentacynthia@gmailcom"

print(validate_email(email1))
print(validate_email(email2))

""" Generators and iterators
'yield' generator
 iterator '__iter__' "__next__" iterator
 
"""
def factorial(n):
    # return factorial of a number
    if n == 0:
        yield 1
    else:
        yield n * factorial(n - 1)

        fact = 1
    for i in range(1,n+1):
        fact *=i
        yield fact
# print the factorial of a number from 1-10

for i in range(1,10):

    print(factorial(i))
# example 3 : generate function that yields the square of numbers from 1 to 10

def squares():
    for i in range(1,10):
        yield i**2
        # create iterator object
squares_iterator=squares()
# print the first 5 square numbers
for i in range(5):
    print(next(squares_iterator))

# decorators allows to  modify the behavior of classes or functions without changing their source code
# @my_decorator
def my_decorator(func):
    def inner():
        print("this is the decorator")
        func()
    return inner
@my_decorator
def outer_decorator():
    print("this is the outer decorator")
outer_decorator()

"""CONTEXT MANAGERS
Context managers are objects that can be used in Python's with statements.
__enter__() – setup the context and optionally return some object
__exit__() – cleanup the object.
"""
from pathlib import Path
import os

target_directory = "/"
# Store the current directory
previous_directory = os.getcwd()

# Change to the target directory
os.chdir(target_directory)

try:
    # Code to be executed in the target directory
    print("Current Directory:", Path.cwd())
finally:
    # Return to the previous directory
    os.chdir(previous_directory)

# Continue with the main program logic
print("Back to Previous Directory:", Path.cwd())

# example2 0n context manager
try:
    with open("cynthia.txt") as f:
        contents = f.read()
        # Process the contents as needed
        print("File Contents:", contents)
except FileNotFoundError:
    print("Error: File not found.")
except IOError as e:
    print(f"Error reading file: {e}")

"""MALTITHREADING AND MALTIPROCESSING
Multithreading involves executing multiple threads within the same process. 
Threads are lightweight units of execution that share the same memory space and resources of the parent process.

 """
import threading

def task():
    # Code to be executed concurrently
    print("Executing task...")

# Create multiple threads
thread1 = threading.Thread(target=task)
thread2 = threading.Thread(target=task)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Continue with the main program
print(" wawoo Threads have finished executing.")

# Continue with the main program

"""
maltiprocessing
Multiprocessing involves the execution of multiple processes, where each process has its own memory space and resources

"""
import multiprocessing

def display():
    # Code to be executed concurrently
    print("Executing task...")

# Create multiple processes
process1 = multiprocessing.Process(target=display)
process2 = multiprocessing.Process(target=display)

# Start the processes
process1.start()
process2.start()

# Wait for the processes to finish
process1.join()
process2.join()

# Continue with the main program
print(" wawoo Processes have finished executing.")
