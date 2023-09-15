print("Chapter 6:")
print("Exercise 1 - Simple Dictionaries")

# In Python, a dictionary (in some languages a hashtable) is a collection of key/value pairs
#    instead of just values
# You can think of this as an object with properties but without a defined class
# The syntax is very similar to JavaScript/JSON objects using key : value throughout
# Dictionaries are denoted by curly-braces instead of square-brackets

# Syntax:   {key_1: value_1, key_2: value_2, ..., key_n: value_n}

# Keys must be unique within a dictionary
alien_0 = {"color" : "green", "points" : 5}

# You access a given value by specifying its key instead of an index
print(alien_0["color"])
print(alien_0["points"])

print()

# Of course, like lists, you can create dictionaries using comprehensions
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)
