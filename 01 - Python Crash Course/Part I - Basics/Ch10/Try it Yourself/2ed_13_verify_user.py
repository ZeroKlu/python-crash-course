# Assignment 10.13
# Verify User: The final listing for remember_me.py assumes either that the user has already entered
#              their username or that the program is running for the first time. We should modify it
#              in case the current user is not the person who last used the program. Before printing
#              a welcome back message in greet_user(), ask the user if this is the correct username.
#              If it's not, call get_new_username() to get the correct username.

import os
import json

ROOT_DIR = os.path.dirname(__file__)

def store_user(file_path):
    """Store the username to JSON file"""
    first_name = input("Enter your first name:\n> ")
    last_name = input("Enter your last name:\n> ")

    username = f"{first_name[0]}{last_name}".upper()

    with open(file_path, "w") as f:
        json.dump(username, f)

    return username

def get_stored_user(file_path):
    """Attempt to retrieve the username from JSON file"""
    try:
        with open(file_path) as f:
            username = json.load(f)
    except:
        return None
    else:
        return username

def greet_user(file_path):
    """Show desired greeting to user"""
    username = get_stored_user(file_path)
    matched = False
    if username:
        answer = input(f"Are you {username.upper()}? (Y|N)\n> ")
        matched = answer[0].lower() == "y"
    else:
        username = store_user(file_path)

    if matched:
        print(f"\nWelcome back, {username.upper()}\n")
    else:
        username = store_user(file_path)
        print(f"\nWe'll remember you when you come back, {username.upper()}\n")

print("Try-it-Yourself:")
print("Assignment 10.13\n")

file_name = "username.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

greet_user(file_path)
