# Assignment 10.13
# Verify User: The final listing for remember_me.py assumes either that the user has already entered
#              their username or that the program is running for the first time. We should modify it
#              in case the current user is not the person who last used the program. Before printing
#              a welcome back message in greet_user(), ask the user if this is the correct username.
#              If it's not, call get_new_username() to get the correct username.

from relative_paths import get_path
from pathlib import Path
import json

def store_user(file_path):
    """Store the username to JSON file"""
    first_name = input("Enter your first name:\n> ")
    last_name = input("Enter your last name:\n> ")

    username = f"{first_name[0]}{last_name}".upper()

    file = Path(file_path)
    file.write_text(json.dumps(username))

    return username

def get_stored_user(file_path):
    """Attempt to retrieve the username from JSON file"""
    file = Path(file_path)

    if file.exists():
        username = json.loads(file.read_text())
        return username
    else:
        return None

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
file_path = get_path(file_name, "Files")

greet_user(file_path)
