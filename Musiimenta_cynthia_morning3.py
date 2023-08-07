
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Cynthia calc")

# Create an entry field
entry = tk.Entry(window, width=45)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operators
button_1 = tk.Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))

button_add = tk.Button(window, text="+", padx=20, pady=10, command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=20, pady=10, command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=20, pady=10, command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=20, pady=10, command=lambda: button_click("/"))
button_clear = tk.Button(window, text="C", padx=20, pady=10, command=button_clear)
button_equal = tk.Button(window, text="=", padx=20, pady=10, command=button_equal)

# Position the buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)

# Start the main event loop
window.mainloop()

"""Day3
#arithmetic operator
+ add
_subtract
* multiply
/ division
% modulus
** exponentiation


COMPARISON OPERATORS
== equal to
!= not eqaul to 
> greater than
< less than
>=greater or equal to
<= less or equal to

"""
"""
LOGICAL OPERATORS
logical and--and
logical or---or
 
 ASSIGNMENT OPERATORS
 assign a value--'='
 add a value--'+'
 add and assign value '+='
 subtract and assign value '-='
 multiply and assign value '*='
 divide and assign value '/='
 modulus and assign a value '%='
 exponentiate and assign value '**='
 
 MEMBERSHIP OPERATORS
 'in'-- checks if a variable exists in a sequence
 'not in'-- checks if a value does not exist in a sequence
 
 IDENTITY OPERATORS
 'is'--- checks if two values are the same
 'is not' checks if two values are not the same
"""
"""# examples of arthmetic operators
# addition
a = 50+45
print(a)
# subtraction
b = 50-45
print(b)
# multiplication
c = 50*45
print(c)
# division
d = 50/2
print(d)
# modulus
e = 50 % 3
print(e)
# exponentiation
f = 2**3
print(f)
# comparison operators
x = 35
z = 30
# greater
if x > z:
 print('its greater')
 # less
 if x<z:

  print('its less')
else:
    print('its false')
    # greater or equal
if x>=z:
 print('its greater or equal')
 # logical operators
n = True
m = False
# AND
print(n and m)
# OR
print(n or m)
# NOT
print(not n)
print(not m)

# ASSIGNMENT OPERATORS
q = 5
# add and assign
q += 3
print(q)
# subtract and assign
v = 8
v -= 2
print(v)

# multiply and assign

u = 4
u *= 2
print(u)

# division and assign
r = 10
r /= 2
print(r)
# membership operators
cars = ['jeep','tesla','BMW']
if 'jeep' in cars:
    print('its in cars')
    print('tesla' in cars)
    print('BMW' in cars)
# identity operators
g = 100
p = 100
print(g is p)
print(g is not p)
print(g ==p)
g = [1 , 2,3,4,5]
p = [1,2,3,4,5]
print(g is not p)

# BITWISE OPERATORS
# They are used to perform operations on individual bits in of binary numbers
# Bitwise And('&): perform bitwise and operation between the corresponding bits of two integers
or(|): performs bitwise OR operation between the corresponding bits
XOR('^'): performs XOR operation
NOT(~)
left shift(<<)
right shift(>>)

a = 10
b = 20
result = a & b
catt = a| b
dogg= a ^ b
gug= ~a
print(result)
print(catt)
print(dogg)
print(gug)
# create a simple calc function to calculate (add, subtract, multiply, divide)

"""








