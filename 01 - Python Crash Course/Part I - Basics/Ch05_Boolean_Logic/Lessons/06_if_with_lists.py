print("Chapter 5:")
print("Exercise 6 - Using 'if' with Lists")

# Using a list reduces the need to create redundant if statements
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    print( f"Adding {requested_topping}.")
print("Finished making your pizza!\n")

# Handling special values is also easier when using lists
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print( f"Adding {requested_topping}.")
print("Finished making your pizza!\n")

# You can further refine this by using two lists
out_of_stock = ["green peppers", "anchovies"]
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in out_of_stock:
        print(f"Sorry, we are out of {requested_topping} right now.")
    else:
        print( f"Adding {requested_topping}.")
print("Finished making your pizza!")

# You can check easily for an empty list
# This is a really important concept. An empty list is False in Boolean logic
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print( f"Adding {requested_topping}.")
    print("Finished making your pizza!\n")
else:
    print("\nAre you sure you want a plain pizza?\n")

# Frequently, you'll want to compare values against multiple lists
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
out_of_stock = ["green peppers", "mushrooms"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        if requested_topping in out_of_stock:
            print(f"Sorry. We're out of {requested_topping}")
        else:
            print( f"Adding {requested_topping}.")
    else:
        print( f" Sorry, we don't have {requested_topping}.")
print("Finished making your pizza!")
