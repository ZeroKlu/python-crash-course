def is_even_mod(n: int) -> bool:
    return not n % 2

def is_even_and(n: int) -> bool:
    return not n & 1

def main() -> None:
    for n in [42, 73]:
        print(f"Using 'n % 2', {n} is {('even' if is_even_mod(n) else 'odd')}")
        print(f"Using 'n & 1', {n} is {('even' if is_even_and(n) else 'odd')}")

if __name__ == "__main__":
    main()
