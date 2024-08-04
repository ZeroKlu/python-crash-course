# Assignment 10.5
# Programming Poll: Write a while loop that asks people why they like programming. Each time someone
#                   enters a reason, add their reason to a file that stores all the responses.

import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "poll_results.txt")

print("Try-it-Yourself:")
print("Assignment 10.5\n")

while True:
    print("What do you like about programming?")
    response = input("Please enter your answer (or 'quit'):\n> ")
    if response.lower() == "quit":
        break
    with open(file_path, "a") as file:
        file.write(f"{response}\n")

with open(file_path, "r") as file:
    print(file.read())
