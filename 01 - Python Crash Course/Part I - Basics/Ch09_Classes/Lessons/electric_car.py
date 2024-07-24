"""A class module to define an electric car"""

# Because the superclass "Car" is defined in a separate module, we have to import it
from car import Car

class ElectricCar(Car):
    """ Define an electric car as a subclass of Car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the ElectricCar class"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Set the fuel level to full"""
        print("This car doesn't have a gas tank!")

    def check_fuel_level(self):
        """Get the fuel level"""
        print("This car doesn't contain any fuel!\n")


class Battery:
    """Define a battery"""

    def __init__(self, battery_size = 75):
        """Initialize a new instance of the Battery class"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the battery"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Get the battery range in miles"""
        range = "unknown"
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.\n")

    def upgrade_battery(self):
        """Upgrade the battery"""
        if self.battery_size < 100:
            self.battery_size = 100
            print("Upgraded battery.")
