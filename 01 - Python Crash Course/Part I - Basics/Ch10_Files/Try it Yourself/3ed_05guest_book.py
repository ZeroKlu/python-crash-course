# Assignment 10.5
# Guest Book: Write a while loop that prompts users for their name. When they enter their name,
#             print a greeting to the screen and add a line recording their visit in a file called
#             guest_book.txt. Make sure each entry appears on a new line in the file.

from relative_paths import get_path
from pathlib import Path

file_path = get_path("guest_book.txt", "Files")

print("Try-it-Yourself:")
print("Assignment 10.5\n")

names = ""

while True:
    name = input("Please enter your name (or 'quit'):\n> ")
    if name.lower() == "quit":
        break
    names += name + "\n"

file = Path(file_path)

with file.open("a") as f:
    f.write(names)

print(file.read_text())
