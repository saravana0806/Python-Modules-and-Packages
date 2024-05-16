# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:42:52 2024

@author: HP
"""


# Modules

import os
os.chdir(r'C:\Users\HP\Downloads\Python-Modules-and-Packages-main\Python-Modules-and-Packages-main')

import modules

print(modules.average([1,2,3]))
print(modules.add(1,2))

###################


# my_package.py
import my_package

print(my_package.add(1,2))
print(my_package.multiply(3, 5))






# Class

class Calculator:

    def add(num1, num2):
        return num1 + num2

    def subtract( num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def divide( num1, num2):
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return num1 / num2

Calculator.add(3,4)
Calculator.subtract(3,4)
Calculator.multiply(3,4)
Calculator.divide(3,0)




###############################

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return name,"Woof!"

    def info(self):
        return f"{self.name} is {self.age} years old."

new_dog = Dog('Roy',2)

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # Output: Buddy
print(dog1.age)
print(dog2.name)
print(dog2.age)
print(dog2.info())  # Output: Max is 5 years old.
print(dog1.bark())  # Output: Woof!
print(dog2.bark())  # Output: Woof!





####################################


class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. Current balance: {self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn {amount}. Current balance: {self.balance}"
        else:
            return "Insufficient funds."

    def check_balance(self):
        return f"Current balance: {self.balance}"

account = BankAccount(100)

print(account.deposit(50))  # Output: Deposited 50. Current balance: 150

print(account.withdraw(30))  # Output: Withdrawn 30. Current balance: 120

print(account.check_balance())  # Output: Current balance: 120






# Packages


#my_package/
#    __init__.py
#    module1.py
#    module2.py


import os
os.chdir(r'C:\Users\HP\Downloads\Python-Modules-and-Packages-main\Python-Modules-and-Packages-main')

from my_package import add, multiply
add(7,0)

import my_package
my_package.add(6,9)


# Test the functions
result_add = add(5, 3)
result_multiply = multiply(2, 6)

# Display the results
print("Addition:", result_add)
print("Multiplication:", result_multiply)



