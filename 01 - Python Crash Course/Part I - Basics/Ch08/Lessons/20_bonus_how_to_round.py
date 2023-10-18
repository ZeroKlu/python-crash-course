from sm_utils import clear_terminal, pause
from rounding_functions import *
from statistics import mean
import random
random.seed(100)

# Now that we're looking at libraries and common functions, we need to take a side-trip to discuss rounding.

# Consider these floating-point numbers
pi = 3.14159265359
x = 1.5
y = 2.5

# Python has a built-in function for round()
# The function accepts a float and an optional integer for the number of decimal places
# For example:
clear_terminal()
print("Using the built-in round() function:")
print("round(pi)", round(pi)) # If we omit the decimal places argument, round returns an integer
print("round(pi)", round(pi, 2))

pause()
clear_terminal()

# So far, so good. But observe the following values:
print("Using the built-in round() function:")
print(f"round({x}) =", round(x))
print(f"round({y}) =", round(y))

# For 1.5, we expected it to round to 2 as it did.
# But for 2.5, we expected it to round to 3 but received 2 again.
# What gives?

# This is a design feature of Python's round() function.
# It uses round-to-even (or "Bankers' Rounding"), where rounding ties always round toward the even number.
# This is done to reduce the impact of rounding error across large lists of numbers

pause()
clear_terminal()

# See rounding_functions.py for the definition of the truncate() function
print("Truncating:")
print(f"truncate(pi, 2) = ", truncate(pi, 2))
print(f"truncate(pi) = ", truncate(pi))
print(f"truncate({x}) = ", truncate(x))
print(f"truncate({y}) = ", truncate(y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_up() function
print("Rounding Up:")
print(f"round_up(pi, 2) = ", round_up(pi, 2))
print(f"round_up(pi) = ", round_up(pi))
print(f"round_up({x}) = ", round_up(x))
print(f"round_up({y}) = ", round_up(y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_down() function
print("Rounding Down:")
print(f"round_down(pi, 2) = ", round_down(pi, 2))
print(f"round_down(pi) = ", round_down(pi))
print(f"round_down({x}) = ", round_down(x))
print(f"round_down({y}) = ", round_down(y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_half_up() function
print("Rounding Half Up:")
print(f"round_half_up(pi, 2) = ", round_half_up(pi, 2))
print(f"round_half_up(pi) = ", round_half_up(pi))
print(f"round_half_up({x}) = ", round_half_up(x))
print(f"round_half_up({y}) = ", round_half_up(y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_half_down() function
print("Rounding Half Down:")
print(f"round_half_down(pi, 2) = ", round_half_down(pi, 2))
print(f"round_half_down(pi) = ", round_half_down(pi))
print(f"round_half_down({x}) = ", round_half_down(x))
print(f"round_half_down({y}) = ", round_half_down(y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_half_away_from_zero() function
print("Rounding Half away from Zero:")
print(f"round_half_away_from_zero(pi, 2) = ", round_half_away_from_zero(pi, 2))
print(f"round_half_away_from_zero(pi) = ", round_half_away_from_zero(pi))
print(f"round_half_away_from_zero({x}) = ", round_half_away_from_zero(x))
print(f"round_half_away_from_zero({y}) = ", round_half_away_from_zero(y))

pause()
clear_terminal()

# See rounding_functions.py for the definition of the round_half_to_even() function
print("Rounding Half to Even:")
print(f"round_half_to_even(pi, 2) = ", round_half_to_even(pi, 2))
print(f"round_half_to_even(pi) = ", round_half_to_even(pi))
print(f"round_half_to_even({x}) = ", round_half_to_even(x))
print(f"round_half_to_even({y}) = ", round_half_to_even(y))

pause()
clear_terminal()

# Let's create some data to observe
# data = [random.uniform(-1.0, 1.01) for _ in range(100_000)]
data = [i + j / 10 for i in range(10) for j in range(10)]
d = 0

print("** Rounding Bias Examples **")
print("----------------------------")
print("Computed Average:          ", average(data))
print("Statistical Mean:          ", mean(data))
print("Rounded Mean:              ", average([round(x, d) for x in data]))
print("Truncated Mean:            ", average([truncate(x, d) for x in data]))
print("Round Up Mean:             ", average([round_up(x, d) for x in data]))
print("Round Down Mean:           ", average([round_down(x, d) for x in data]))
print("Round Half Up Mean:        ", average([round_half_up(x, d) for x in data]))
print("Round Half Down Mean:      ", average([round_half_down(x, d) for x in data]))
print("Round Away from Zero Mean: ", average([round_half_away_from_zero(x, d) for x in data]))
print("Round Half to Even Mean:   ", average([round_half_to_even(x, d) for x in data]))
