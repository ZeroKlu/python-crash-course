print("Chapter 4:")
print("Exercise 8 - Tuples")

# In Python, a "tuple" is simply an immutable list (Note: The syntax uses parentheses instead of square-brackets)
dimensions = (200, 50)
print(f"Dimensions: {dimensions[0]} x {dimensions[1]}")

# The line below would produce an error, since you cannot change the values of a tuple
# dimensions[0] = 250

# Some people will use a single-element tuple as a quasi-constant. Since the comma in the syntax is what symbolizes
#   a tuple, you need to add one, even though there is no second number.
three = (3,)

# Of course, you can loop over a tuple, just like a list
for dim in dimensions: print(dim)

# Unlike an actual constant, you can reassign a new value to the entire tuple, just not its components
print("Original dimensions:")
for dim in dimensions: print(dim)
dimensions = (250, 50)
print("Modified dimensions:")
for dim in dimensions: print(dim)

# You can produce a list of tuples using the zip() function
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
tuples = zip(letters, numbers)
print(list(tuples))
