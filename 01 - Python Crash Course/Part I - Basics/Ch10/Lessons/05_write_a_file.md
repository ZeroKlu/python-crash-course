## Write a File

Of course, file interaction would be meaningless without the ability to create,
write, and edit files.

For this lesson, you'll need to create a path to a file that doesn't exist.

My code uses the relative path `.\Files\programming.txt`

> Note: the process to obtain file paths is covered here:  
> [00_bonus_relative_paths.md](./00_bonus_relative_paths.md)

---

### How to Search for a Pattern in a File

Select the edition of the textbook you're using below to see the relevant
lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### Setting the Mode with `open()`

When using the `open()` function, you can specify one of several modes in this
form:  
`open(file_path, mode)`

|Code|Mode|Description|
|:-:|-|-|
|`r`|read|open the file as read-only<br>This is the default mode if the argument is omitted|
|`w`|write|open the file as write-only - any existing data will be replaced|
|`a`|append|open the file and write to the end - any existing data will be retained|
|`r+`|read/write|open the file to both read and write|

There are also a couple of important rules to follow:

* The `TextIOWrapper` doesn't expose a `write_line` method, so you need to
  append your own newline characters.
    * e.g.: `file.write("some line\n")`
* Only strings can be written to file, so numerical data must be converted 
  first.
    * e.g.: `file.write(str(12345))`
* Write mode `w` will crete the file if it doesn't exist

---

### Writing the File

We will use this code to write the file

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "programming.txt")

with open(file_path, "w") as file:
    file.write("I love programming!\n")
    file.write("I love creating new games!\n")
```

### Verifying the File

After writing, we can use the technique we learned already to read the file and
verify that it contains the text we are expecting.

```python
# -- SNIP --

with open(file_path, "r") as file:
    print(file.read())
```

Output:

```
I love programming!
I love creating new games!
```

---

### Creating a `write_line` Function

Of course, since we know how to create functions now, it is relatively trivial
to create a `write_line()` function ourselves, so that we don't need to 
manually append newline characters every time we write to a file.

```python
def write_line(file_object, text):
    file_object.write(f"{text}\n")
```

Now we can perform our file writing (and verification) like this:

```python
# -- SNIP --

with open(file_path, "w") as file:
    write_line(file, "I love coding!")
    write_line(file, "I love creating new applications!")

with open(file_path, "r") as file:
    print(file.read())
```

Output:

```
I love coding!
I love creating new applications!
```

</details>

---

<details>
<summary>3rd Edition Method</summary>

### Using the `write_text()` Method

The `Path` type exposes a `write_text()` method that we can use to write to a
file.

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("programming.txt", "Files")

file = Path(file_path)

file.write_text("I love programming!\n")
```

And then we can verify the text we wrote.

```python
print(file.read_text())
```

Output:

```
I love programming!
```

---

### Creating a `write_line()` Function

Like we did with traditional files in the 2nd edition section, we can create
a `write_line()` function for ourselves.

```python
def write_line(path_object, text):
    path_object.write_text(f"{text}\n")
```

Then we can write to the file without appending a newline every time.

```python
# -- SNIP --

content = """I love programming!
I love creating new games.
I also love working with data."""

write_line(file, content)

print(file.read_text())
```

Output:

```
I love programming!
I love creating new games.
I also love working with data.
```

</details>

---
