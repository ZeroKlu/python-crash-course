print("Chapter 7:")
print("Exercise 1 - Get User Input")

# The "input" method prompts the user, pauses for user input, and returns the data the user types
message = input("Tell me something, and I will repeat it back to you:\n> ")
print(message)

name = input("\nPlease enter your name:\n> ")
print(f"\nHello, {name.title()}!")

prompt = "\nIf you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?\n> "
first_name = input(prompt)
prompt += "\nWhat is your last name?\n> "
last_name = input(prompt)
print(f"Hello, {first_name.title()} {last_name.title()}!")
