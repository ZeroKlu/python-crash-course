# The 'as' keyword allows us to create aliases for modules or functions we import
import pizza as p
from pizza import make_pizza as mp

print("Chapter 8:")
print("Exercise 14 - Using an Alias for an Import")

# Call a function in the aliased module
p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushrooms", "green pepper")

# Call the aliased function
mp(16, "pepperoni")
mp(12, "mushrooms", "green pepper")
