import os
import json

ROOT_DIR = os.path.dirname(__file__)

print("Chapter 10:")
print("Exercise 17 - Retrieving User Data from JSON file\n")

file_name = "username.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

with open(file_path) as f:
    username = json.load(f)

print(f"Welcome back, {username}\n")
