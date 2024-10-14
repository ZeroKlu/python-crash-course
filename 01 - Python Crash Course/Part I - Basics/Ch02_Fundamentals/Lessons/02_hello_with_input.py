"""Chapter 2: Lesson 2"""

print("Chapter 2:")
print("Exercise 2 - Populate a variable from user input")

name = input("Please enter your name: ")

# f-strings (formatted strings) are the equivalent to string-interpolation
# (available in 3.6+)
message = f"Hello {name}"
print(message)

# In older versions, you would need to use this syntax:
message = "Hello {0}".format(name)
print(message)
