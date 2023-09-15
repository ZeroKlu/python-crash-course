print("Chapter 5:")
print("Exercise 1 - Handling Conditions")

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    # An if statement provides a code block to execute if a condition is met
    if car == "bmw":
        print(car.upper())
    # An else statement provides a code block to execute if the condition is not met
    else:
        print(car.title())

# It is important to understand that a condition is ANY expression that can be evaluated as TRUE or FALSE
