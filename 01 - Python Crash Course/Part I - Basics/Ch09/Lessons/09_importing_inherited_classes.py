# Note: We are only explicitly importing ElectricCar
from electric_car import ElectricCar

# Use the Classes
print("Chapter 9:")
print("Exercise 9 - Importing Inherited Classes")

my_nissan = ElectricCar("nissan", "leaf", 2024)

# Since ElectricCar is a subclass of Car, we get the properties of Car as well
print(my_nissan.get_descriptive_name())

# Since the battery attribute of ElectricCar is an instance of Battery, we get its properties too
my_nissan.battery.describe_battery()
my_nissan.battery.get_range()
