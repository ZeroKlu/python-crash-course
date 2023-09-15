# We will import the PSL 'json' library in order to read/write JSON strings
import json
import os

ROOT_DIR = os.path.dirname(__file__)

print("Chapter 10:")
print("Exercise 14 - Storing Data as JSON\n")

# Create an object to store
numbers = [2, 3, 5, 7, 11, 13]
numbers_object = {"numbers" : numbers}

file_name = "numbers.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)
with open(file_path, "w") as f:
    # Here, we will convert the numbers list to JSON and store it in a file
    # Syntax:   json.dump(<<data>>, <<file>>)
    json.dump(numbers_object, f)

# Verify that we stored the file
print(f"Stored JSON file [{file_name}]")
with open(file_path) as f:
    print(f.read().rstrip())
