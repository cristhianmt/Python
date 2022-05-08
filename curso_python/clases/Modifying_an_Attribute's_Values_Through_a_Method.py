print("\nModifying an Attribute's Values Through a Method, line 73")

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 10 #cuenta kilometrajes de un carro pero su valor comienza en 0

    def get_descriptive_name(self):
         '''Return a neatly formatted descriotive nale.'''
         long_name = f"{self.year} {self.make} {self.model}"
         return long_name

    def read_odometer(self):
        '''Printing a statement showing the car's mileage '''
        print(f"This car has {self.odometer_reading} miles on it ")

    def update_odometer(self, mileage):
        '''Set the odometer reading to given value.
        Reject the chance if it attempts to roll the odometer back'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(15)
my_new_car.read_odometer()