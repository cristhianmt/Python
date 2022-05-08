
"""funcion aleatorio de numeros randit
devuelve un numero aleatorio"""
print('randit funtion'.title())
from random import randint
print(randint(1,6))

"""esta funcion toma una lista o una tupla
y regrea un elemento escogido al azar"""
print('\nchoice funtion'.title())
from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

print('''\nel modulo random no se deberia usar cuando se construye aplicaciones 
relacionadas con la seguridad ''')