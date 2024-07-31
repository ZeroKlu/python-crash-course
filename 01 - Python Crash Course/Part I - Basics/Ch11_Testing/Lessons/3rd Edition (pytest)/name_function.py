"""A module containing name-formatting functions"""

# Here is the function we'll be testing
def get_formatted_name(first, last, middle = ""):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

# To see a broken test case, we'll also test this one
def get_formatted_name_broken(first, last, middle):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
