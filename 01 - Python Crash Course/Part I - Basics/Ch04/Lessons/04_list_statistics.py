print("Chapter 4:")
print("Exercise 4 - List Statistics")

# This is here to enable the "mean" calculation in line 17
# Don't worry about this syntax for now. We'll learn this soon
import statistics

digits = list(range(0, 10))
print(digits)
print(f"List Length:  {len(digits)}")
print(f"Minimum:      {min(digits)}")
print(f"Maximum:      {max(digits)}")
print(f"Sum:          {sum(digits)}")
print(f"Average:      {sum(digits) / len(digits)}")

# if you import the statistics module, you can use the mean function instead of sum/len
# This has the advantage that it does not convert a whole number result to a float
tens = list(range(10, 101, 10))
print(f"\n{tens}")
print(f"Average:     {sum(tens) / len(tens)}")
print(f"Mean Average: {statistics.mean(tens)}")
