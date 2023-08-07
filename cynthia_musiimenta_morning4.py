# inheretence
class Animal:
  def __init__(self, name):
    self.name = name


  def eat(self):
    print(f"{self.name}, is eating")

    class Dog(Animal):
        def bark(self):
            print(f"{self.name},is barking")


    class cat(Animal):
        def mweuw(self):
            print(f"{self.name},is mweuwing")

   #creating Animal objects

    animal=Animal("general animal")
    do= Dog("stop")
    ca= cat("joo")

    #  invoking the method
    animal.eat()
    do.eat()
    ca.eat()
    do.bark()
    ca.mweuw()

# example 2
class car:
  def __init__(self, brand, color,num_wheels):
    super(car, self).__init__(brand,color)
    def desplay(self):
        print("brand",self.brand)
        print("color", self.color)
    def hon(self):
        print("honking the horn")
# exercise 1
"""
demonstrate using inheritence to calculate the area and perimeter of a circle and a rectangle
"""
class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculate and print the area and perimeter
print("Circle - Area:", circle.calculate_area())
print("Circle - Perimeter:", circle.calculate_perimeter())

print("Rectangle - Area:", rectangle.calculate_area())
print("Rectangle - Perimeter:", rectangle.calculate_perimeter())

# multiple inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Flyable:
    def fly(self):
        print(f"{self.name} is Flying")


class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def display_info(self):
        print(f" Name:{self.name} ")
        print( f" Specie:{self.species} .")



# Create an instance of Bird
bird = Bird("pigeon", "bird")

# Access methods from Animal class
bird.eat()

# Access methods from Flyable class
bird.fly()

# Access methods from Bird class
bird.display_info()


# method overriding.....me
class Animal:
    def  sound(self):
        print("animal is making sound")
class Dog(Animal):
    def sound(self):
        print("dog is barking")
class cat(Animal):
    def sound(self):
        print("cst is mewing")
def make_animal_sound(Animal):
    Animal.sound()
animals = Animal()
dogs = Dog()
cats = cat()
# calling the make animal sound function
make_animal_sound(animals)
make_animal_sound(dogs)
make_animal_sound(cats)

"""POLYMORPHISM
allows to write code that can be used in different objects
 method overloading allows the class to have multiple methods with the same name but different parameter
 method overriding occurs when a child class provides its own implementation of a method that is already defined in its super class
 """
# example 4
class shape:
    def calculate_area(self):
        pass
class rectangle(shape):
    def __init__(self, length,widith):
        self.length = length
        self.width = widith
    def calculate_area(self):
        return self.length * self.width
    class circle(shape):
        def __init__(self, radius):
            self.radius = radius
        def calculate_area(self):
            return 3.14 * self.radius **2
        def calculate_cirmufrance(self):
            return 2* 3.14* self.radius

# creating shape objects
rectangles= rectangle(5,5)
#circles = circle(5)
# calculate display area
print("rectangle area:",rectangles.calculate_area())
#print("circle area:",circles.calculate_area())


# overloaading
class Calc:
    def add(self, x, y, c=None):
        if c is None:
            return x + y
        else:
            return x + y + c

my_calc = Calc()
print(my_calc.add(1, 2))
print(my_calc.add(1, 2, 3))

    # abstraction
   # allows you to focus on essental features and hide them from uneccessary details

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Starting a car")

    def stop(self):
        print("Stopping a car")


class Truck(Vehicle):
    def start(self):
        print("Starting a truck")

    def stop(self):
        print("Stopping a truck")


car = Car()
car.start()
car.stop()

truck = Truck()
truck.start()
truck.stop()

# exercise 2 demonstrate abstraction using calculation of area
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Creating instances and calculating areas
circle = Circle(5)
circle_area = circle.calculate_area()
print(f"Area of circle: {circle_area}")

rectangle = Rectangle(4, 6)
rectangle_area = rectangle.calculate_area()
print(f"Area of rectangle: {rectangle_area}")


# assignment: receipt program
import tkinter as tk


class ReceiptItem:
    def __init__(self, item, quantity, price):
        self.item = item
        self.quantity = quantity
        self.price = price

    def calculate_total(self):
        return self.quantity * self.price

    def get_details(self):
        return f"{self.item}\t{self.quantity}\t\t{self.price:.2f}"


class GroceryItem(ReceiptItem):
    pass


class ElectronicsItem(ReceiptItem):
    def calculate_total(self):
        # Apply a 10% discount for electronics items
        total = super().calculate_total()
        return total - (0.1 * total)


class ReceiptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cynthia's Receipt Book")

        self.item_label = tk.Label(root, text="Item:")
        self.item_label.pack()
        self.item_entry = tk.Entry(root)
        self.item_entry.pack()

        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.pack()

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.item_type_label = tk.Label(root, text="Item Type:")
        self.item_type_label.pack()
        self.item_type_var = tk.StringVar(root)
        self.item_type_var.set("Grocery")
        self.item_type_dropdown = tk.OptionMenu(root, self.item_type_var, "Grocery", "Electronics")
        self.item_type_dropdown.pack()

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.receipt_text = tk.Text(root)
        self.receipt_text.pack()

        self.print_button = tk.Button(root, text="Print Receipt", command=self.print_receipt)
        self.print_button.pack()

        self.receipt_items = []

    def add_item(self):
        item = self.item_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        item_type = self.item_type_var.get()

        if item_type == "Grocery":
            receipt_item = GroceryItem(item, quantity, price)
        elif item_type == "Electronics":
            receipt_item = ElectronicsItem(item, quantity, price)
        else:
            # Default to Grocery item if the type is not recognized
            receipt_item = GroceryItem(item, quantity, price)

        self.receipt_items.append(receipt_item)

        self.item_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def print_receipt(self):
        self.receipt_text.delete('1.0', tk.END)

        self.receipt_text.insert(tk.END, "Receipt\n\n")
        self.receipt_text.insert(tk.END, "Item\tQuantity\tPrice\n")

        for receipt_item in self.receipt_items:
            self.receipt_text.insert(tk.END, receipt_item.get_details() + "\n")

        total_quantity = sum(receipt_item.quantity for receipt_item in self.receipt_items)
        total_price = sum(receipt_item.calculate_total() for receipt_item in self.receipt_items)
        self.receipt_text.insert(tk.END, "\n")
        self.receipt_text.insert(tk.END, f"Total Quantity: {total_quantity}\n")
        self.receipt_text.insert(tk.END, f"Total Price: ${total_price:.2f}\n")


root = tk.Tk()
receipt_app = ReceiptApp(root)
root.mainloop()

