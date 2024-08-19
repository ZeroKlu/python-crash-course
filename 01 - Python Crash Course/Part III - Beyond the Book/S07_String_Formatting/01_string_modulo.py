def hello(name: str) -> None:
    """Print a greeting using the string-modulo operator"""
    template = "Hello, %s!"
    values = (name,)
    print(template % values)

def price(item: str, qty: int, price: float) -> None:
    """Calculate a total and print a description"""
    template = "%d %s cost $%.2f"
    values = (qty, item, price * qty)
    print(template % values)

def main() -> None:
    hello("World")
    price("bananas", 10, 0.39)

if __name__ == "__main__":
    main()
