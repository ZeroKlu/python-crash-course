def throw(ex: Exception) -> None:
    """Raise an exception"""
    raise ex

def throw_from_lambda() -> None:
    """Raise an exception"""
    try:
        (lambda: throw(Exception("\nCaught an error!\n")))()
    except Exception as ex:
        print(ex)

def cryptic_lambda() -> None:
    """Execute a lambda that is hard to read"""
    print((lambda _: list(map(lambda _: _ // 2, _)))([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "\n")

def readable_function() -> None:
    """Execute the same code in a more readable format"""
    div_by_two = lambda n: n // 2
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(map(div_by_two, lst)), "\n")

def main() -> None:
    throw_from_lambda()
    cryptic_lambda()
    readable_function()

if __name__ == "__main__":
    main()