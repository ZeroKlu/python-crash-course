import sys

def recursion_overflow() -> None:
    """Demonstrates exceeding max recursion depth"""
    x = 1
    recursion_overflow()

def main() -> None:
    print(f"Max recursion depth: {sys.getrecursionlimit()}")
    recursion_overflow()

if __name__ == "__main__":
    main()
