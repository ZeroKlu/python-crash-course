print("Chapter 9:")
print("Exercise 6 - Overriding Parent Class Methods")

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

    def fill_gas_tank(self):
        """Set the gas tank to full"""
        self.fuel_level = 1

    def check_fuel_level(self):
        """Check the fuel level"""
        fuel_state = "empty"
        if self.fuel_level == 1.0:
            fuel_state = "full"
        elif self.fuel_level >= 0.75:
            fuel_state = "three quarters full"
        elif self.fuel_level >= 0.5:
            fuel_state = "half full"
        elif self.fuel_level >= 0.25:
            fuel_state = "one quarter full"
        elif self.fuel_level > 0.0:
            fuel_state = "running on fumes"
        print(f"Fuel Status: {fuel_state}\n")


class ElectricCar(Car):
    """Defines an Electric Car as a subclass of Car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the ElectricCar class"""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Describe the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    # Here we are overriding the fill_gas_tank() and check_fuel_level() methods from the parent class
    # If the object is an ElectricCar, this will execute instead of the parent function

    def fill_gas_tank(self):
        """Set the gas tank to full"""
        print("This car doesn't have a gas tank!")

    def check_fuel_level(self):
        """Check the fuel level"""
        print("This car doesn't contain any fuel!\n")

my_car = Car("dodge", "challenger", 2014)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank()
my_car.check_fuel_level()
        
# We create an instance of the child class
my_nissan = ElectricCar("nissan", "leaf", 2024)

# We have all of the attributes and functions from the parent class
print(my_nissan.get_descriptive_name())

# We also have the attributes and functions specific to the child class
my_nissan.describe_battery()

# These are overridden in the child class
my_nissan.fill_gas_tank()
my_nissan.check_fuel_level()
