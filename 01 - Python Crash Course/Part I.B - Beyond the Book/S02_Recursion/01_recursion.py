import fibonacci_functions as fib

def print_menu() -> None:
    """Display the menu of algorithm options"""
    print("\nEnter one of the following options:")
    print("[R]ecursive Algorithm")
    print("[M]emoized Recursive Algorithm")
    print("[I]terative Algorithm")
    print("[F]ormula-Based Algorithm")
    print("[Q]uit")

def main() -> None:
    options = ["r", "m", "i", "f", "q"]

    while True:
        n = -1
        print_menu()
        option = ""
        option = input("\n> ")[:1].lower()
        if option not in options:
            print("Please enter a valid value!")
            continue
        else:
            while n < 0 and option != "q":
                try:
                    n = int(input("Enter a non-negative integer:\n> "))
                except:
                    continue
        if option == "r":
            # Call naive recursive function
            print(f"\nF({n}) = {fib.fibonacci_recursive(n):,}")
            print(f"Recursive calculation required {fib.fibonacci_recursive.call_count:,} function calls.")
        elif option == "m":
            # Call recursive function with memoization
            print(f"\nF({n}) = {fib.fibonacci_recursive_memo(n):,}")
            print(f"Cached recursive calculation required {fib.fibonacci_recursive_memo.call_count:,} function calls.")
        elif option == "i":
            # Call iterative function
            print(f"\nF({n}) = {fib.fibonacci_iterative(n):,}")
            suffix = "s"
            if fib.fibonacci_iterative.call_count == 1:
                suffix = ""
            print(f"Iterative calculation required {fib.fibonacci_iterative.call_count:,} function call{suffix}.")
        elif option == "f":    
            # Call formulaic function
            print(f"\nF({n}) = {fib.fibonacci_formulaic(n):,}")
            suffix = "s"
            if fib.fibonacci_formulaic.call_count == 1:
                suffix = ""
            print(f"Formula-based calculation required {fib.fibonacci_formulaic.call_count:,} function call{suffix}.")
        else:
            break

if __name__ == "__main__":
    main()
