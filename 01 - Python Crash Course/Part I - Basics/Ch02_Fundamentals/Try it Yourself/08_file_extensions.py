"""Assignment 2.8"""

# File Extensions: Python has a removesuffix() method that works exactly like removeprefix().
#                  Assign the value 'python_notes.txt' to a variable called filename.
#                  Then use the removesuffix() method to display the filename without the
#                  file extension, like some file browsers do.

# Note: This exercise only appears in the 3rd edition

print("Try-it-Yourself:")
print("Assignment 2.8")

filename = "python_notes.txt"
print(f"Filename without extension: {filename.removesuffix('.txt')}")
