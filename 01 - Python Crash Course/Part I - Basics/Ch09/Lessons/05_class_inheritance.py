print("Chapter 9:")
print("Exercise 5 - Class Inheritance")

class Car:
    """Defines a car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the Car class"""
        self.make = make
        self.model = model
        self.year = year
        # This attribute is set by default (not included in the constructor call)
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Describe the car"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Get the odometer mileage"""
        print(f"This car has {self.odometer_reading} miles on it.\n")

    # We can create a method to handle modifying an attribute
    def set_odometer(self, mileage):
        """Set the odometer mileage"""
        # Let's prevent anyone from "rolling back" the odometer
        if mileage >= self.odometer_reading:
            print(f"Setting odometer to {mileage}")
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # We can take the attribute's existing value into account when modifying it
    def increment_odometer(self, miles=1):
        """Increment the odometer mileage"""
        if miles > 0:
            self.odometer_reading += miles
            print(f"Updated odometer to {self.odometer_reading}")
        else:
            print("You can't add negative miles!")


# When inheriting a class, include the name of the parent class in parentheses in the child or 'sub' class definition
# This will model the specifics of an electric car in addition to the properties already existing on the Car class
class ElectricCar(Car):
    """Defines an Electric Car as a subclass of Car"""

    # We still need to include the initialization function
    def __init__(self, make, model, year):
        """Initialize a new instance of the ElectricCar class"""
        # But (importantly), any attributes inherited from the parent class need to be initialized there
        # For this, we call the 'super()' method to identify the parent or 'super' class
        super().__init__(make, model, year)
        # Now we can initialize all of the child class's non-inherited attributes
        self.battery_size = 75

    def describe_battery(self):
        """Describe the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")


# We create an instance of the child class
my_nissan = ElectricCar("nissan", "leaf", 2024)

# We have all of the attributes and functions from the parent class
print(my_nissan.get_descriptive_name())

# We also have the attributes and functions specific to the child class
my_nissan.describe_battery()
