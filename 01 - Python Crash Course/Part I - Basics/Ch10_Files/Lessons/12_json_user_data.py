print("Chapter 10:")
print("Exercise 12 - Storing User Data as JSON\n")

from sm_utils import pause, clear_terminal

def get_user_data() -> dict[str, str]:
    """Get the user's information"""

    return user

# --- 2nd Edition Method ---

import os
import json

ROOT_DIR = os.path.dirname(__file__)
file_name = "user.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

clear_terminal()

user = {}
user["first_name"] = input("Enter your first name:\n> ")
user["last_name"] = input("Enter your last name:\n> ")
user["username"] = \
    f"{user['first_name'][0]}{user['last_name']}".upper()

with open(file_path, "w") as f:
    json.dump(user, f)
print(f"We'll remember you when you come back, {user['username']}")

pause()
clear_terminal()

with open(file_path) as f:
    user = json.load(f)
print(f"Welcome back, {user['username']}")

pause()
clear_terminal()

# --- 3rd Edition Method ---

from relative_paths import get_path
from pathlib import Path
import json

user = {}
user["first_name"] = input("Enter your first name:\n> ")
user["last_name"] = input("Enter your last name:\n> ")
user["username"] = \
    f"{user['first_name'][0]}{user['last_name']}".upper()

file_name = "user.json"
file_path = get_path(file_name, "Files")

file = Path(file_path)
file.write_text(json.dumps(user))
print(f"We'll remember you when you come back, {user['username']}")

pause()
clear_terminal()

user = json.loads(file.read_text())
print(f"Welcome back, {user['username']}")