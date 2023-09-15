print("Chapter 7:")
print("Exercise 10 - Populating a Dictionary")

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name?\n> ")
    mountain = input("Which mountain would you like to climb someday?\n> ")
    
    # Store the response in the dictionary.
    responses[name] = mountain
    
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no)\n> ").lower()[0]
    if repeat == "n":
        polling_active = False
        
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, mountain in responses.items():
    print(f"{name.title()} would like to climb {mountain.title()}.")
