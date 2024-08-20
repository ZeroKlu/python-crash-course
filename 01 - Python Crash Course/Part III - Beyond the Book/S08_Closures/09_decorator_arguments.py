def power(exp: int) -> callable:
    """Generates a decorator (applying a non-local value for the exponent)"""
    def _power(func: callable) -> callable:
        """Calls the inner function, passing the function to execute"""
        def _inner_power(*args: list[int]) -> int:
            """Executes the called function, modifying its value n to be n ** exp"""
            base = func(*args)
            return base ** exp
        return _inner_power
    return _power

@power(2)
def square(n: int) -> int:
    """Square an integer (using a decorator function)"""
    return n

@power(3)
def cube(n: int) -> int:
    """Cube an integer (using a decorator function)"""
    return n

def main() -> None:
    for n in range(1, 6):
        print(f"{n}² = {square(n):>2} : {n}³ = {cube(n):>3}")

if __name__ == "__main__":
    main()
