# Notes: The Python Standard Library (PSL) is a set of modules included with every Python installation.
#        Using the skills from this chapter, we can import and use these ready-made modules

# Import the random integer and choice functions from the 'random' module in the PSL
from random import randint, choice

print("Chapter 9:")
print("Exercise 11 - Importing Random from the Python Standard Library")

dice = [randint(1, 6), randint(1, 6)]
print (f"\nYou rolled {dice}\n")

players = ["charles", "martina", "michael", "florence", "eli"]
first_up = choice(players)
print(f"First Up: {first_up.title()}\n")
