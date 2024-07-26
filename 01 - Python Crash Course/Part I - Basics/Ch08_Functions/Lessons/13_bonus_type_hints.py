print("Chapter 8:")
print("Exercise 19 - Bonus Lesson - Type Hints")

def calculate(operation: str, x: int|float, y: int|float) -> int|float:
    """
    Perform selected arithmetic calculation

    Parameters:  
    **operation**: Arithmetic operation to perform on the provided operands
    * [a]dd
    * [s]ubtract
    * [m]ultiply
    * [d]ivide  

    **x**: Left numerical operand  
    **y**: Right numerical operand

    **Returns**:  
    the result of the arithmetic operation
    """
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

x = 3
y = 2
print(f"{x} + {y} = {calculate('add', x, y)}")
print(f"{x} - {y} = {calculate('subtract', x, y)}")
print(f"{x} * {y} = {calculate('multiply', x, y)}")
