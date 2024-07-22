print("Chapter 7:")
print("Exercise 5 - Using a Boolean Flag")

prompt = "\nTell me something and I will repeat it back to you:\n> "
message = ""

# Setting a Boolean flag outside the loop allows you to manage multiple conditions that can end the loop
active = True

while active:
    message = input(prompt)
    if message.lower() == "quit":
        # Here, we make the flag false, so the loop will terminate after the current iteration
        active = False
    else:
        print(message)
else:
    # We can use an else statement to perform some tasks when the loop condition becomes False
    print("\nThe loop terminated because the 'active' flag is now '{active}'")

# You may have heard of using bit-flags in other scenarios. This is not the same thing.
# You can review Chapter 5, Lesson 7 for a review of bitwise operations and bitflags
