## Ch 2 - Lesson 3: Examples of String Literals

In Python, a string (a series of characters) can be surrounded by either
double quotes (`"`) or single quotes (`'`)

Some languages distinguish between these two symbols, but in Python, they
can be used interchangeably.

---

### You can enclose a `"string"` in double-quotes

```python
message = "This is a string"
print(message)
```

---

### You can also enclose a `'string'` in single-quotes

```python
message = 'This is also a string'
print(message)
```

---

### Including double-quotes in your strings

When you enclose a string with single-quotes, double-quotes are 
automatically interpreted as literals

```python
message = 'I told my friend, "Python is my favorite language!"'
print(message)
```

---

However, when your string is enclosed in double-quotes, including a
double-quote in the string requires the use of an *escape sequence* `\"`

```python
message = "I told my friend, \"Python is my favorite language!\""
print(message)
```

---

### Including single-quotes in your strings

When you enclose a string with double-quotes, single-quotes are 
automatically interpreted as literals

```python
message = "The language 'Python' is named after Monty Python, not the snake."
print(message)
```

---

As above, when your string is enclosed in single-quotes, including a
single-quote in the string requires the use of an *escape sequence* `\'`

```python
message = 'The language \'Python\' is named after Monty Python, not the snake.'
print(message)
```

---
