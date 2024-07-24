print("Chapter 9:")
print("Exercise 4 - Modifying Class Attributes")

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

# Create an instance
my_new_car = Car("dodge", "challenger", 2014)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Here we are calling the attribute modifying method
my_new_car.set_odometer(14_000)
my_new_car.read_odometer()

# We can also just modify the attribute directly
my_new_car.odometer_reading = 15_000
my_new_car.read_odometer()

# Validating the functionality of our "no roll back" logic
my_new_car.set_odometer(14_000)
my_new_car.read_odometer()

# Create another instance
my_used_car = Car("ford", "thunderbird", 1978)
print(my_used_car.get_descriptive_name())

# Set the initial mileage
my_used_car.set_odometer(140_000)
my_used_car.read_odometer()

# Update the mileage with miles driven since previous setting
my_used_car.increment_odometer(200)
my_used_car.read_odometer()
