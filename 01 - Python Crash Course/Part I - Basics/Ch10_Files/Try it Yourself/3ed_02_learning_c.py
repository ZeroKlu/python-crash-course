"""Assignment 10.2 (3rd Edition)"""

# Learning C: You can use the replace() method to replace any word
#             in a string with a different word. Here's a quick
#             example showing how to replace 'dog' with 'cat' in a
#             sentence:
#             -----------------------------------
#             >>> message = "I really like dogs."
#             >>> message.replace('dog', 'cat')
#             'I really like cats.'
#             -----------------------------------
#             Read in each line from the file you just created,
#             `learning_python.txt`, and replace the word Python
#             with the name of another language, such as C. Print
#             each modified line to the screen.

from pathlib import Path
from relative_paths import get_path

file_path = get_path("learning_python.txt", "Files")

print("Try-it-Yourself:")
print("Assignment 10.2\n")

file = Path(file_path)
text = file.read_text(encoding="utf-8")
for line in text.splitlines():
    print(line.rstrip().replace("Python", "C++"))
