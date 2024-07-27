from relative_paths import get_path
from pathlib import Path
import json

print("Chapter 10:")
print("Exercise 18 - Storing and Retrieving User Data in JSON file\n")

file_name = "username.json"
file_path = get_path(file_name, "Files")

file = Path(file_path)

if file.exists():
    username = json.loads(file.read_text())
    print(f"Welcome back, {username}\n")
else:
    first_name = input("Enter your first name:\n> ")
    last_name = input("Enter your last name:\n> ")

    username = f"{first_name[0]}{last_name}".upper()

    file.write_text(json.dumps(username))

    print(f"We'll remember you when you come back, {username}")
