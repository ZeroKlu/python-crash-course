print("Chapter 9:")
print("Exercise 3 - Default Class Attributes")

class Car:
    """Defines a car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the Car class"""
        self.make = make
        self.model = model
        self.year = year
        # This attribute is set by default (not included in the constructor arguments)
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Describe the car"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Get the odometer mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

# Create an instance
my_new_car = Car("dodge", "challenger", 2014)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
