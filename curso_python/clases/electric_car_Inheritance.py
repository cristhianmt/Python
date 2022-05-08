"""
Inheritance #Herencia

No siempre tiene que comenzar desde cero al escribir una clase. Si la clase
estás escribiendo es una versión especializada de otra clase que escribiste,
puedes usar la herencia. Cuando una clase hereda de otra, adquiere los atributos
y métodos de la primera clase. La clase original se llama clase padre, y la nueva
clase es la clase hija. La clase secundaria puede heredar cualquiera o todos los
atributos y métodos de su clase principal, pero también es libre de definir nuevos
atributos y métodos propios.
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
        print(f"this ca has {self.odometer_reading} miles on it")

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


my_tesla = Electric_car('tesla', 'model x', 2020)
print(my_tesla.get_descriptive_name())

#Defining Attributes and Methods for the Child Class
#my_tesla.describe_battery()

#Overriding Methods from the Parent Class
my_tesla.fill_gas_tank()

#Instances as Attributes
my_tesla.battery.describe_battery()  #manda a llamar a la clase Electric_car que esta a su ves llama a Battery

my_tesla.battery.get_range()

#Modeling Real-World Objects

