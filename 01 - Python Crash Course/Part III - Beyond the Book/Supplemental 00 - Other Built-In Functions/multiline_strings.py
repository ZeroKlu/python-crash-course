# Using triple-quotes, you can make a multi-line, formatted string

my_string = '''1
 2
  3
   4
    
     6'''
print(my_string)

# While we're here, take note of the older version of string interpolation
name = "Arthur"
num = 42
my_string = "I'm %s, and my favorite number is %s." % (name, num)
print(my_string)

# And the isupper()/islower() functions
my_string = "DataBank"
upper_string = my_string.upper()
lower_string = my_string.lower()
title_string = my_string.title()
for string in [my_string, upper_string, lower_string]:
    state = "mixed"
    if string.isupper(): state = "upper"
    if string.islower(): state = "lower"
    if string.istitle(): state = "title"
    print(f"'{string}' is {state}-case")

# And the isX() functions
for string in ["", "abc", "abc123", "123", "123.45", "\t"]:
    if len(string) == 0: state = "blank"
    elif string.isalpha(): state = "alpha-only"
    elif string.isdecimal(): state = "integer"
    elif string.isalnum(): state = "alpha-numeric"
    elif string.isspace(): state = "white-space"
    else: state = "mixed-types"
    print(f"'{string}' is {state}")

# partition() results in a three-element tuple
my_string = "Hello World!"
print(my_string.partition("o"))
elem_a, elem_b, elem_c = my_string.partition("W")
print(elem_a, elem_b, elem_c)
# Even when the partition match is not found
print(my_string.partition("a"))

# Justify string
my_string = "hello"
print(my_string.ljust(30))
print(my_string.center(30))
print(my_string.rjust(30))

# Int to Char and vice versa
print(ord("A"))
print(chr(65))
