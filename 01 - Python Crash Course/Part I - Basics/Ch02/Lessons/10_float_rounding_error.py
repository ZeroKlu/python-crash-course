
print("Chapter 2:")
print("Exercise 9 - Understanding floating-point rounding error\n")

# Any number in a computer can always be expressed as an integer multiplied by an integer power of two.
#       n * 2^m	(m, n) ∈ ℤ
#
# This means that:
# 1.	There are no floating-point decimals inside the computer.
# 2.	The majority of floating-point value approximations are inexact.
#       We just select the nearest value that the computer can express. For example:
# 
#       0.1	≅ 7205759403792794 * 2^-56 ≅ 0.10000000000000000555
#       0.2	≅ 7205759403792794 * 2^-55 ≅ 0.2000000000000000111
#
# Because these values do not show a discrepancy until the 18th decimal place, you often will not see the
#   rounding error visually in your results. Nevertheless, it is there.
#
# >>> print(.1)
# >>> 0.1
# >>> print(.2)
# >>> 0.2
#
# At 0.3, the discrepancy is a bit below the real value instead of above, but still does not show as part of our output
#
# 	0.3 ≅ 5404319552844595 * 2^-54 ≅ 0.29999999999999998889776975
#
# >>> print(.3)
# >>> 0.3
#
# However, the sum of the approximations of 0.1 and 0.2 is not an approximation of 0.3
#
# 	 0.10000000000000000555 + 0.2000000000000000111 ≅ 0.30000000000000004440
#
# Here, the rounding error has changed, because the computer doesn’t know anything about the expected approximation of .3,
#   just about the request to add the approximations of .1 and .2
#
# Additionally, in Python we get to see 17 decimal places in our output, and since the decimal rounding error has moved
#   into the 17th instead of 18th position, we now actually see the rounding error in our code results
#
# >>> print(0.1 + 0.2)
# >>> 0.30000000000000004

print(f"      0.1 = {0.1}")
print(f"      0.2 = {0.2}")
print(f"      0.3 = {0.3}")
print(f"0.1 + 0.2 = {0.1 + 0.2}\n")
