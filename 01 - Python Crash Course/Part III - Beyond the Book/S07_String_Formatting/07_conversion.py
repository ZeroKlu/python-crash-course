from datetime import datetime

def convert_dates() -> None:
    """Display dates using `str()` and `repr()` conversions"""
    now = datetime.now()
    print("{!s}".format(now))
    print("{!r}".format(now))

def replace_invalid(invalid_string: str) -> str:
    """Remove invalid characters from a string"""
    return "{!a}".format(invalid_string)

def main():
    convert_dates()
    invalid_string = "Thisö stringö haö invalidö charactersö."
    print(replace_invalid(invalid_string))

if __name__ == "__main__":
    main()
