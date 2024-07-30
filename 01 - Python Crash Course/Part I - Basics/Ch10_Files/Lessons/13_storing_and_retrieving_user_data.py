print("Chapter 10:")
print("Exercise 13 - Storing and Retrieving User Data Using a JSON File\n")

from sm_utils import pause, clear_terminal

clear_terminal()

# --- 2nd Edition Method ---

import os
import json

def user_check(file_path: str) -> None:
    """
    If a user file exists, get the user from it
    Otherwise, create a new file with user input
    """
    try:
        with open(file_path) as f:
            user = json.load(f)
            print(f"Welcome back, {user['username']}")
    except FileNotFoundError:
        user = {
            "first_name": input("Enter your first name:\n> "),
            "last_name": input("Enter your last name:\n> ")
        }
        user["username"] = f"{user['first_name'][0]}{user['last_name']}".upper()
        with open(file_path, "w") as f:
            json.dump(user, f)
        print(f"We'll remember you when you come back, {user['username']}")

ROOT_DIR = os.path.dirname(__file__)
file_name = "user.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)
user_check(file_path)

pause()
clear_terminal()

# --- 3rd Edition Method ---

from relative_paths import get_path
from pathlib import Path
import json

def user_check(file_path: str) -> None:
    """
    If a user file exists, get the user from it
    Otherwise, create a new file with user input
    """
    file_object = Path(file_path)
    try:
        user = json.loads(file_object.read_text())
        print(f"Welcome back, {user['username']}")
    except FileNotFoundError:
        user = {
            "first_name": input("Enter your first name:\n> "),
            "last_name": input("Enter your last name:\n> ")
        }
        user["username"] = f"{user['first_name'][0]}{user['last_name']}".upper()
        file_object.write_text(json.dumps(user))
        print(f"We'll remember you when you come back, {user['username']}")

file_name = "user.json"
file_path = get_path(file_name, "Files")
user_check(file_path)

