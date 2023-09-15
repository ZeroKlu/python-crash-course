import math

for r in range(1, 11):
    circumference = round(2 * math.pi * r, 2)
    area = round(math.pi * r ** 2, 2)
    print(f"\nradius:        r   = {'{:.2f}'.format(r).rjust(6)} cm")
    print(f"circumference: 2πr = {str(circumference).rjust(6)} cm")
    print(f"area:          πr² = {str(area).rjust(6)} cm²")
