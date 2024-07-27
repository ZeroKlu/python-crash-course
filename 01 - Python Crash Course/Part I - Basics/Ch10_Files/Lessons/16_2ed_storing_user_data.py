import os
import json

ROOT_DIR = os.path.dirname(__file__)

print("Chapter 10:")
print("Exercise 16 - Storing User Data as JSON\n")

first_name = input("Enter your first name:\n> ")
last_name = input("Enter your last name:\n> ")

username = f"{first_name[0]}{last_name}".upper()

file_name = "username.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

with open(file_path, "w") as f:
    json.dump(username, f)

print(f"We'll remember you when you come back, {username}")
