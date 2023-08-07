 # exception handling

try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
    print("Result:", result)  # This line will not be executed
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("An error occurred:", str(e))
else:
    print("No exceptions occurred.")
finally:
    print("it will execute.")

print("Program continues...")

# file handling
# Open the file in read mode
with open("cynthia.txt", "r") as file:
    # Read the entire file content
    content = file.read()
    print(content)
# Open the file in write mode
with open("cynthia.txt", "w") as file:
    file.write("have a beautiful day !")
# file handling and exception handling together
try:
    # Open the file in read mode
    with open("cynthia.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")