from relative_paths import get_path
from pathlib import Path
import json

print("Chapter 10:")
print("Exercise 17 - Retrieving User Data from JSON file\n")

file_name = "username.json"
file_path = get_path(file_name, "Files")

file = Path(file_path)
username = json.loads(file.read_text())

print(f"Welcome back, {username}\n")
