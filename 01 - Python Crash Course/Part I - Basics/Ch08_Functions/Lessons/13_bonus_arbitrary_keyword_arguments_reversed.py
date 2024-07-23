# Although the book doesn't cover it, we can reverse the arbitrary keywords arguments concept

# Here we have a function expecting three positional arguments
def sum_up(x, y, z):
    print(f"{x} + {y} + {z} = {x + y + z}")

values = {"z": 4, "y": 3}

# This would NOT work, because the values dictionary is only a single argument
# sum_up(2, values)
#   TypeError: sum_up() missing 1 required positional argument: 'z'

# However, using the ** syntax, we can instruct the call to break up our dictionary and
# deliver it as two keyword arguments
sum_up(2, **values)
# Hint for memory: Remember that when you declare **param in a function, it reads the arguments
#                  as a dictionary. This is just the reverse of that.
