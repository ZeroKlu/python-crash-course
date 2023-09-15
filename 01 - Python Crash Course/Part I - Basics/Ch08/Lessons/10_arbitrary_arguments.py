print("Chapter 8:")
print("Exercise 10 - Passing an Arbitrary Amount of Arguments")

# An asterisk preceding the last parameter name indicates that an arbitrary number of values can be passed.
# These values will be received a list
def make_pizza_simple(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Of course, this can be preceded by non-arbitrary arguments as well
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def pause():
    """Wait for user to press <ENTER>"""
    input("\nPress <ENTER> to continue\n")

make_pizza_simple("pepperoni")
make_pizza_simple("mushrooms", "green peppers", "extra cheese")

pause()
    
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")
