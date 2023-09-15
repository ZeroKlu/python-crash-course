print("Chapter 7:")
print("Exercise 4 - Using 'while' Loops")

# Syntax:
# while come_condition:
#     code_to_execute

# A while loop does not require an incrementing value or range.
# It executes as long as the condition is true
current_number = 1
while current_number <= 5:
    print(current_number)
    # Be careful not to accidentally create an infinite loop
    # If you don't provide a path where the condition becomes False, your loop will never end
    # Here, we are incrementing current_number so that it will eventually make the condition <= 5 False
    current_number += 1
    # If we omitted that line, the loop would just print the number 1 forever

print()

# Of course, the condition does not have to be numeric
prompt = "\nTell me something and I will repeat it back to you:\n> "
message = ""
while message.lower() != "quit":
    # The loop will execute as long as the user enters something other than "quit"
    message = input(prompt)
    if message.lower() != "quit":
        print(message)

print()

# You may recall, way back in Lesson 04.01, we discussed the problem with modifying
#   an object we're looping across
# With a while loop, since we are no longer iterating across the list, but instead checking
#   a condition, we can accomplish what we were trying to do in that loop
numbers = [1, 2, 3, 4, 5]
# Remember that an empty list is False for conditional logic
while numbers:
    n = numbers.pop(0)
    print(n)
# Now, numbers is empty, but we processed all the values without skipping
print(numbers)

# As your code becomes more complex, it will be more difficult to detect infinite loops
# When testing, if you create an infinite loop, enter Ctrl+C in the terminal to stop your program
