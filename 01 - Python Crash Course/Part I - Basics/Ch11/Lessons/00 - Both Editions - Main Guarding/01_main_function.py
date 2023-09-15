# It's usually best to compose all of your script code in functions

# Note that because the call to say_hello() is in a function, the say_hello function doesn't have to be defined first
# Since this is the function called when checking for __main__, this method will execute when the script is run
def main():
    say_hello()

# Simple function to demonstrate
def say_hello():
    print("Hello World!")

# In python, there are some conventions for the use of underscores in naming:
#
#  Leading Underscore:
#  _name        This is an indicator from the developer that we should treat the variable as private.
#               Generally speaking this is not enforced in any way by the Python interpreter
#               However, when declared in a module it will not be imported using:
#                   from <<module>> import *
#               It will, however, be accessible when imported using:
#                   import <<module>>
#
#  Trailing Underscore:
#  name_        This is used to disambiguate when the variable name is a Python reserved word
#               For Example:
#                   class_ = "some value"
#
#  Standalone Underscore:
#  _            This is used to create a temp variable that will not be accessed anywhere in the code
#               For Example:
#                   for _ in range(100): do_something_100_times()
#                   var1, _, _, var2, _ = ["important", "don't care", "don't care", "important", "don't care"]
#
#  Leading Dunderscore:
#  __name       This is used for name mangling (to prevent collisions with subclass naming)
#               If used in a class, the interpreter renames this to _<<class>>__var
#
#  Leading and Trailing Dunderscores ("Dunder Methods"):
#  __name__     This naming convention is used to indicate special, universal methods in Python such as:
#                   __init__        Class constructor
#               We can override these in our classes, for example:
#                   __str__         Defines the data written to the screen by a print()
#                                   We could modify this so that print(our_class) has special behavior
#                                   We'll see this in our model classes in our portal
#               While we *could* create out own dunder methods, this nomenclature is reserved for future use in Python,
#                   so we probably shouldn't.
#               More Info:  https://www.section.io/engineering-education/dunder-methods-python/

# The dunder '__name__' is set when a Python program executes, and if this file is the one being run,
#     its value is '__main__'
if __name__ == "__main__":
    # After checking that this file is the one being executed this will run our main() function
    main()
