"""Assignment 7.5"""

print("Chapter 7:")
print("Exercise 5 - Using a Boolean Flag")

prompt = "\nTell me something and I will repeat it back to you:\n> "
message = ""
active = True

while active:
    message = input(prompt)
    if message.lower() == "quit":
        active = False
    else:
        print(message)
else:
    print(f"\nThe loop terminated because the 'active' flag is now '{active}'")
