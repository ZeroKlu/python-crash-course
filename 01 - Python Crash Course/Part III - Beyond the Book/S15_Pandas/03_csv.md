## DataFrame from CSV File

Frequently, we receive data in the form of a CSV file. Pandas provides the
`read_csv()` function to load a `DataFrame` from a CSV file.

For this example, I have included a [data.csv](./data/data.csv) file.

---

### Load DataFrame from CSV

Let's load and print the `DataFrame`

```python
import pandas as pd

print(f"Loading data from data.csv:")
df = pd.read_csv("./data/data.csv")
print(df)
```

Output:

```
Loading data from data.csv:
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
..        ...    ...       ...       ...
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4

[169 rows x 4 columns]
```

Notice that the default string representation truncates the data if there 
are more than ten rows, showing only the first and last five.

---

### Showing All the Data

There are a couple of different ways to show all the data.

Note: I will omit the output from these items to save space.

#### Convert to String

```python
# -- SNIP --

print(df.to_string())
```

---

#### Set Max Rows

```python
# -- SNIP --

pd.options.display_max_rows = 200
print(df)
```

---