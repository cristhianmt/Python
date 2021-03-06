"""
Working with Classes and instances
"""

print("\nThe car Class")

class Car:
    '''A simple attempt to represent a car'''

    def __init__(self, make , model, year):
        "Initialize attributes to describe a car"
        self.make = make
        self.model = model
        self.year = year

    def  get_descriptive_name(self):
        '''Return a neatly formatted descriotive nale.'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

print('\nSetting a default value for an attribute, line 25')

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #cuenta kilometrajes de un carro pero su valor comienza en 0

    def get_descriptive_name(self):
         '''Return a neatly formatted descriotive nale.'''
         long_name = f"{self.year} {self.make} {self.model}"
         return long_name

    def read_odometer(self):
        '''Printing a statement showing the car's mileage '''
        print(f"This car has {self.odometer_reading} miles on it ")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()





