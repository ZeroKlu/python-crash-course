## Recursion

Recursion occurs when a function calls itself. That may sound weird, but there
are many scenarios where a recursive algorithm is the most sensible approach to a problem, including:

* Sorting Algorithms
* Traversing Complex Data Structures Like Trees  
  and famously...
* The Fibonacci Sequence

---

### What is the Fibonacci Sequence?

The Fibonacci Sequence is a mathematical sequence with the following 
properties:

* `F(0) = 0`
* `F(1) = 1`  
  and for all other non-negative integers:
* `F(n) = F(n-1) + F(n-2)`

You can see that for integers larger than one, the formula defining the 
Fibonacci Sequence is recursive even before we implement any code. By
definition, we have to call the formula to solve the formula.

> Note: An interesting property of the Fibonacci Sequence is that as *n*
> gets larger, F(*n*) / F(*n*-1) approaches phi (φ), the golden ratio:  
> F(*n*) / F(*n*-1) ≈ φ ≈ 1.618

---

### A Couple of Warnings about Recursion

As developers, we need to be careful how we structure a recursive function for
two main reasons:

1. Function calls get costly in terms of memory and CPU usage when we make a
   lot of them.
2. In Python, there is a maximum number of calls that can be on the recursion
   stack at a given time. By default, this is `1000`, and we can check the
   max recursion depth with the following code:

```python
import sys

print(sys.getrecursionlimit())
```

Output:

```
1000
```

We can change this value using the `sys.setrecursionlimit()` function, but
I recommend against this. If your recursive algorithm requires a dept of more
than 1000, you should redesign the algorithm, not the environment.

---

### A Little Setup

I have provided a special class known as a decorator in the following:

<details>
<summary>The CountCalls Class</summary>
<br>

In [count_calls.py](./count_calls.py)

```python
class CountCalls:
    """Class to allow counting the times a recursive function is called"""

    def __init__(self, func: callable):
        """Initialize"""
        self._count = 0
        self._func = func

    def __call__(self, *args, **kwargs):
        """Magic method override to add to counter and execute function"""
        self._count += 1
        return self._func(*args, **kwargs)
    
    @property
    def call_count(self):
        """Number of times the recursive function has been called"""
        return self._count
```

</details>
<br>

This class can be applied to a recursive function as a decorator as follows,
giving the function a property `call_count` that represents the number of 
times the function was called while processing the recursive algorithm.

```python
from count_calls import CountCalls

@CountCalls
def recursive_function():
    ...

count = recursive_function.call_count
```

---

### A Naive Algorithm

We can approach this naively and just directly translate the Fibonacci formula
to code:

```python
from count_calls import CountCalls

@CountCalls
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (naive algorithm)"""
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = 40
print(f"Calculated F({n}) = {fibonacci(n):,}")
print(f"call_count = {fibonacci.call_count:,}")
```

Output:

```
F(40) = 102,334,155
call_count =  331,160,281
```

> Note: You may have to wait several minutes for this computation to complete.

Holy cow! It took over two minutes and over 300 million recursive calls to
compute  
`F(40) = 102,334,155`

Why did it take so long?

---

### Wasted Recursive Calls

The big problem is that we made the exact same calculations many times. Let's
take a look at a simpler example `F(5)` and see where the wasted calls come 
in.

Only when `n < 2` does a call return a value without spawning additional
calls.

The initial call spawns two recursive calls

* `F(5) = F(4) + F(3)` (+2 calls)

Each of those two calls spawns two more

* `F(4) = F(3) + F(2)` (+2 calls)
* `F(3) = F(2) + F(1)` (+2 calls)

Looking at those four calls:

* `F(3) = F(2) + F(1)` (+2 calls)
* `F(2) = F(1) + F(0)` (+2 calls)
* `F(2) = F(1) + F(0)` (+2 calls)
* `F(1) = 1`

Then, we have to resolve those six additional calls:

* `F(2) = F(1) + F(0)` (+2 calls)
* `F(1) = 1`
* `F(1) = 1`
* `F(0) = 0`
* `F(1) = 1`
* `F(0) = 0`

We still have two more calls:
* `F(1) = 1`
* `F(0) = 0`

Looking at all of the resolved calls, we get:  
`F(5) = 1 + 1 + 1 + 0 + 1 + 0 + 1 + 0 = 5`

And it took us 15 calls to the function to figure that out, but when we list
out the values of *n* passed to the function and how many times each was
passed, we see:

|*n*|calls|
|:-:|:-:|
|5|1|
|4|1|
|3|2|
|2|3|
|1|5|
|0|3|

We calculated `F(3)` twice, and `F(2)` three times, and so on.

We're wasting calls recalculating values we've already computed, and that
problem gets more severe the larger *n* becomes.

In fact, this increases in what we call exponential time where the number of
calls required to compute any `F(n)` is (worst case) `2ⁿ` function calls.

Surely we can do better...

---

### Storing Previously Computed Values (Memoization)

That's not a typo, by the way, *memoization* is a process of storing the
previously computed values in a *memo* (short for *memorandum* - Latin: "to
be remembered") and then retrieving existing values instead of recomputing them.

Let's come up with a way to store the computed values as we go and improve our
function.

```python
from count_calls import CountCalls

@CountCalls
def fibonacci(n: int, memo: dict[int, int]={0: 0, 1: 1}) -> int:
    """Return the nth Fibonacci number (memoized algorithm)"""
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

n = 40
print(f"Calculated F({n}) = {fibonacci(n):,}")
print(f"call_count = {fibonacci.call_count:,}")
```

Output:

```
F(40) = 102,334,155
call_count =  79
```

This time, our call finished in under a second and only required 79 calls: 
once to store each number and once to retrieve it to get to the next number.

As *n* increases, `2 * n` becomes a lot smaller than `2ⁿ`. We're now getting
answers in linear time.

> Note: One interesting tidbit about Python is that if we initialize a mutable
> variable as a default value in a function signature, it will only 
> initialize one time. After that, if I call this function again, after I
> have already used it once, the memo will still contain the previous 
> calculation's values, so it becomes more efficient the more it is used 
> during the program's execution.

---

### Do I Have To Use Recursion?

Short answer: No.

For any recursive algorithm, there is always a way to complete the same task
iteratively (using a loop, e.g.) without needing recursion. Sometimes, though,
the iterative algorithm may be much more complicated.

That's not the case with the Fibonacci Sequence, so here is an iterative
solution (in the interest of completeness):

```python
from count_calls import CountCalls

@CountCalls
def fibonacci_iterative(n: int) -> int:
    """Return the nth Fibonacci number (iterative algorithm)"""
    values = [0, 1]
    for i in range(2, n + 1):
        values.append(values[i - 1] + values[i - 2])
    return values[-1]

n = 40
print(f"Calculated F({n}) = {fibonacci(40):,}")
print(f"call_count = {fibonacci.call_count:,}")
```

Output:

```
F(40) = 102,334,155
call_count =  1
```

Even though we're only making one call, we're still doing the a similar 
amount of work (since the loop iterates *n* times), but it does eliminate
recursion.

---

### Any Other Options?

There's a mathematical formula to compute an approximation of a Fibonacci
number, that will allow us to reduce the number of operations to just a few
calculations, where the number of computations doesn't increase at all as
*n* gets larger.

> Warning: Because this computes an approximation for any `n > 50`, the 
> returned answer may be incorrect, so only use this for relatively small
> values of *n*.

Formulae:  
`φ = (1 + √5) / 2` (φ is the golden ratio)  
`F(n) = (φⁿ - (1-φ)ⁿ) / (φ - (1-φ))`  (φ is used in calculating F(n))

```python
from count_calls import CountCalls

@CountCalls
def fibonacci(n):
    """Return the nth Fibonacci number approximation (formulaic algorithm)"""
    if n in [0, 1]:
        return n
    phi = (1 + 5 ** 0.5) / 2
    return int((phi ** n - (1 - phi) ** n) / (phi - (1 - phi)))

n = 40
print(f"Calculated F({n}) = {fibonacci(40):,}")
print(f"call_count = {fibonacci.call_count:,}")
```

Output:

```
F(40) = 102,334,155
call_count =  1
```

This completes in milliseconds, regardless how large *n* is (provided you have
enough memory to hold the resulting value for `F(n)`)

---

### Can I See This in Action?

All of the functions described above are in this file:

<details>
<summary>Fibonacci Functions</summary>
<br>

In [fibonacci_functions.py](./fibonacci_functions.py)

```python
from count_calls import CountCalls

@CountCalls
def fibonacci_recursive(n: int) -> int:
    """Return the nth Fibonacci number (naive algorithm)"""
    if n in [0, 1]:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

@CountCalls
def fibonacci_recursive_memo(n: int, cache: dict[int, int]={0: 0, 1: 1}) -> int:
    """Return the nth Fibonacci number (memoized algorithm)"""
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_recursive_memo(n - 1, cache) + fibonacci_recursive_memo(n - 2, cache)
    return cache[n]

@CountCalls
def fibonacci_iterative(n: int) -> int:
    """Return the nth Fibonacci number (iterative algorithm)"""
    values = [0, 1]
    for i in range(2, n + 1):
        values.append(values[i - 1] + values[i - 2])
    return values[-1]

@CountCalls
def fibonacci_formulaic(n):
    """Return the nth Fibonacci number approximation (formulaic algorithm)"""
    if n in [0, 1]:
        return n
    phi = (1 + 5 ** 0.5) / 2
    return int((phi ** n - (1 - phi) ** n) / (phi - (1 - phi)))
```

</details>
<br>

<details>
<summary>Fibonacci Runner Program</summary>
<br>

In [01_recursion.py](./01_recursion.md)

```python
import fibonacci_functions as fib

def print_menu() -> None:
    """Display the menu of algorithm options"""
    print("\nEnter one of the following options:")
    print("[R]ecursive Algorithm")
    print("[M]emoized Recursive Algorithm")
    print("[I]terative Algorithm")
    print("[F]ormula-Based Algorithm")
    print("[Q]uit")

def main() -> None:
    options = ["r", "m", "i", "f", "q"]

    while True:
        n = -1
        print_menu()
        option = ""
        option = input("\n> ")[:1].lower()
        if option not in options:
            print("Please enter a valid value!")
            continue
        else:
            while n < 0 and option != "q":
                try:
                    n = int(input("Enter a non-negative integer:\n> "))
                except:
                    continue
        if option == "r":
            # Call naive recursive function
            print(f"\nF({n}) = {fib.fibonacci_recursive(n):,}")
            print(f"Recursive calculation required {fib.fibonacci_recursive.call_count:,} function calls.")
        elif option == "m":
            # Call recursive function with memoization
            print(f"\nF({n}) = {fib.fibonacci_recursive_memo(n):,}")
            print(f"Cached recursive calculation required {fib.fibonacci_recursive_memo.call_count:,} function calls.")
        elif option == "i":
            # Call iterative function
            print(f"\nF({n}) = {fib.fibonacci_iterative(n):,}")
            suffix = "s"
            if fib.fibonacci_iterative.call_count == 1:
                suffix = ""
            print(f"Iterative calculation required {fib.fibonacci_iterative.call_count:,} function call{suffix}.")
        elif option == "f":    
            # Call formulaic function
            print(f"\nF({n}) = {fib.fibonacci_formulaic(n):,}")
            suffix = "s"
            if fib.fibonacci_formulaic.call_count == 1:
                suffix = ""
            print(f"Formula-based calculation required {fib.fibonacci_formulaic.call_count:,} function call{suffix}.")
        else:
            break

if __name__ == "__main__":
    main()
```

</details>
<br>

Run the code, and you can test all the algorithms for yourself:

```pwsh
python .\01_recursion.py
```

---
