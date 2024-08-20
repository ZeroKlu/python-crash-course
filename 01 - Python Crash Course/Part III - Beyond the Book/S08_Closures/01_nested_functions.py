def outer_function() -> None:
    """Executes the inner function"""
    def inner_function() -> None:
        print("Hello World!")
    inner_function()

def outer_function_with_args(name: str) -> None:
    """Executes the inner function (sharing variable 'name')"""
    def inner_function() -> None:
        print(f"Hello {name.title()}!")
    inner_function()

def main() -> None:
    outer_function()
    outer_function_with_args("Scott")

if __name__ == "__main__":
    main()
