## Ch 2 - Lesson 2: "Hello `name`" with User Input

### Get input from the user

Python allows you to accept text entered by the user via the `input()`
function:

```python
# Get the user's name
name = input("Please enter your name: ")
```

---

### Add the input to a greeting:

There are several ways to construct a string including the user input.

For each example, I will assume that the user entered `John` as the name

#### Concatenate the strings using the `+` operator:

```python
name = input("Please enter your name: ")
print("Hello " + name)
```

Output:

```
Hello John
```

---

#### Print multiple strings (separated by spaces) using `,` in `print()`:

```python
name = input("Please enter your name: ")
print("Hello", name)
```

Output:

```
Hello John
```

---

#### Using a formatted string

In Python 2, formatting a string required the use of the `format()` 
function, for which the syntax is as follows:

`some_string.format("{}", value_for_placeholder)`

```python
name = input("Please enter your name: ")
print("Hello {0}".format(name))
```

Output:

```
Hello John
```

---

#### Using f-Strings (Python 3.6+)

In Python v3.6, f-strings were introduced. These make reading a formatted
string much easier for the developer.

You can compare the Python f-string to the idea of string interpolation
in other languages.

```python
name = input("Please enter your name: ")
print(f"Hello {name}")
```

Output:

```
Hello John
```

> Digging Deeper:
> 
> In some scenarios, you may want to use the `format()` function instead of
> the f-string. This is because f-strings are evaluated whether or not they are
> used, while `format()` is not evaluated until/unless needed.
>
> An example of this would be a string that is only used if a condition is met.

---
