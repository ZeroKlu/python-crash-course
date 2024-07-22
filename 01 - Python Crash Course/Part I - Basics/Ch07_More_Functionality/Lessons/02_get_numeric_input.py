print("Chapter 7:")
print("Exercise 2 - Get Numeric Input")

# Even if a user enters a number, the result from the input() function is a string.
# Try the next two lines in the Python terminal
# age = input("How old are you?\n> ")
# age
# age >= 18

# Using int(), we can force that input to be treated as a number
age = input("How old are you?\n> ")
# Note: In a real-world scenario, you might want to use a try/except block here
#       to handle the possibility of the user entering invalid input
age = int(age)
print(age >= 18)

# You can include the int() casting function on the same line as the input
height = int(input("\nHow tall are you in inches?\n> "))
if height >= 48:
    print("You're tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older...")
