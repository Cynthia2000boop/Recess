# afternoon exercise
# Creating a dictionary
my_dict = {'dog': 3, 'cat': 7, 'bird': 2}
# Using values() method to create a list of items from a dictionary
item_list = list(my_dict.values())
print(item_list)
# Checking if a specific key exists in a dictionary
if 'cat' in my_dict:
    print("The key 'cat' exists in the dictionary.")
# Changing and updating items in a dictionary
my_dict['dog'] = 4
my_dict['fish'] = 9
print(my_dict)
# Adding and removing items from a dictionary
my_dict['rabbit'] = 6
del my_dict['bird']
print(my_dict)
# Looping through a dictionary and nesting dictionaries within dictionaries
nested_dict = {'person1': {'name': 'Alice', 'age': 25},
               'person2': {'name': 'Bob', 'age': 30}}

for key, value in nested_dict.items():
    print(key)
    for sub_key, sub_value in value.items():
        print(f'{sub_key}: {sub_value}')
# Determining the length of a string using the len() function
my_string = "Hello, world "
length = len(my_string)
print(length)
# Iterating through each character in a string using a for loop
for char in my_string:
    print(char)
# Slicing a string to extract specific portions of it
my_slice = my_string[7:13]
print(my_slice)
# Performing arithmetic operations with numbers and printing the results
a = 10
b = 2
sum_result = a + b
sub_result = a - b
mul_result = a * b
div_result = a / b

print(f"Sum: {sum_result}")
print(f"Difference: {sub_result}")
print(f"Product: {mul_result}")
print(f"Division: {div_result}")
# Using boolean values and conditions to control program flow
condition = True

if condition:
    print("Condition is True")
else:
    print("Condition is False")


# CLASS PRACTICE
"""thisdict = {
  "brand": "iphone",
  "model": "13pro",
  "year": 2021
}
print(thisdict)
# using the get()
x = thisdict.get("model")
# change values
thisdict["year"] = 2023
# length of dict
print(len(thisdict))
# Make a copy of a dictionary with the copy() method:
mydict = thisdict.copy()
print(mydict)

k = 16    
j = 3.7  
r = 1j
print(type(k))
print(type(j))
print(type(r))

x = 4
y = 563732622554887711
z = -567388

print(type(x))
print(type(y))
print(type(z)
# FLOAT
m = 35e3
h = 12E4
n = -87.7e100

print(type(m))
print(type(h))
print(type(n)
# COMPLEX
x = 6+9j
y = 1j
z = -1j

print(type(x))
print(type(y))
print(type(z))

x = 1 
y = 2.8  
z = 1j 

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# CASTING
x = str("s1") 
y = str(2)    
z = str(3.0) 
 #STRINGS
 a = "Jesus loves us !"
print(len(a))

a = " Jesus saved us! "
print(a.strip())
print(a.lower())
print(a.upper())
print(a.split(","))
txt = "And through him, we can face tomorrow"
x = "im" in txt
print(x)
a = "love"
b = "Jesus"
c = a + " " + b
print(c)

quantity = 3
item_no = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, item_no, price))

# booleans
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
"""
