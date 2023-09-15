# We are importing both Car and ElectricCar
# When importing multiple classes from a module, separate them with commas
from full_car import Car, ElectricCar

# Note: We could import the entire module
# import full_car
#       or we could import all the classes from the module
# from full_car import *

# Use the Classes
print("Chapter 9:")
print("Exercise 10 - Importing Multiple Classes")

my_beetle = Car("volkswagen", "beetle", 2019)
print(my_beetle.get_descriptive_name())

my_nissan = ElectricCar("nissan", "leaf", 2024)
print(my_nissan.get_descriptive_name())
