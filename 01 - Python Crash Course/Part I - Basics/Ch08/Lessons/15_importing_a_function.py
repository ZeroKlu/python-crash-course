# To import only specific functions from a module, the syntax is as follows:
#   from <<module>> import <<function>>
from pizza import make_pizza

print("Chapter 8:")
print("Exercise 13 - Importing a Function from a Module")

# Because we've imported the actual function, we do not need to precede it with the module name
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green pepper")

# Note, you can import multiple functions like this:
#       from <<module>> import <<function_1>>, <<function_2>>, ...
