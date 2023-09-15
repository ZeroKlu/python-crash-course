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

# for index, column in enumerate(header_row):
#     print(index, column)

# Now that we know tha the high temperature (TMAX) is in index 4, we can extract the data from the CSV rows
highs = [int(row[4]) for row in reader]

print(highs)
