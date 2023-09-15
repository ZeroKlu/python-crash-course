print("Chapter 5:")
print("Exercise 5 - Using 'if' Statements")

age = 19
# We looked at an example of an "if" block at the beginning of the chapter
if (age >= 18):
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
# We also looked at an "else" block containing instructions for when the condition is False
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 12
# We can also chain together additional conditions using "elif" ("else" + "if")
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")

# A smart way to handle this would be to only print after all conditions are evaluated
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}")

# You can chain as many "elif" conditions as you want
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}")

# Even with "elif" blocks, the "else" block is not required
#
# A standard coding pattern that doesn't use an "else" block looks like
# some_variable = default_value
# if condition_1 : some_variable = value_1
# elif condition_2 : some_variable = value_2
# ...
# elif condition_n : some_variable = value_n
#
# At the end, if no conditions are met the variable still contains the original default value
price = 20
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
print(f"Your admission cost is ${price}\n")

# When you need to check another condition regardless of the first result, use another "if", not "elif"
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms...")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni...")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese...")
print("Finished making your pizza!")

# An interesting note is that you can use 'else' at the end of a loop to include code that runs when the
#   condition becomes False
print()
i = 0
while i < 10:
    i += 1
    print(i)
else:
    print("If this ran, i must be 10 or more.")
