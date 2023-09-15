from relative_paths import get_path
from pathlib import Path
import json

print("Chapter 10:")
print("Exercise 15 - Loading Data from JSON\n")

file_name = "numbers.json"
file_path = get_path(file_name, "Files")

file = Path(file_path)
# json.loads() reads a string and parses the JSON therein
# The JSON stored in the file after running lesson 10.14 should be:
#    { "numbers" : [2, 3, 5, 7, 11, 13] }
numbers_object = json.loads(file.read_text())

print(numbers_object["numbers"])
