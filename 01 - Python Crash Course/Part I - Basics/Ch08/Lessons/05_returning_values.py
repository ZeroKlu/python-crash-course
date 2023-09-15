print("Chapter 8:")
print("Exercise 5 - Returning Values")

# By writing your function so that it returns some data, you add a lot of flexibility to your code
# Note: ALL functions provide return values. If you do not include a return statement, the function returns None

# Note: You do not have to declare a return in the method signature
def get_formatted_name_simple(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    # The return statement determines what the function returns to the calling code
    return full_name.title()

def get_formatted_name_middle(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

def pause():
    """Wait for user to press <ENTER>"""
    input("\nPress <ENTER> to continue\n")

# Often, you don't want a function to display its results but to return them and store them in variables.
musician = get_formatted_name_simple("jimi", "hendrix")
print(musician)
pause()

# This function requires a middle name
musician = get_formatted_name_middle("john", "lee", "hooker")
print(musician)
pause()

# By using a default value, this function gives the option of ignoring the middle name
musician = get_formatted_name("jimi", "hendrix")
print(musician)
musician = get_formatted_name("john", "hooker", "lee")
print(musician)

# HINT: Mouse over a function name to see what data type it returns
