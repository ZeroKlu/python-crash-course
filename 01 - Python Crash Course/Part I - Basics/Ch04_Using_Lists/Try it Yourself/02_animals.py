"""Assignment 4.2"""

# Animals: Think of at least three different animals that have
#          a common characteristic. Store the names of these
#          animals in a list, and then use a for loop to print
#          out the name of each animal.
# • Modify your program to print a statement about each animal,
#   such as "A dog would make a great pet."
# • Add a line at the end of your program stating what these animals
#   have in common. You could print a sentence such as:
#   "Any of these animals would make a great pet!"

from random import choice

print("Try-it-Yourself:")
print("Assignment 4.2")

animals = ["octopus", "squid", "cuttlefish"]
verbs = ["eat", "devour", "dine on"]
for animal in animals:
    print(f"I like to {choice(verbs)} {animal}.")
print("You have to be very careful cooking any of these animals.")
