print("Chapter 4:")
print("Exercise 4 - List Statistics")

# This is here to enable the "mean" calculation in line 22
# Don't worry about this syntax for now. We'll learn this soon
import statistics

digits = list(range(0, 10))
print(digits)
print(f"List Length:  {len(digits)}")
print(f"Minimum:      {min(digits)}")
print(f"Maximum:      {max(digits)}")
print(f"Sum:          {sum(digits)}")
print(f"Average:      {sum(digits) / len(digits)}")

# If you import the statistics module, you can use the mean function instead of sum/len
# This has the advantage that it does not convert a whole number result to a float
tens = list(range(10, 101, 10))
print(f"\n{tens}")
avg = sum(tens) / len(tens)
print(f"Average:      {avg}")
mean_avg = statistics.mean(tens)
print(f"Mean Average: {mean_avg}")

# Of course, we could check this and clean up the value ourselves
# But this requires some syntax we won't encounter until chapters 5 and 8...
# calc_avg = int(avg) if (avg * 10) % 10 == 0 else avg
# print(f"Calc Average: {calc_avg}")
