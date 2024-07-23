print("Chapter 8:")
print("Exercise 2 - Function Arguments and Parameters")

# You can define parameters that can be passed to the function
def greet_named_user(name):
    """Print a greeting to the user passed to the function"""
    print(f"\nHello, {name.title()}")

# A parameter can be a list, not just a single variable
def greet_users(names):
    """Print a greeting to each of the users passed to the function"""
    for name in names:
        msg = f"\nHello, {name.title()}!"
        print(msg)

# You can pass arguments to a function
name = "abe"
greet_named_user(name)

# An argument can be a list, not just a single variable
usernames = ["hannah", "ty", "margot"]
greet_users(usernames)
