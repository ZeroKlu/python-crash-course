# Chapter Notes
#region
# >>> import this
# Will display "The Zen of Python" by Tim Peters
#
# Note: Any line staring with "#" + a whitespace character is a comment
#
# Variable naming notes
#
# Rules:
# Only use ASCII characters
# May contain letters, numbers, and underscores
# May not start with a number
# May not contain spaces
# Should not use Python reserved words
# Avoid "l" and "O" which may be mistaken for "1" and "0"
# Except where specifically recommended, avoid upper-case letters
#
# Conventions:
# snake_case
# - modules and packages
# - variables
# - method/function names
#
# PascalCase
# - class names
# - type variables
# - exceptions (also append "Error")
#
# ALL_CAP_SNAKE_CASE
# - "constants" *Python doesn't have constants, so this is just a convention to tell the programmer not to modify it
#
# camelCase
# - Not used in Python standards
#
# kebab-case
# - Not used in Python standards
#endregion

print("Chapter 2:")
print("Exercise 1 - Use a variable in 'Hello World'")

# In Python, we don't need to separately declare a variable before we assign a value
message = "Hello Python World"
print(message)
# You can replace a variable by assigning another value
message = "Hello Python Crash Course"
print(message)