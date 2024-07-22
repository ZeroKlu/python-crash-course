print("Chapter 7:")
print("Exercise 6 - Using 'break'")

# The "break" command immediately ends the loop
# - The remainder of the current iteration does not execute
# - No more iterations execute

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)\n> "

# This would seem to be an infinite loop because (tautologically) True can never become False
while True:
    city = input(prompt)
    if city.lower() == "quit":
        # But this immediately stops the loop after the user enters "quit"
        break
    else:
        print(f"I'd love to go to {city.title()}!")
