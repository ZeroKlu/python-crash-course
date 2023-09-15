import os
import json

ROOT_DIR = os.path.dirname(__file__)

print("Chapter 10:")
print("Exercise 15 - Loading Data from JSON\n")

file_name = "numbers.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

with open(file_path) as f:
    # json.load() reads the file and parses the JSON therein
    # The JSON stored in the file after running lesson 10.14 should be:
    #    { "numbers" : [2, 3, 5, 7, 11, 13] }
    numbers_object = json.load(f)

print(numbers_object["numbers"])
