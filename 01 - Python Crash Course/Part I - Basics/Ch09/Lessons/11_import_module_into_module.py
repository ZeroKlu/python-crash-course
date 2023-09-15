import electric_car

# Use the Classes
print("Chapter 9:")
print("Exercise 11 - Importing Module that Imports Another Module")

my_nissan = electric_car.ElectricCar("nissan", "leaf", 2024)
# We have the attributes of Car (as the inherited parent class of ElectricCar)
print(my_nissan.get_descriptive_name())

# But, because we have not actually imported the Car class, we cannot do this...
# my_beetle = Car("volkswagen", "beetle", 2019)
# print(my_beetle.get_descriptive_name())
