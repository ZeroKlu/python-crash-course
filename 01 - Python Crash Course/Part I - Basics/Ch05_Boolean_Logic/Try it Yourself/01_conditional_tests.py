"""Assignment 5.1"""

# Conditional Tests: Write a series of conditional tests.
#                    Print a statement describing each test and your
#                    prediction for the results of each test.
#                    Your code should look something like this:
#                    -----------------------------------------
#                    car = "subaru"
#                    print("Is car == 'subaru'? I predict True.")
#                    print(car == "subaru")
#
#                    print("\nIs car == 'audi'? I predict False.")
#                    print(car == "audi")
#                    -----------------------------------------
#                    • Look closely at your results, and make sure you
#                      understand why each line evaluates to
#                      True or False.
#                    • Create at least ten tests.
#                      Have at least five tests evaluate to True and
#                      another five tests evaluate to False.

print("Try-it-Yourself:")
print("Assignment 5.1")

make = "Dodge"
model = "Challenger"
print("Is make == 'fiat'? I predict False.")
print(make == "fiat")
print("Is make == 'dodge'? I predict False.")
print(make == "dodge")
print("Is make == 'Dodge'? I predict True.")
print(make == "Dodge")
print("Is case-insensitive make == 'dodge'? I predict True.")
print(make.lower() == "dodge")

print("Is model == 'charger'? I predict False.")
print(model == "charger")
print("Is model != 'charger'? I predict True.")
print(model != "charger")
print("Is model == 'challenger'? I predict False.")
print(model == "challenger")
print("Is model == 'Challenger'? I predict True.")
print(model == "Challenger")
print("Is case-insensitive model == 'charger'? I predict False.")
print(model.lower() == "charger")
print("Is case-insensitive model == 'challenger'? I predict True.")
print(model.lower() == "challenger")
