'''9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message
indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
'''

print("\n9-1 Class Restaurant ")


class Restaurant:
    def __init__(self, name, cusine):
        self.name = name
        self.cusine = cusine

    #Method
    def describe_restaurant(self):
        print(f"{self.name} serve wonderful {self.cusine} food")

    #Method
    def open_restaurant(self):
        print(f"The restauran {self.name} is open, Come in!!")

mexican_restaurant = Restaurant('Los primos', 'Mexican')
print(f"The Restaurant's name is { mexican_restaurant.name}")
print(f"The cuisine is { mexican_restaurant.cusine}\n")

mexican_restaurant.describe_restaurant()
mexican_restaurant.open_restaurant()