## Ch 2 - Lesson 1: "Hello World" with a Variable

### The Zen of Python

[Tim Peters](https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer)),
the creator of the TimSort algorithm and a significant contributor to the
Python language, created a set of 19 guiding principles for developing
programs. These principles influenced the design of Python, and code that
adheres to them is referred to as "Pythonic."

You can read the principles by following these steps:

In your terminal, execute the following command:

```
python
```

This will take you into the Python interpreter, which you can recognize by
the appearance of the Python prompt: `>>>`

At the Python prompt, execute the following command:

```
import this
```

That command will display this:

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

When you're done, be sure to return to your normal command prompt by
executing the following command:

```
exit()
```

---

### Some Code Conventions

#### Comments

Any line of code staring with `#` + a whitespace character is a comment

```python
# This is a comment
print("I created a comment!")
```

---

#### Variable Naming

Rules:

* Only use ASCII characters
* May contain letters, numbers, and underscores
* May not start with a number
* May not contain spaces
* Should not use Python reserved words
* Avoid "l" and "O" which may be mistaken for "1" and "0"
* Except where specifically recommended, avoid upper-case letters

---

Conventions:

`snake_case` is used for
* modules and packages
* variables
* method/function names

`PascalCase` is used for
* class names
* type variables
* exceptions (also append "Error")

`ALL_CAP_SNAKE_CASE` is used for
* "constants"<br>Note: Python doesn't have constants, so this is just a 
  convention to warn the programmer not to modify a variable

`camelCase`
* Not used in Python standards

`kebab-case`
* Not used in Python standards

---

### Using a Variable in "Hello World"

Instead of just passing the string value "Hello World" to the `print()`
function, we can store the value in a variable.

In Python, the syntax for declaring a variable is `name = value`

```python
# Store the value in a variable
message = "Hello World"

# Print the value from the variable
print(message)
```

Result:

```
Hello World
```

---

We can modify a variable by assigning a different value to it

```python
message = "Hello World"
print(message)

# Assign a new value to the variable
message = "Goodbye World"
print(message)
```

Result:

```
Hello World
Goodbye World
```

---
