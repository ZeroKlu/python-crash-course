## Using Slices to Copy Lists

An unbounded slice of a list creates a copy of the original list.

This can be very useful when you don't want to modify the original.

---

### Lists Assign by Reference

If we create a list and then assign it to a new variable, both variables are
pointing to the same list in memory.

```python
my_foods = ["pizza", "falafel", "carrot cake"]
print(my_foods)
other_foods = my_foods # Assignment is by reference
other_foods.append("gyros")
print(other_foods)
print(my_foods)
```

Output:

```
['pizza', 'falafel', 'carrot cake']
['pizza', 'falafel', 'carrot cake', 'gyros']
['pizza', 'falafel', 'carrot cake', 'gyros']
```

Appending a value to `other_foods` modified `my_foods`, since both are 
references to the same list.

---

### Slices Make Copies

But if we assign to a slice, we're creating the copy as a new list in memory.

```python
my_foods = ["pizza", "falafel", "carrot cake"]
print(my_foods)
other_foods = my_foods[:] # Unbounded slice makes a copy
other_foods.append("gyros")
print(other_foods)
print(my_foods)
```

Output:

```
['pizza', 'falafel', 'carrot cake']
['pizza', 'falafel', 'carrot cake', 'gyros']
['pizza', 'falafel', 'carrot cake']
```

Appending to the copied list did not modify the original.

---