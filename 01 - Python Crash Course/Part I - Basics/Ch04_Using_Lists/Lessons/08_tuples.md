## Tuples

A `tuple` in Python is essentially an immutable list.

To distinguish that a collection is a tuple in stead of a list, we use 
parentheses instead of square brackets when we initialize the variable.

---

### Declaring and Accessing Elements

Elements in a tuple can be read by index just like elements in a list.

```python
coords = (1, 3)
print(f"x: {coords[0]}, y: {coords[1]}")
```

Output:

```
x: 1, y: 3
```

---

### Immutability

Unlike lists, tuples are immutable. You cannot add, remove, or modify items
after the tuple is initialized.


```python
coords = (1, 3)
coords[0] = 2 # TypeError occurs here
```

Output:

```
TypeError: 'tuple' object does not support item assignment
```

---

Although tuples cannot be mutated, they can be replaced/reinitialized.

```python
coords = (1, 3)
coords = (2, 3)
print(f"x: {coords[0]}, y: {coords[1]}")
```

Output:

```
x: 2, y: 3
```

---

### Pseudo-Constants

A tuple can have just one value, but the value must be followed by a comma.

Some developers use these single-value tuples to create pseudo-constant
variables. They aren't truly constant, but the immutability of an initialized
tuple helps prevent inadvertent modification of data.
```python
x = (2,)
y = (3,)
print(f"x: {x[0]}, y: {y[0]}")
```

Output:

```
x: 2, y: 3
```

---

### Looping

You can loop across a tuple, just like a list

```python
dimensions = (3, 4, 5)
for d in dimensions:
    print(d)
```

Output:

```
3
4
5
```

---

### Unpacking

Tuples are especially well suited to being deconstructed using multiple 
assignment (we call this "unpacking").

```python
coords = (1, 3)
x, y = coords
print(f"x: {x}, y: {y}")
```

Output:

```
x: 2, y: 3
```

---

### Zipping Lists

You can join two lists into a single list of tuples using the `zip()` 
function.

This takes the elements at each index in the lists and creates a tuple to 
populate at that index in a new list.

```python
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
tuples = zip(letters, numbers)
print(list(tuples))
```

Output:

```
[('a', 1), ('b', 2), ('c', 3)]
```

---
