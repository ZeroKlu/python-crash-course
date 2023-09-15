# Definition of a prime number:
#    Any positive integer that has exactly two integer factors: 1 and itself
#    * Since 1 only has one factor (itself), it is the unit number, not a prime number
#    * All other non-prime positive integers are called composite numbers
#    * 0 is neither positive nor negative, so it is also not a prime number
#    * To test that our algorithm is correct, it is known that there are 9,592 primes from 1 to 100,000

# This is the least efficient algorithm

# We aren't yet up to the chapter on importing modules, but I am using this module for the timer
import time

# We aren't yet up to the chapter on functions, but this is easier to demonstrate with one
# In my test, this ran for 19.63 seconds
def is_prime(n):
    # By definition, 1 is not a prime (neither are any non-positive integers)
    if n < 2:
        return False
    # 2 is prime
    if n == 2:
        return True
    # Check if any number 2 or greater is a factor of n
    for d in range(2, n):
        if n % d == 0:
            return False
    # If we found no factors, n is prime
    return True

min = 1
max = 100_000
primes = []
t0 = time.time()
for n in range(min, max + 1):
    if is_prime(n):
        primes.append(n)
t1 = time.time()
print(f"Found {len(primes)} prime numbers between {min} and {max}:")
print(f"----------------------------------------------------------\n{primes}")
print(f"\n----------------------------------------------------------\nElapsed time: {t1 - t0}\n")
