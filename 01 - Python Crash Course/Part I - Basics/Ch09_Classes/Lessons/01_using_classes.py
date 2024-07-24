# A class represents a conceptual thing and encapsulates its attributes and functions
# Modeling items in this way is the fundamental concept underlying object-oriented programming (OOP)

print("Chapter 9:")
print("Exercise 1 - Creating and Using a Class")

class Dog:
    """This is a simple model for a dog"""
    # The Python class constructor uses the '__init__' keyword (see lesson 15 for deeper discussion)
    def __init__(self, name, age):
        """Initialize a new instance of the Dog class"""
        # We initialize the attributes (name and age)
        # Note the syntax: self.<<variable>> to make the value a global member (attribute) of the class
        self.name = name
        self.age = age

    # We create a function to simulate the dog sitting
    def sit(self):
        """Tell the Dog to sit"""
        print(f"{self.name.title()} is now sitting.")

    # We create a function to simulate the dog rolling over
    def roll_over(self):
        """Tell the Dog to roll over"""
        print(f"{self.name.title()} has rolled over.")

# Create an instance (which calls the '__init__' constructor)
my_dog = Dog("willie", 6)

# Access the class attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Call the class functions
my_dog.sit()
my_dog.roll_over()
