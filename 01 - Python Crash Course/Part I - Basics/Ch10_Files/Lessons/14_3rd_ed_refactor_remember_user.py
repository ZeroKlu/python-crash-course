print("Chapter 10:")
print("Exercise 14 - Refactoring Code\n")

from sm_utils import pause, clear_terminal

clear_terminal()

# --- 3rd Edition Method ---

from relative_paths import get_path
from pathlib import Path
import json

USER_FILE = "user.json"
USER_DIR = "Files"

def get_user_path() -> str:
    """Returns the path to the user JSON file"""
    return get_path(USER_FILE, USER_DIR)

def read_user_file(file_path: str) -> dict[str, str] | None:
    """Reads the user JSON file and returns the `user` dictionary"""
    try:
        path_obj = Path(file_path)
        return json.loads(path_obj.read_text())
    except FileNotFoundError:
        return None

def write_user_file(user: dict[str, str], file_path: str) -> None:
    """Writes the `user` dictionary to the user JSON file"""
    path_obj = Path(file_path)
    path_obj.write_text(json.dumps(user))

def get_user_input() -> dict[str, str]:
    user = {
        "first_name": input("Enter your first name:\n> "),
        "last_name": input("Enter your last name:\n> ")
    }
    user["username"] = f"{user['first_name'][0]}{user['last_name']}".upper()
    return user

def check_returning_user() -> None:
    path = get_user_path()
    user = read_user_file(path)
    if user is None:
        user = get_user_input()
        write_user_file(user, path)
        print(f"We'll remember you next time, {user['username']}")
    else:
        print(f"Welcome back, {user['username']}!")

check_returning_user()