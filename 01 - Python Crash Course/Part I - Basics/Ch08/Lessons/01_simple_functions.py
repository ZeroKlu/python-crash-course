print("Chapter 8:")
print("Exercise 1 - Simple Functions")

# Up to this point, we have written code line-by-line whenever it was needed
# Adding functions to our code allows us to avoid writing similar code over and over
# Avoiding redundant code is one of the primary goals of a programmer

# You define a function using the "def" keyword
# Note: When defined in a script, the function must be defined before the code that calls it
def greet_user():
    # Typically, when we write a function, we include a documentation (or 'doc') string
    """Display a simple greeting"""
    # Code indented after the function definition is executed only when the function is called
    print("\nHello!")

# Calling a function only requires an instruction containing its name
greet_user()
