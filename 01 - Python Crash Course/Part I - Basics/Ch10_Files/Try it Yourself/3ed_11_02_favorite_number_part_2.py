# Assignment 10.11
# Favorite Number: Write a program that prompts for the user's favorite number. Use json.dump() to
#                  store this number in a file. Write a separate program that reads in this value
#                  and prints the message, "I know your favorite number! It's _____."

from relative_paths import get_path
from pathlib import Path
import json

file_name = "favorite_number.json"
file_path = get_path(file_name, "Files")

print("Try-it-Yourself:")
print("Assignment 10.11 - part 2\n")

file = Path(file_path)

if file.exists():
    num = json.loads(file.read_text())
    print(f"I know your favorite number is {num}.\n")
else:
    print("You haven't stored a favorite number yet!")