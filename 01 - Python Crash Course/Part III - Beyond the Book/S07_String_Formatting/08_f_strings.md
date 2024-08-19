## Python Formatted Literals (f-strings)

The most recent major enhancement to string formatting is formatted literals
(or *f-strings*), added in Python v3.6.

Often referred to as *string interpolation* (or variable substitution/
expansion), f-strings allow us to place variable names and/or expressions
directly in curly braces in a string, replacing the necessity of placeholders.

If we compare the different eras of string formatting, it's easy to see that
f-strings result in more easily readable code.

Consider these three identical formatted strings:

```python
item, qty, price = "bananas", 5, 0.39
total = round(price * qty)

# string-modulo operator
s = "%d %s cost $%f" % (qty, item, total)

# `string.format()` function
s = "{} {} cost ${}".format(qty, item, total)

# f-string
s = "{qty} {item} cost ${total}"
```

In each case the result value in `s` is:

```
5 bananas cost $1.95
```

But with the inline variable names, the f-string is far and away the easiest 
to understand.

---

### Simple Example

Here's a simple example

```python
name = "World"
f_string = f"Hello, {name}!"
print(f_string)
```

Output:

```
Hello, World!
```

---

### Multiple Variables

Here's an example with multiple variables

```python
item, qty, price = "bananas", 5, 0.39
total = round(price * qty)
f_string = "{qty} {item} cost ${total}"
print(f_string)
```

Output:

```
5 bananas cost $1.95
```

---

### Converting Dates

Like string formatting, f-strings support using the conversion operator to
specify the `str()` or `repr()` string...

```python
now = datetime.now()
print(f"{now!s}")
print(f"{now!r}\n")
```

Output:

```
2024-08-18 12:22:23.902714
datetime.datetime(2024, 8, 18, 12, 22, 23, 902714)
```

---

### Replacing Invalid Characters

... or the `ascii()` string for that matter.

```python
invalid_string = "Thisö stringö hadö invalidö charactersö."
print(f"{invalid_string!a}")
```

Output:

```
'This\xf6 string\xf6 had\xf6 invalid\xf6 characters\xf6.'
```

---
