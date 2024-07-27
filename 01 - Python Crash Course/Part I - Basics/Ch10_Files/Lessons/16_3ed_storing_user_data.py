from relative_paths import get_path
from pathlib import Path
import json

print("Chapter 10:")
print("Exercise 16 - Storing User Data as JSON\n")

first_name = input("Enter your first name:\n> ")
last_name = input("Enter your last name:\n> ")

username = f"{first_name[0]}{last_name}".upper()

file_name = "username.json"
file_path = get_path(file_name, "Files")

file = Path(file_path)
file.write_text(json.dumps(username))

print(f"We'll remember you when you come back, {username}")
