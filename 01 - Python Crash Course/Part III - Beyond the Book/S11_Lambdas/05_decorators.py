def trace(func: callable) -> callable:
    def _trace(*args, **kwargs):
        print(f"[TRACE] func: {func.__name__}, args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return _trace

@trace
def add_two(x: int) -> int:
    return x + 2

def main() -> None:
    print(add_two(3), "\n")

    print((trace(lambda x: x + 2))(3), "\n")
    
    print(list(map(trace(lambda x: x * 2), range(3))), "\n")

if __name__ == "__main__":
    main()
