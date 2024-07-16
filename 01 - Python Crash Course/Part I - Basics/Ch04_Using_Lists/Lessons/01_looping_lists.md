## Looping over Lists

If we look back at assignment 3.6, we spent a lot of time repeatedly printing 
the members of a list, one at a time.

That's really awful, and it violates the principle of not writing redundant 
code.

Wouldn't it be neat if we had a way to look at all the items in a list and 
repeat an instruction on each one?

Well, I have some good news for you!

### Iterating Lists with `for`

In Python a `for` loop is like a "foreach" loop in C#. The loop iterates over
the list, capturing each element and performing some task(s) with it.

The syntax is as follows:

```python
for item in collection:
    # Code to perform on each item
```

Across Python, a line ending in a colon indicates the start of a block 
containing indented lines below it.

> Note: Indents are required for code blocks and follow specific rules:
>
> * The indentation must always be the same throughout the Python file<br>
>   e.g.: four spaces is not the same as a tab character
> * Only indent inside a block
> * If a block contains another block, indent twice inside the inner block

---

### Examples

#### A simple loop with one statement in the block

```python
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    # Indented line executes on each loop iteration
    print(magician)
```

Output:

```
alice
david
carolina
```

---

#### A more thorough example

The code block within a `for` loop can contain multiple instructions.

A non-indented line following the loop is executed after the loop completes.

```python
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    # Indented lines execute on each loop iteration
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next one.\n")
# Non-indented line executes after the loop is complete
print("That was a great magic show!\n")
```

Output:

```
Alice, that was a great trick!
I can't wait to see your next one.

David, that was a great trick!
I can't wait to see your next one.

Carolina, that was a great trick!
I can't wait to see your next one.

That was a great magic show!
```

---
