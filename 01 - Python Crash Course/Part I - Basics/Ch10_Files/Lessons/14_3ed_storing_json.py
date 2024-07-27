# We will import the PSL 'json' library in order to read/write JSON strings
import json
from relative_paths import get_path
from pathlib import Path

print("Chapter 10:")
print("Exercise 14 - Storing Data as JSON\n")

# Create an object to store
numbers = [2, 3, 5, 7, 11, 13]
numbers_object = {"numbers" : numbers}

file_name = "numbers.json"
file_path = get_path("numbers.json", "Files")

# Here, we will convert the numbers list to JSON and store it in a string
# Note the 's' for string on the function call to json.dumps()
# Syntax:   json.dumps(<<data>>, <<file>>)
contents = json.dumps(numbers_object)
file = Path(file_path)
file.write_text(contents)

# Verify that we stored the file
print(f"Stored JSON file [{file_name}]")
print(file.read_text())
