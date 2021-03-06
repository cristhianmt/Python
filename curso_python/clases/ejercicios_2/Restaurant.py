"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""

# Parent Class
class Restaurant:
    def __init__(self, name, cusine):
        self.name = name.title()
        self.cusine = cusine.title()
        self.number_served = 0  # attribute


    #Method
    def describe_restaurant(self):
        print(f"{self.name} serve wonderful {self.cusine} food")

    #Method
    def open_restaurant(self):
        print(f"The restauran {self.name} is open, Come in!!")


    def set_number_served(self, number_served):
        self.number_served = number_served


    def increment_number_served(self, increment_ns):
        self.number_served += increment_ns


# Child Class
class Ice_Cream_Stand(Restaurant):
    '''A simple attempt (intento) to model an ice cream for '''

    def __init__(self, name, cusine_type='ice cream'):
        super().__init__(name, cusine_type)
        self.flavors = []

    def show_flavors(self):
        '''Display the flavors available'''
        print('We have the following flavor available')
        for flavor in self.flavors:
            print(f'{flavor}')



