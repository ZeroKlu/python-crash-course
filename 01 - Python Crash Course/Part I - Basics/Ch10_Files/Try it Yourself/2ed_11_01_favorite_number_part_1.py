# Assignment 10.11
# Favorite Number: Write a program that prompts for the user's favorite number. Use json.dump() to
#                  store this number in a file. Write a separate program that reads in this value
#                  and prints the message, "I know your favorite number! It's _____."

import os
import json

print("Try-it-Yourself:")
print("Assignment 10.11 - part 1\n")

ROOT_DIR = os.path.dirname(__file__)

file_name = "favorite_number.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

num = None

while num == None:
    response = input("Please enter your favorite number:\n> ")
    try:
        num = int(response)
    except ValueError:
        print("Your entry must be a number!")

with open(file_path, "w") as f:
    json.dump(num, f)

print(f"I saved {num} as your favorite number!\n")
