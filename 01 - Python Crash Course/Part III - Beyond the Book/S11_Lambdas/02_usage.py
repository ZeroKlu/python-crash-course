import dis
import traceback
from utility_functions import pause, clear_terminal

def higher_order_function(x: int, func: callable) -> int:
    """Returns `x` plus result of `func(x)`"""
    return x + func(x)

def add_function(x: int, y: int) -> int:
    """Add two numbers"""
    return x + y

def compare_bytecode() -> None:
    """Examine the bytecode generated by a function versus a lambda"""
    clear_terminal()
    
    print("\nAnalyzing add_function...")
    print(f"Type: {type(add_function)} ({add_function})")
    dis.dis(add_function)
    print()

    add_lambda = lambda x, y: x + y
    print("\nAnalyzing add_lambda...")
    print(f"Type: {type(add_lambda)} ({add_lambda})")
    dis.dis(add_lambda)
    print()

def divide_function(x: int, y: int) -> int:
    """Divide two numbers"""
    return x / y

def compare_errors() -> None:
    """Examine the errors generated by a function versus a lambda"""
    clear_terminal()

    x = 2
    y = 0

    try:
        print("\nError in function...")
        print(divide_function(x, y))
    except:
        print(traceback.format_exc())
    print("\n-----\n")

    divide_lambda = lambda x, y: x / y
    
    try:
        print("\nError in lambda...")
        print(divide_lambda(x, y))
    except:
        print(traceback.format_exc())
    print()

def main() -> None:
    clear_terminal()
    higher_order_lambda = lambda x, func: x + func(x)
    x = 2
    print("function:", higher_order_function(x, lambda y: y ** 2))
    print("lambda:", higher_order_lambda(x, lambda y: y ** 2))
    pause()

    compare_bytecode()
    pause()
    
    compare_errors()

if __name__ == "__main__":
    main()
