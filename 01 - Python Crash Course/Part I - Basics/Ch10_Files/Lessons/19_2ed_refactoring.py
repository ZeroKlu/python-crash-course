import os
import json

ROOT_DIR = os.path.dirname(__file__)

# Perform Lesson Tasks
print("Chapter 10:")
print("Exercise 19 - Refactoring Code\n")
        
file_name = "username.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

# Often you will find that you have written difficult-to-follow "spaghetti" code
# Refactoring (splitting out functional code into meaningfully-named functions) can be the answer

def store_user(file_path):
    """Create the username and store it to a JSON file"""
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
    if username:
        print(f"Welcome back, {username.upper()}")
    else:
        username = store_user(file_path)
        print(f"We'll remember you when you come back, {username.upper()}")

# Now instead of spaghetti code, we make a single, meaningful call
greet_user(file_path)
