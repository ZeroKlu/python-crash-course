## Creating a List and Accessing Values

Lists are ordered collections of items.

Items in Python lists do not need to be of the same data type.

---

### Syntax

* Surround a list with square brackets `[]`
* Separate items with commas `,`<br>
  e.g.:<br>
  ```python
  numbers = [1, 2, 3, 4, 5]
  number_names = ["one", "two", "three"]
  ```

---

### Indexing
                 
List indices are zero-based and allow backward-indexing, so:

* First item is `list_name[0]`
* Last item is `list_name[-1]`

---

### Examples

```python
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[1].title())
print(bicycles[-2].upper())

message = f"My favorite bicycle was a {bicycles[0].title()}."
print(message)
```

Output:

```
['trek', 'cannondale', 'redline', 'specialized']
trek
specialized
Cannondale
REDLINE
My favorite bicycle was a Trek.
```

---
