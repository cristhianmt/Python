"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
five letters. Randomly select four numbers or letters from the list and print a
message saying that any ticket matching these four numbers or letters wins a
prize.
"""

from random import choice

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b','c', 'd', 'e']
win = []
while len(win) < 4:
    pulled_item = choice(lottery)
    if pulled_item not in win:
        print(f'We pulled  a { pulled_item}!')
        win.append(pulled_item)

print(f'the win ticker is :{win}'.title())
