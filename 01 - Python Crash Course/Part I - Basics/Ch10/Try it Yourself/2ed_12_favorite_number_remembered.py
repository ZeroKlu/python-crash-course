# Assignment 10.12
# Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file. If the number
#                             is already stored, report the favorite number to the user. If not, prompt
#                             for the user's favorite number and store it in a file. Run the program twice
#                             to see that it works.

import os
import json

ROOT_DIR = os.path.dirname(__file__)

print("Try-it-Yourself:")
print("Assignment 10.12\n")

def store_favorite_number(file_path):
    """Get the user's favorite number and store it in a file"""
    num = None
    while num == None:
        response = input("Please enter your favorite number:\n> ")
        try:
            num = int(response)
        except ValueError:
            print("Your entry must be a number!\n")
    with open(file_path, "w") as f:
        json.dump(num, f)
    print(f"I saved {num} as your favorite number!\n")
    return num

def get_favorite_number(file):
    """Attempt to read user's favorite number from a file"""
    try:
        with open(file) as f:
            num = json.load(f)
        return num
    except FileNotFoundError:
        return store_favorite_number(file)

file_name = "favorite_number_remembered.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

number = get_favorite_number(file_path)
if number:
    print(f"I know your favorite number is {number}.\n")
else:
    print("Something went wrong!")
