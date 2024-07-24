print("Chapter 9:")
print("Exercise 2 - Creating and Using Multiple Instances of a Class")

class Dog:
    """This is a simple model for a dog"""
    # The Python class constructor uses the '__init__' keyword
    def __init__(self, name, age):
        """Initialize a new instance of the Dog class"""
        # We initialize the attributes (name and age)
        self.name = name
        self.age = age

    # We create a function to simulate the dog sitting
    def sit(self):
        """Tell the Dog to sit"""
        print(f"{self.name.title()} is now sitting.\n")

    # We create a function to simulate the dog rolling over
    def roll_over(self):
        """Tell the Dog to roll over"""
        print(f"{self.name.title()} has rolled over.\n")

# You can create as many instances of a class as you need
my_dog = Dog("willie", 6)
your_dog = Dog("lucy", 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()
