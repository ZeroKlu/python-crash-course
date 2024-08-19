from random import randint

def get_random_numbers(min: int=1, max: int=1000, length: int=5) -> list[int]:
    """Get a list of random integers"""
    return [randint(min, max) for _ in range(length)]

def align_numbers(numbers: list[int]) -> None:
    """Right-justify numbers for proper alignment"""
    total = sum(numbers)
    width = max(len(str(n)) for n in numbers + [total]) + 1
    for i in range(len(numbers)):
        lead = "+" if i == len(numbers) - 1 else " "
        print(f"{lead}{numbers[i]:>{width}}")
    print("-" * (width + 1))
    print(f" {total:>{width}}")

def main() -> None:
    numbers = get_random_numbers()
    align_numbers(numbers)

if __name__ == "__main__":
    main()
