print("Chapter 7:")
print("Exercise 3 - Using the Modulo Operator")

# The modulo [or modulus] operator (%) returns the remainder when dividing two numbers
# e.g.:  5 % 3 = 2, 6 % 3 = 0
numbers = [4, 5, 6, 7]
for number in numbers:
    print(f"{number} % 3 = {number % 3}")

# A common use of modulus is when you want to determine if a number is a multiple of another
# e.g.: Any multiple of 2 is an even number
number = int(input("\nEnter a number, and I will tell you if it is even or odd:\n> "))
if number % 2 == 0:
    condition = "even"
else:
    condition = "odd"
print(f"The number {number} is {condition}.")

# A fun exercise you can try is using modulo to determine if a number is prime
# - Definition of a prime number:
#    Any positive integer that has exactly two integer factors: 1 and itself
#    • Since 1 only has one factor (itself), it is the unit number, not a prime number
#    • All other non-prime positive integers are called composite numbers
#    • 0 as the identity number is neither positive nor negative, so it is also not a prime number
#
# Try to resist the urge to looking at my example until you give it a go yourself
# Think about efficiency as well as functionality
