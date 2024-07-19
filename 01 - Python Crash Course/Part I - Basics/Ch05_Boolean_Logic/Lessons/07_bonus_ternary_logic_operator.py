# Let's get a value from the user:
user_entry = input("Enter whatever you want:\n> ")

# If the user entered nothing but whitespace, then set the value to the string "nothing"

# Up to now, if we wanted to do that, we'd have structured an if/else like this:
if user_entry.strip() == "":
    data = "nothing"
else:
    data = user_entry.strip()
print(f"You entered: [{data}]")

# In many languages, you will encounter a ?: ternary logic operator, where the
#   syntax looks like condition ? value_if_true : value_if_false

# Python does not have an operator for this, but we can accomplish the same thing
#   using the following syntax:     value_if_true if condition else value_if_false

# Examples:
# Here, we're setting a value for data based on whether or not the user entered non-space characters
data = "nothing" if user_entry.strip() == "" else user_entry.strip()
print(f"You entered: [{data}]")

# We could also just use the ternary operator right in the print() statement
print(f"You entered: [{'nothing' if user_entry.strip() == '' else user_entry.strip()}]")
