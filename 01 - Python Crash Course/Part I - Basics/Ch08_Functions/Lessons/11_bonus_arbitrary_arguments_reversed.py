# Although the book doesn't cover it, we can reverse the arbitrary arguments concept

# Here we have a function expecting three positional arguments
def sum_up(x, y, z):
    print(f"{x} + {y} + {z} = {x + y + z}")

values = [2, 3, 4]

# This would NOT work, because the values list is only a single argument
# sum_up(values)
#   TypeError: sum_up() missing 2 required positional arguments: 'y' and 'z'

# However, using the * syntax, we can instruct the call to break up our list and
# deliver it as three positional arguments
sum_up(*values)
# Hint for memory: Remember that when you declare *param in a function, it reads the arguments
#                  as a list. This is just the reverse of that.
