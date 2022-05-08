print("\nIncrementing an Attribute’s Value Through a Method")

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

    def update_odometer(self, mileage):
        '''Set the odometer reading to given value.
        Reject the chance if it attempts to roll the odometer back'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def imcrement_odometer(self, miles):
        '''Add the given amount to the odometer reading'''
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outbak', 2015)
print(my_used_car.get_descriptive_name())

print()
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

print()
my_used_car.update_odometer(100)
my_used_car.read_odometer()
