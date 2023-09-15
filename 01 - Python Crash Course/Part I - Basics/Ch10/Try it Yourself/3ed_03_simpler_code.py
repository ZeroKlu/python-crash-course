# Assignment 10-3.
# Simpler Code: The program file_reader.py in this section uses a temporary variable, lines,
#               to show how splitlines() works. You can skip the temporary variable and loop directly
#               over the list that splitlines() returns: for line in contents.splitlines():
#               Remove the temporary variable from each of the programs in this section, to make them more concise.

from relative_paths import get_path
from pathlib import Path

text = Path(get_path("pi_digits.txt", "Files")).read_text()

for line in text.splitlines():
    print(line.rstrip())
