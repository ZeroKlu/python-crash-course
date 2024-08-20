## Decorator Arguments

We can even design decorators that accept arguments.

---

### Example

Let's modify the `power()` function from our first closure example:

```python
def power(exp: int) -> callable:
    """Generates a decorator (applying a non-local value for the exponent)"""
    def _power(func: callable) -> callable:
        """Calls the inner function, passing the function to execute"""
        def _inner_power(*args: list[int]) -> int:
            """Executes the called function, modifying its value n to be n ** exp"""
            base = func(*args)
            return base ** exp
        return _inner_power
    return _power
```

We've wrapped an additional outer function layer around the original function.
This allows us to accept the exponent as an argument in the decorator.

---

### Usage

Here, instead of storing the closure in a variable, we'll use it to decorate 
another function definition.

```python
@power(2)
def square(n: int) -> int:
    """Square an integer (using a decorator function)"""
    return n

@power(3)
def cube(n: int) -> int:
    """Cube an integer (using a decorator function)"""
    return n
```

Note how the functions just return `n` without performing a computation. This
is because the decorator's closure `_inner_power()` is doing the math.

---

### Testing

Let's test the functions:

```python
for n in range(1, 6):
    print(f"{n}² = {square(n):>2} : {n}³ = {cube(n):>3}")
```

Output:

```
1² =  1 : 1³ =   1
2² =  4 : 2³ =   8
3² =  9 : 3³ =  27
4² = 16 : 4³ =  64
5² = 25 : 5³ = 125
```

Now that's some powerful programming!

---
