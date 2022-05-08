print("importing a module into a module")

"""A set of classes  that can  be used to represent electric car """
from car import Car

# Child Class
class ElectricCar(Car):
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

    def __init__(self, battery_size=100):
        '''Initizalize the battery's attributes. '''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f"This battery has {self.battery_size}-kwh battery.")

    def get_range(self):
        '''Print a statement about the range this battery provides '''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full  charge")

