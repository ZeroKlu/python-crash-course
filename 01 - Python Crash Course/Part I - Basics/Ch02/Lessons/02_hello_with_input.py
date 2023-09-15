print("Chapter 2:")
print("Exercise 2 - Populate a variable from user input")

name = input("Please enter your name: ")
# f-strings (formatted strings) are the equivalent string-interpolation (available in 3.6+)
message = f"Hello {name}"
# In older versions, you would need to use this syntax:
# message = "Hello {0}".format(name)
print(message)
