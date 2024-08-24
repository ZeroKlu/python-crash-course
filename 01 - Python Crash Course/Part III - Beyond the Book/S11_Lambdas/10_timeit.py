from timeit import timeit

def timeit_normal() -> float:
    return timeit("factorial(999)", "from math import factorial", 
                  number=10)

def timeit_with_lambda() -> float:
    from math import factorial
    return timeit(lambda: factorial(999), number=10)

def main() -> None:
    print(timeit_normal(), "\n")
    print(timeit_with_lambda())

if __name__ == "__main__":
    main()
