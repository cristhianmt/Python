"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint

class Die:
    '''Represent a die, wich ca be rolled'''
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        '''Return a number between 1 and the number of sides'''
        return randint(1, self.sides)


d6= Die(6)
results = []
for roll_die in range(10):
    result = d6.roll_die()
    results.append(result)
print(f'\n 10 rolls of 6-sided die: ')
print(results)


d10 = Die(10)
results = []
for roll_die in range(10):
    result = d10.roll_die()
    results.append(result)
print(f'\n 10 rolls of 10-sided die: ')
print(results)


d6 = Die(20)
results = []
for roll_die in range(10):
    result = d6.roll_die()
    results.append(result)
print(f'\n 10 rolls of 20-sided die: ')
print(results)