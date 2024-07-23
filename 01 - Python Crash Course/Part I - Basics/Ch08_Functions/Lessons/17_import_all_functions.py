# A wild-card '*' will import all of the functions from a module
from pizza import *

print("Chapter 8:")
print("Exercise 15 - Importing All Functions from a Module")

# Because we've imported the actual functions, we do not need to precede them with the module name
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green pepper")
