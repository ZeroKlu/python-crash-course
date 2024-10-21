"""Example Comprehensions"""

from sm_utils import timer

@timer
def for_loop(n: int) -> list[int]:
    """Calculate the square of numbers from 0 to n using a for loop"""
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

@timer
def list_comprehension(n: int) -> list[int]:
    """Calculate the square of numbers from 0 to n using list comprehension"""
    return [i ** 2 for i in range(n)]

def main() -> None:
    """Run the program"""
    n = 10 ** 6
    print("Using for_loop...")
    for_loop(n)
    print("\nUsing list_comprehension...")
    list_comprehension(n)

if __name__ == "__main__":
    main()
