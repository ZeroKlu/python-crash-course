# In many languages, you will encounter the ?: ternary logic operator, where the
#   syntax looks like condition ? value_if_true : value_if_false

# Python does not have an operator for this, but we can accomplish the same thing
#   using the following syntax:     value_if_true if condition else value_if_false

# Example:
numbers = range(1, 16)
five_multiples = ["0", "5"]
for n in numbers:
    # Here we are setting the value of 'state' based on whether the number ends in 0 or 5 or not.
    state = "" if str(n)[-1] in five_multiples else "not "
    print(f"{n} is {state}a multiple of 5")

# There is a much better way of doing this, which I will show below, but you'll have to wait until
#   chapter 8 to learn the underlying operator
# for n in numbers:
#     # Here we are setting the value of 'state' based on whether the number is divisible by 5 or not.
#     state = "" if n % 5 == 0 else "not "
#     print(f"{n} is {state}a multiple of 5")
