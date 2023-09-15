# Here, we're importing a class stored as a module
from car import Car

# Use the Classes
print("Chapter 9:")
print("Exercise 8 - Importing a Class")

my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
