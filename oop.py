"""
oop 
classes
objects
encapslation
polymorthism
inheritence
"""


"""class Student:
 def __init__(self, name, year, course):
    self.name = name
    self.year = year
    self.course = course

 def display(self):
      print('NAME', self.name)
      print('YEAR',self.year)
      print('COURSE',self.course)


p1 = Student("John", 3, "bse")
p1.display()"""


# example 2
"""class Person:
    def __init__(self, name, age):
       self.name= name
       self.age = age
    def greet(self):
        print("good morning",self.name)
        print("i am ",self.age,"years")
        p2= Person("cy" ,23)
        p2.greet()"""

# exercise 2
class employee:
  def __init__(self, name, salaray):
      self.name=name
      self.salaray=salaray
  def bonus(self):
      return self. salaray* 0.15
  def display(self):
      print("Name",self.name)
      print("salaray",self.salaray)
      print("bonus",self.bonus())

      empy=employee("cynthia" , 150000)
      employ2=employee("jelly" , 2000000)
      empy.display()
      employ2.display()

# encapsulation

# goals of encapsulation
"""
to hide implementation details
code organisation
"""
"""class bankAccount:
    def __init__(self, account_number,balance):
        self.acount_number=account_number
        self.balance= balance
    def depost(self , amount):
      self.balance >=amount
   def withdraw(self , amount):
       if self.balance>=amount:
           self.balance -= amount
    else:
     print("insufficient")
    def get_balance(self):
       return self.balance
  my = bankAccount("1235",1000)
print(my . account_number)
print(my.balance)
my.depost(300)
print(my.balance)
my.withdraw(200)
print(my.balance)"""




"""class temp:
    def __int__(self ,celcius):
        self.celcius= celcius
    def change_temp(self):
        return (self.celcius * 9/5 ) + 32
  my_tep=temp(37)

print(my_tep.change_temp)"""

