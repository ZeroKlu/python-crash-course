"""Assignment 6.7"""

# People: Start with the program you wrote for Exercise 6.1.
#         Make two new dictionaries representing different people, and
#         store all three dictionaries in a list called `people`. Loop
#         through your list of people. As you loop through the list,
#         print everything you know about each person.

print("Try-it-Yourself:")
print("Assignment 6.7")

person1 = { "first_name": "Scott", "last_name": "McLean", "age": 52, "city": "Lewisville" }
person2 = { "first_name": "Jeremy", "last_name": "McLean", "age": 47, "city": "Columbus" }
person3 = { "first_name": "Hillary", "last_name": "Taylor", "age": 50, "city": "Twinsburg" }
people = [person1, person2, person3]
for person in people:
    print()
    for key, value in person.items():
        print(f"{key} = {value}")
