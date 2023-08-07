name=['Joan','Jon','Jelly','Cindy','Julie']
name[0] = "Jude"
print(name)
# add an item
name.append("John")
print(name)
name[2]="Bethel"
index_to_remove = 4
del name[index_to_remove]
print(name)
print(name[-1])
# no 7
fruits=[ 'mango','orange','apple','chill','berry','tomato','mellon']
print(fruits[2:4])
# list of countries
countries = ["USA", "Canada", "France", "Germany", "Japan"]

# Make a copy of the list
countries_copy = countries.copy()

# Loop through the copied list
print("Looping through the copied list:")
for country in countries_copy:
 print(country)
animals=['dogs','cat','cow','rabbit','rat','alligator']
animals.sort()
print(animals)
animals.sort(reverse=True)
a_animals = [x for x in animals if x.startswith('a')]

print("Animal names starting with 'a':")
for x in a_animals:
    print(x)
# joining lists
fname = ['cynthia']
lname = ['musiimenta']
fname.extend(lname)
joined_list = lname
print(joined_list)

# TUPLES
x=("samsung","iphone","techno","redmi")
favourate = x[2]
print(favourate)
second_last_item = x[-2]
print(second_last_item)
my_list = list(x)  # Convert the tuple to a list

# Update the specific item at index 2
my_list[1] = "itel"

updated_tuple = tuple(my_list)  # Convert the list back to a tuple
print(updated_tuple)
new_item = "Huawei"

# Create a new tuple with the additional item
new_phone = x + (new_item,)

print(new_phone)
for item in x:
    print(item)
    new_x= x[1:]

    print(new_x)

    cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])

    print(cities)
    cities = ('Kampala', 'Entebbe', 'Jinja', 'Mbarara', 'Gulu')

    # Unpack the tuple
    city1, city2, city3, city4, city5 = cities

    # Print the unpacked variables
    print(city1)
    print(city2)
    print(city3)
    print(city4)
    print(city5)
    cities = ('Kampala', 'Entebbe', 'Jinja', 'Mbarara', 'Gulu')

    # Print the second, third, and fourth cities using a range of indexes
    y= cities[1:4]

    print(y)
    first_name = ("cynthia",)
    last_name = ("musiimenta",)

    full_name = first_name + last_name
    print(full_name)
colors = ("red", "blue", "green")

multiplied_colors = colors * 3
print(multiplied_colors)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

count = thistuple.count(8)
print("The number of times 8 appears in the tuple:", count)



# exercise 3

best_drinks = {"Coffee", "Matcha", "Mango Lassi"}

print(best_drinks)
best_drinks.update(["Iced Tea", "Smoothie"])
print(best_drinks)
myset = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in myset:
    print("Yes, 'microwave' is in the set.")
else:
    print("No, 'microwave' is not in the set.")
for item in myset:
 print(item)

# Using the remove() method
myset.remove("kettle")
print(myset)

# Using the discard() method
myset.discard("kettle")
print(myset)
# joining the set to a list
myset = {1, 2, 3, 4}
mylist = [5, 6]

result = myset.union(mylist)
print(result)
age = {25}
first_name = {"Cynthia"}

combined_set = age.union(first_name)
print(combined_set)


# STRINGS
string_var = "Hello, "
integer_var = 42

mum = string_var + str(integer_var)
print(mum)
txt = " Hello, Uganda! "

# Remove spaces in the middle
txt = txt.replace(" ", "")

# Remove spaces at the end
txt = txt.rstrip()
# convert to upper case

txt = txt.upper()
print(txt)
txt = txt.replace('U', 'V')

print(txt)
x = 'All "Data scientists" are cool!'
print(x)


# DICTIONARIES
shoes = {
    "Brand": "Nick",
    "color": "Black",
    "size": 40
}

shoes_size = shoes["size"]
print("Shoes Size:", shoes_size)


shoes["Brand"] = "Adidas"

print(shoes)


shoes["type"] = "sneaker"

print(shoes)

keys_list = list(shoes.keys())
print(keys_list)


values_list = list(shoes.values())
print(values_list)

if "size" in shoes:
    print("Key 'size' exists in the dictionary")
else:
    print("Key 'size' does not exist in the dictionary")

    for key, value in shoes.items():
     print(key, ":", value)

     shoes = {
         "Brand": "Nick",
         "color": "Black",
         "size": 40,
         "type": "sneaker"
     }

     del shoes["color"]

     print(shoes)

    shoes.clear()

    print(shoes)
    # Original dictionary
    original_dict = {
        "name": "Cynthia",
        "age": 30,
        "city": "Kampala"
    }


    copied_dict = original_dict.copy()

    # Modifying the copied dictionary
    copied_dict["age"] = 35

    # Printing both dictionaries
    print("Original Dictionary:", original_dict)
    print("Copied Dictionary:", copied_dict)
# NESTED DICTIONARIES
# Creating nested dictionaries
student1 = {
    "name": "John",
    "age": 20,
    "grades": {
        "math": 90,
        "science": 85,
        "history": 95
    }
}

student2 = {
    "name": "Emily",
    "age": 19,
    "grades": {
        "math": 95,
        "science": 92,
        "history": 88
    }
}

# Outputting nested dictionaries
print("Student 1:")
print("Name:", student1["name"])
print("Age:", student1["age"])
print("Grades:", student1["grades"])

print("\nStudent 2:")
print("Name:", student2["name"])
print("Age:", student2["age"])
print("Grades:", student2["grades"])

















