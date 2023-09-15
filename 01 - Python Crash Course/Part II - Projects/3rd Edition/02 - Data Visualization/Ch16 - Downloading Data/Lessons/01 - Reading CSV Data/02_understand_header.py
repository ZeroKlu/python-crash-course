from relative_paths import get_path
from pathlib import Path
import csv

folder = "Data"
file_name = "sitka_weather_07-2021_simple.csv"
file_path = get_path(file_name, folder)

csv_file = Path(file_path)
lines = csv_file.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# The enumerate() function provides the index and value of each item in a list
# We'll use this to view what the headers and their indices are
# We can later use this for parsing the CSV data
for index, column in enumerate(header_row):
    print(index, column)
