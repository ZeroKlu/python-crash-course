from relative_paths import get_path
from pathlib import Path

file_path = get_path("programming.txt", "Files")

file = Path(file_path)

# Let's write a line to the file
# Python does not contain a write_line method, so you must include your own new-line characters
file.write_text("I love programming!\n")

# Verify that the file was written
print(file.read_text())

# Create a string to write with multiple lines
content = "I love programming!\n"
content += "I love creating new games.\n"
content += "I also love working with data.\n"

# Write the multi-line content (Notice how we can continue to use the Path object unlike a closed file)
file.write_text(content)
# Note: The write_text method rewrites the entire text file, so be careful when using it

# Verify that the file was overwritten with the new data
print(file.read_text())
