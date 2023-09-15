print("Chapter 4:")
print("Exercise 3 - Numeric Lists")

# The "range" function allows you to access a sequential, numeric list without declaring it as a variable
# Note: The second value must be one after the last value you want to process ("off-by-one" behavior)
for value in range(1, 6):
    print(value)

# Of course, you could assign the range to a list variable
nums = []
for i in range(1, 6):
    nums.append(i)
print(nums)

# Or do the same thing using the list() function
numbers = list(range(1, 6))
print(numbers)

# Although repetitive, you could also use multiple assignment
one, two, three = list(range(1, 4))
print(f"{one} - {two} - {three}\n")

# You can also specify the interval that each value increments
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Leveraging a loop, you can create lists with other relationships
# For example, this one will list the first five squares
squares = []
for value in range(1, 6):
    squares.append(value ** 2)
print(squares)
