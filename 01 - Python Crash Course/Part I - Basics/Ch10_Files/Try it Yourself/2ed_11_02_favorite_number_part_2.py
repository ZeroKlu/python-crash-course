# Assignment 10.11
# Favorite Number: Write a program that prompts for the user's favorite number. Use json.dump() to
#                  store this number in a file. Write a separate program that reads in this value
#                  and prints the message, "I know your favorite number! It's _____."

import os
import json

ROOT_DIR = os.path.dirname(__file__)
file_name = "favorite_number.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

print("Try-it-Yourself:")
print("Assignment 10.11 - part 2\n")

try:
    with open(file_path) as f:
        num = json.load(f)
        print(f"I know your favorite number is {num}.\n")
except FileNotFoundError:
    print("You haven't stored a favorite number yet!")
