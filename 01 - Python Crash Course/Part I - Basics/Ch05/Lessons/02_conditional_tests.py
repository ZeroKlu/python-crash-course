print("Chapter 5:")
print("Exercise 2 - Conditional Tests")

# The simplest test is for equivalency (==)
# Equivalency means that the values are equal.
car = "bmw"
print(f"'{car}' == 'bmw': {car == 'bmw'}")
print(f"'{car}' == 'audi': {car == 'audi'}")

# You can check case-insensitive equality in a string by forcing the operand to be in lower-case
car = "Audi"
print(f"'{car.lower()}' == 'audi': {car.lower() == 'audi'}")
print(f"'{car.upper()}' == 'AUDI': {car.upper() == 'AUDI'}")

# Since you have negation (!) available, you can also check for inequality
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

# Of course, you can apply the same comparisons to numbers
age = 18
print(f"{age} == 18: {age == 18}")
answer = 63
if answer != 42:
    print("That is not the correct answer. Please try again!")

# When working with numbers you have additional comparisons available
age = 21
# Less than (<)
print(f"{age} < 21: {age < 21}")
# Less than or equal (<=)
print(f"{age} <= 21: {age <= 21}")
# Greater than (>)
print(f"{age} > 21: {age > 21}")
# Greater than or equal (>=)
print(f"{age} >= 21: {age >= 21}")

# Note: Inequalities can also be used with non-numeric values
print(f"'abc' < 'def': {'abc' < 'def'}")
