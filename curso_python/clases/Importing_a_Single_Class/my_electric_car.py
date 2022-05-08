print("Storing Multiple Classes in a Module")
from car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2020)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
