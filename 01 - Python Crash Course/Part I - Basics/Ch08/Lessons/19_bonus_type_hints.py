print("Chapter 8:")
print("Exercise 19 - Bonus Lesson - Type Hints")

# To best communicate the intent of a function, it is useful to be able to provide another developer
#   who may be working with your code with hints as to the expected data types for parameters.

# We can do this by providing type hints for our function parameters like this:
#       def my_function(arg_1: type_1, arg_2: type_2, ...)

# We can also provide a hint for the return type of the function like this:
#       def my_function(...) -> return_type:

# This will become especially useful when we start packaging our functions in modules

# Here, I am type-hinting the float type for my numbers (because float implicitly includes integer types)

def calculate(operation: str, x: float, y: float) -> float:
    """Perform basic arithmetic calculation"""
    op = operation[0].lower()
    if op == "a":
        # add
        return x + y
    elif op == "s":
        # subtract
        return x - y
    elif op == "m":
        # multiply
        return x * y
    elif op == "d":
        # divide
        return x / y
    else:
        print(f"Operation [{operation}] not supported!")
        return None

# In Python 3.10+ we can specify multiple acceptable types using bitwise OR (|)

def calc(operation: str, x: int | float, y: int | float) -> int | float:
    """Perform basic arithmetic calculation"""
    return calculate(operation, x, y)

x = 3
y = 2
print(f"{x} + {y} = {calculate('add', x, y)}")
print(f"{x} - {y} = {calculate('subtract', x, y)}")
print(f"{x} * {y} = {calculate('multiply', x, y)}")
print(f"{x} / {y} = {calc('divide', x, y)}")
print(f"{x} to the {y} power = {calc('power', x, y)}")

# Hover the mouse over any instance of calculate() or calc() to see a clear description of the hinted data types
# Keep in mind, this does not enforce these types. It just provides the developer guidance in using the function.
