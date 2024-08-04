# Assignment 10.4
# Guest: Write a program that prompts the user for their name. When they respond,
#        write their name to a file called guest.txt.

from relative_paths import get_path
from pathlib import Path

file_path = get_path("guest.txt", "Files")

print("Try-it-Yourself:")
print("Assignment 10.4\n")

file = Path(file_path)

name = input("Please enter your name:\n> ")
file.write_text(name + "\n")

print(file.read_text())
