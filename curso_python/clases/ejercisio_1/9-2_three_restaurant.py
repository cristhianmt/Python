'''9-2. Three Restaurants: Start with your class from Exercise 9-1.
Create three different instances from the class,
and call describe_restaurant() for each instance.
'''

print("\n9-2 Three Restaurant")

class Restaurant:
    def __init__(self, name, cusine):
        self.name = name
        self.cusine = cusine

    def describe_restaurant(self):
        print(f"{self.name} serve wonderful {self.cusine} food")

    # Method
    def open_restaurant(self):
        print(f"The restauran {self.name} is open, Come in!!")

print()
mexican_restaurant = Restaurant('Los Primos', 'Mexican')
mexican_restaurant.describe_restaurant()

print()
italian_restaurant = Restaurant('Lucrezio Di Pasta e Vino','Italian')
italian_restaurant.describe_restaurant()

print()
spain_restaurant = Restaurant('Casa de Castilla','Spain')
spain_restaurant.describe_restaurant()