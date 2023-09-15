# Assignment 10.11
# Favorite Number: Write a program that prompts for the user's favorite number. Use json.dump() to
#                  store this number in a file. Write a separate program that reads in this value
#                  and prints the message, "I know your favorite number! It's _____."

from relative_paths import get_path
from pathlib import Path
import json

print("Try-it-Yourself:")
print("Assignment 10.11 - part 1\n")

file_name = "favorite_number.json"
file_path = get_path(file_name, "Files")

num = None

while num == None:
    response = input("Please enter your favorite number:\n> ")
    try:
        num = int(response)
    except ValueError:
        print("Your entry must be a number!")

file = Path(file_path)
file.write_text(json.dumps(num))

print(f"I saved {num} as your favorite number!\n")
