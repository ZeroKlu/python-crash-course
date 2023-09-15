print("Chapter 4:")
print("Exercise 5 - List Comprehensions")

# A comprehension allows defining the content of a list based on an expression
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# An easy way to think of a list comprehension is a loop that computes an expression on each iteration
#   and automatically appends the result to the list

# The code above is equivalent to the following:
# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
# print(squares)
