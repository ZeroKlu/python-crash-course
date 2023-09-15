# Like a module, we can import a class with an alias
from electric_car import ElectricCar as EC

# Use the Classes
print("Chapter 9:")
print("Exercise 12 - Using an Alias for an Imported Class")

# We then use the alias to create instances of the class
my_nissan = EC("nissan", "leaf", 2024)
print(my_nissan.get_descriptive_name())
