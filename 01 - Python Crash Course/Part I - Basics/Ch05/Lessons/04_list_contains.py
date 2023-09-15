print("Chapter 5:")
print("Exercise 4 - Check if List Contains Value")

# The "in" condition evaluates a value to see if a list contains it
requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings)
print("pepperoni" in requested_toppings)

# With "in" we use the "not" keyword instead of negation (!)
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# You can explicitly set variables to boolean values for use in conditions
game_active = True
can_edit = False
print(f"Game Active: {game_active}")
print(f"Can Edit: {can_edit}")
