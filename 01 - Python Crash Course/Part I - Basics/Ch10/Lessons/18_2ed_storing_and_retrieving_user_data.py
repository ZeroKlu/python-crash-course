import os
import json

ROOT_DIR = os.path.dirname(__file__)

print("Chapter 10:")
print("Exercise 18 - Storing and Retrieving User Data in JSON file\n")

file_name = "username.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

try:
    with open(file_path) as f:
        username = json.load(f)
except:
    first_name = input("Enter your first name:\n> ")
    last_name = input("Enter your last name:\n> ")

    username = f"{first_name[0]}{last_name}".upper()

    with open(file_path, "w") as f:
        json.dump(username, f)

    print(f"We'll remember you when you come back, {username}")
else:
    print(f"Welcome back, {username}\n")
