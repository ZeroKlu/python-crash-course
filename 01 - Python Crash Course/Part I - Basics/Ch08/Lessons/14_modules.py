# We use the syntax 'import <<module>>' to import the functionality exposed in a module
#   where <<module>> is the filename without its extension
# This finds and imports a module from 'pizza.py'
import pizza

# The syntax above imports the entire module, exposing all its functions

print("Chapter 8:")
print("Exercise 12 - Importing a Module")

# When we call a function from the module, we use '<<module>>.<<function>>'
pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green pepper")
