from relative_paths import get_path
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

folder = "Data"
file_name = "sitka_weather_2021_simple.csv"
file_path = get_path(file_name, folder)

csv_file = Path(file_path)
lines = csv_file.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    # Note: We're not accounting for dates where a high or low temp might be missing
    highs.append(int(row[4]))
    lows.append(int(row[5]))
    dates.append(datetime.strptime(row[2], "%Y-%m-%d"))

# Plot the temperatures
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

# Add plots for both high and low temperatures
ax.plot(dates, highs, color="red")
ax.plot(dates, lows, color="blue")

# Format the plot
ax.set_title("Sitka, AK - Daily High & Low Temperatures, 2021", fontsize=18)
ax.set_xlabel("", fontsize=8)
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=8)

# Add date formatting
fig.autofmt_xdate()

plt.show()
