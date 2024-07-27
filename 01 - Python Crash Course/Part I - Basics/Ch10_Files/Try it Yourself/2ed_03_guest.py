# Assignment 10.3
# Guest: Write a program that prompts the user for their name. When they respond,
#        write their name to a file called guest.txt.

import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "T.10.03.guest.txt")

print("Try-it-Yourself:")
print("Assignment 10.3\n")

name = input("Please enter your name:\n> ")
with open(file_path, "w") as file:
    file.write(name)
    
with open(file_path, "r") as file:
    print(file.read())
