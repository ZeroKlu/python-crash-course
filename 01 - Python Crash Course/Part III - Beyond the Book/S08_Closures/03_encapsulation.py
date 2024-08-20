def increment(n: int) -> int:
    """Increment an integer by 1"""
    max = 10
    if n >= max:
        return n
    def inner_increment():
        """Encapsulated function"""
        return n + 1
    return inner_increment()

def main() -> None:
    n = 5
    print(f"{n}++ = {increment(n)}")
    n = 10
    print(f"{n}++ = {increment(n)}")

    try:
        print(f"{n}++ = {inner_increment(n)}") # type: ignore
    except NameError as e:
        print(f"A NameError occurred!\n{e}")

if __name__ == "__main__":
    main()
