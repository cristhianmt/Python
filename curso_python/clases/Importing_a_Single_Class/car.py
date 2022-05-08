"""A class that can be used to represent a car."""
# Parent Class
class Car:
    """A simple attempts to represent a car.""" # Intento
    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        """Display infromation about the car"""
        long_name = f" {self.year} {self.make} {self.model}  "
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"this car has {self.odometer_reading} miles on {self.model}")

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll the odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer +=  miles





