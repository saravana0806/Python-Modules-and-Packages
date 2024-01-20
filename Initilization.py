# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 20:02:02 2024

@author: HP
"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model}'s engine is now running.")

my_car = Car(make="Toyota", model="Camry", year=2022)

print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")
print(f"Is Running: {my_car.is_running}")

my_car.start_engine()
print(f"After starting the engine, is_running: {my_car.is_running}")





class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_object = MyClass("John", 25)

print("Name:", my_object.name)
print("Age:", my_object.age)






class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = MyClass("Alice", 30)
person2 = MyClass("Bob", 25)
person3 = MyClass("Charlie", 35)

print("Person 1 - Name:", person1.name, "Age:", person1.age)
print("Person 2 - Name:", person2.name, "Age:", person2.age)
print("Person 3 - Name:", person3.name, "Age:", person3.age)






class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

person = Person("Ramu", 30)

print(f"{person.name} is {person.age} years old.")
person.celebrate_birthday()







class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

person = MyClass("John", 28)
person.greet()

person1 = MyClass("John", 28)
person1.age = 31
print("Updated Age of Person 1:", person1.age)







class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = [] 

    def add_friend(self, friend):
        self.friends.append(friend)
        
    def print_friends(self):
        print(f"Friends of {self.name}:")
        for friend in self.friends:
            print(f"- {friend.name}")    

person1 = Person("Ram", 30)
person2 = Person("sham", 25)

person1.add_friend(person3)

person1.print_friends()






class Calculator:
    def __init__(self, initial_value=0):
        self.result = initial_value

    def add(self, value):
        self.result += value

    def subtract(self, value):
        self.result -= value

    def get_result(self):
        return self.result

calc = Calculator()
result = calc.get_result()
print("Initial Result:", result)

calc.add(5)
calc.subtract(2)

result = calc.get_result()

print("Final Result:", result)




