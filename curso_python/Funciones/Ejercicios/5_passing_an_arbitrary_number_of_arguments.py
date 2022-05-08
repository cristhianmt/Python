''' Passing an Arbitrary Number of Arguments
a lo mejor no sabras cuantos argumentos tendra que aceptar una funcion por ejemplo,
una funcion que realice una pizza; debe aceptar x cantidad de ingredientes
pero no sabras cuantos ingrediente tendra que aceptar esa funcion
'''

print('Passing an Arbitrary Number of Arguments'.upper())
def make_pizza(*toppings): #El * le dice a python que haga una tupla vacia
    '''Print the list of topping that have been requested.'''
    print(type(toppings), toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers', 'extra cheese')


print('\nPrinting the topping whit a loop, line 15')
def make_pizza(*topping):
    '''Sumariza the pizza we are about to make'''
    print('Making a pizza whit the following topping')
    for x in topping:
        print(f'-{x}')
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers', 'extra cheese')

print('\nMaking positional'.upper())
print('Miking Positional and Arbitrary Arguments')
def make_pizza(size, *topping):
    '''Summarize the pizza we are about to make'''
    print(f'Making a {size}-inch pizza with the following toppings: ')
    for x in topping:
        print(f'-{x}')
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers', 'extra cheese')


print('\nUsing Arbitrary Keyword Arguments'.upper())
def build_profile(first, last, **user_info): # los ** dobles hacen que python cree un diccionario vacio
    '''Build a dictionary containin everything we know about a user'''
    user_info['First name'] = first
    user_info['Last name'] = last
    return user_info
user_profile = build_profile('albert','einstein',
                             location='princeton',
                             field='physics')
print(type(user_profile), user_profile)



print('\nExercises, line 50 '.upper())
'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that’s being ordered. Call the function three times, using a different number
of arguments each time.
'''
print('\n8-12 Sandwiches, line 56')
def sandwiches(*items):
    print('\nMaking sandwiches whit the following topping')
    for x in items:
        print(f'...adding {x} to your sandwiches')
sandwiches('bread','tomato','avocado', 'chitken')
sandwiches('bread','tomato','avocado', 'bistek')


'''
8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
'''
print('\n8-13 User Profile, line 71')
def buil_profile(first, last, **user_profile):
    user_profile['First name'] = first
    user_profile['Last name'] = last
    return user_profile
user_profile = build_profile('Cristhian', 'Martinez',
                             University='IPN',
                             Carrer='Computing scienci')
print(user_profile)


'''
8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was 
stored correctly.
'''
print('\n8-14 Cars, line 92')
def make_car(manufacturer, model_name, **information):
    'Make a dictionary'
    car_dict = {
        'Manufacturer' : manufacturer.title(),
        'Model car' : model_name.title()
    }
    for x, y in information.items():
        car_dict[x] = y
    return car_dict
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

my_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_accord)