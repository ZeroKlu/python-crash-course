"""Assignment 9.10"""

# Imported Restaurant: Using your latest `Restaurant` class, store it
#                      in a module. Make a separate file that imports
#                      `Restaurant`. Make a `Restaurant` instance, and
#                      call one of `Restaurant`'s methods to show that
#                      the import statement is working properly.

from restaurant import Restaurant

print("Try-it-Yourself:")
print("Assignment 9.10")

my_restaurant = Restaurant("my place", "scottish food")
my_restaurant.describe()
