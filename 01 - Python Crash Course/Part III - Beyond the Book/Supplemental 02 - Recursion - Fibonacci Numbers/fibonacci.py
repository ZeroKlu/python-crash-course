class CountCalls:
    def __init__(self, func):
        self._count = 0
        self._func = func
    def __call__(self, *args, **kwargs):
        self._count += 1
        return self._func(*args, **kwargs)
    @property
    def call_count(self):
        return self._count

# The Fibonacci sequence is defined thus:
# - For all non-negative integers:
#   F(0) = 0
#   F(1) = 1
#   F(n) = F(n-1) + F(n-2)

@CountCalls
def fibonacci_recursive(n):
    if n in [0, 1]:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

@CountCalls
def fibonacci_recursive_cached(n, cache = {0: 0, 1: 1}):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_recursive_cached(n - 1, cache) + fibonacci_recursive_cached(n - 2, cache)
    return cache[n]

@CountCalls
def fibonacci_iterative(n):
    values = [0, 1]
    for i in range(2, n + 1):
        values.append(values[i - 1] + values[i - 2])
    return values[-1]

@CountCalls
def fibonacci_formulaic(n):
    if n in [0, 1]:
        return n
    phi = (1 + 5 ** 0.5) / 2
    return int((phi ** n - (1 - phi) ** n) / (phi - (1 - phi)))

