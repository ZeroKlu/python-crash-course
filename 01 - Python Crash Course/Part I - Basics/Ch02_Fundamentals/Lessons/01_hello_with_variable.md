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

### Interpreted, Not Compiled

Many programming languages are compiled to machine language (the 
non-human-readable CPU instructions for a given architecture) before they are 
executed.

Python, by contrast, is interpreted, not compiled*. This means that a 
separate program (the Python interpreter) reads your code line-by-line and 
creates the machine instructions on-the-fly while executing.

> *Note: As we'll see later (when we create and import our own modules),
> there are times where Python is partially compiled (to bytecode) before
> being used.

This has advantages, in that your code will run until it encounters a runtime
error, so it can be easy to tell where something when awry.

However, there are also limitations. For example, because the code has to 
run on the interpreter and be compiled on-the-go, Python can be slower than
some compiled languages. Additionally, with a compiled language, you might
identify errors earlier than you can with Python, since those languages
separate runtime errors from compile-time errors. Other than errors in your
syntax, Python only has errors during runtime.

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

A variable is just a name for some place in memory where you have stored a
value*. It is much more convenient for the programmer to be able to access
values by name rather than trying to keep track of the various memory 
locations where the actual data is stored.

> *Note: This is an over-simplification. There's a lot more going on under
> the covers in variables, and eventually you'll need to understand ideas
> like the `stack` and the `heap`, `pointers`, `mutability`, etc. For now,
> though, it's accurate enough, and it explains how a coder uses variables.

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

### Changing the Value of a Variable

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

### Variables and the `NameError`

In Python, like most languages, both the spelling and capitalization of
variable names matters.

This code will result in an error:

```python
message = "Hello Python Crash Course reader!"
print(mesage)
```

Output:

```
Traceback (most recent call last):
  File "...\hello.py", line 20, in <module>
    print(mesage)
          ^^^^^^
NameError: name 'mesage' is not defined. Did you mean: 'message'?
```

---
