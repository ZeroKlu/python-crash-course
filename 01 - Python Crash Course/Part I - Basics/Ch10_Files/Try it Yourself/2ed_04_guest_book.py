# Assignment 10.4
# Guest Book: Write a while loop that prompts users for their name. When they enter their name,
#             print a greeting to the screen and add a line recording their visit in a file called
#             guest_book.txt. Make sure each entry appears on a new line in the file.

import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "T.10.03.guest_book.txt")

print("Try-it-Yourself:")
print("Assignment 10.4\n")

while True:
    name = input("Please enter your name (or 'quit'):\n> ")
    if name.lower() == "quit":
        break
    with open(file_path, "a") as file:
        file.write(f"{name}\n")

with open(file_path, "r") as file:
    print(file.read())