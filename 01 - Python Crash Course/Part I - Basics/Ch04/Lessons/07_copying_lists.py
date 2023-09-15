print("Chapter 4:")
print("Exercise 7 - Copying Lists")

# Omitting both arguments in a list slice creates a copy from both ends
my_foods = ["pizza", "falafel", "carrot cake"]
print(f"My favorite foods are:          {my_foods}")
# Here, we're omitting both ends of the slice to copy the entire list
friend_foods = my_foods[:]
print(f"My friend's favorite foods are: {friend_foods}")

# The copies are not tied to each other
my_foods.append("cannoli")
friend_foods.append("ice cream")
print(f"My favorite foods are:          {my_foods}")
print(f"My friend's favorite foods are: {friend_foods}")

# Assigning a list to another variable does not make a copy
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods
my_foods.append("cannoli")
friend_foods.append("ice cream")
# Because no copy was made, these lines affect both variables (they refer to the same list)
print(f"My favorite foods are:          {my_foods}")
print(f"My friend's favorite foods are: {friend_foods}")
