print("Chapter 8:")
print("Exercise 7 - Executing a Function in a Loop")

# Calling a function in a loop is a very common way of reusing code

def square(n):
    """Return the square of the integer passed"""
    return n ** 2

# Print out the squares of integers 1 through 5
for n in range(1, 6):
    print(f"{n}² = {square(n)}")

def get_formatted_name(first_name, last_name, middle_name = ""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# Note: This is an infinite loop (until the user breaks it using "q")!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
