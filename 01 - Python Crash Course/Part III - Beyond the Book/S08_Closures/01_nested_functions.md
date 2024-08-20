## Nested Functions

Inner (or nested) functions, also known as nested functions, are functions 
that you define inside other functions.

In Python, this kind of function has direct access to variables and names 
defined in the enclosing function. That is, the inner function shares all
items in the scope of the outer function (its environment).

Inner functions have many uses, most notably as closure factories and 
decorator functions.

---

### Simple Example

This is an oversimplified example, where the outer function simply declares
and executes the inner function.

```python
def outer_function() -> None:
    """Executes the inner function"""
    def inner_function() -> None:
        print("Hello World!")
    inner_function()

outer_function()
```

Output:

```
Hello World!
```

---

### Example With Variable in Scope

In this example, we'll pass a value to the outer function. Although it is not
passed in turn to the inner function, the inner function will still have 
access to the variable.

```python
def outer_function(name: str) -> None:
    """Executes the inner function (sharing variable 'name')"""
    def inner_function() -> None:
        print(f"Hello {name.title()}!")
    inner_function()

outer_function("Scott")
```

Output:

```
Hello Scott!
```

---
