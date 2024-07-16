print("Chapter 4:")
print("Exercise 5 - List Comprehensions")

# Up to now, we have used loops to populate lists.
# For example, this will generate a list of the first 10 squares
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# An easy way to think of a list comprehension is a loop that computes an expression on each iteration
#   and automatically appends the result to the list

# A comprehension allows defining the content of a list based on an expression, simplifying the loop
# Takes the form [expression_on_var for var in collection]
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# You can also add a condition to a list comprehension to filter the results
# Takes the form [expression_on_var for var in collection if condition]
even_squares = [value ** 2 for value in range(1, 11) if value % 2 == 0]
print(even_squares)
