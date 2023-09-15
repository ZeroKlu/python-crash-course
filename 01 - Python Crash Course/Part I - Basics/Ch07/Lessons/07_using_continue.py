print("Chapter 7:")
print("Exercise 7 - Using Continue")

# The "continue" command immediately ends the current iteration of the loop
# - The remainder of the current iteration does not execute
# - But the loop itself continues with the next iteration

current_number = 0

# Printing just the odd numbers
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        # We're using "continue" to skip even numbers but continue the loop
        continue    
    print(current_number)
