"""
9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 100 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range.

"""

# Parent Class
class Car:
    """A simple attempts to represent a car.""" # Intento
    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Display infromation about the car"""
        long_name = f" {self.year} {self.make} {self.model}  "
        return long_name

    def read_odometer(self):
        print(f"this ca has {self.odometer} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll the odometer")

    def increment_odometer(self, miles):
        self.odometer +=  miles


# Child Class
class Electric_car(Car):
    """ Represent aspects of a car, specific to electric car"""
    def __init__(self, make, model, year):
        """Initialize attributes of parent class"""
        # con la funcion super es una funcion especial que le permite llamar a un metodo desde la clase padre
        super().__init__(make, model, year)
        self.battery = Battery()       #Se llama a la clase Battery


    def fill_gas_tank(self):
        """Electric car don't have gas tank """
        print("This car don't need a gas tank!")


class Battery:
    '''A simple attempt to model a battery for an electric car'''

    def __init__(self, battery_size=60):
        '''Initizalize the battery's attributes. '''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f"This battery has {self.battery_size}-kwh battery.")

    def get_range(self):
        '''Print a statement about the range this battery provides '''
        if self.battery_size == 70:
            range = 230
        elif self.battery_size == 85:
            range = 295
        print(f"This car can go about {range} miles on a full  charge")

    def upgrade_battery(self):
        if self.battery_size == 60:
            self.battery_size = 85
            print(f"Upgrade the battery to 85 kwh ")
        else:
            print(f"The battery is ready Upgrade  ")

print("Make an electric car, and check the battery:")
my_tesla = Electric_car('tesla', 'model x', 2020)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nUpgrade the battery a second time:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()