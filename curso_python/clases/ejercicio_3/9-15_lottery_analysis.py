"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket.
Write a loop that keeps pulling numbers until your ticket wins. Print a message
reporting how many times the loop had to run to give you a winning ticket.
"""

from random import choice

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # We don't want to repeat winning numbers or letters, so we'll use a
    #   while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't
        #   already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the
    #   winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the ticket if it hasn't already
        #   been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")



print("\n\n my code")

from random import choice

"""Create a funtion abot gettein_winning_ ticket"""


def get_wiinin_ticket(possibilities):
    winning_ticket = []
    while len(winning_ticket) < 4:
        results = choice(possibilities)
        if results not in winning_ticket:
            winning_ticket.append(results)
    return winning_ticket

def our_ticket(possibilities):
    my_ticket = []
    while len(my_ticket) < 4:
        results =  choice(possibilities)
        if results not in my_ticket:
            my_ticket.append(results)
    return my_ticket

def chances_to_win(play, winning_ticket):
    for elements in play:
        if elements not in winning_ticket:
            return False
    return True


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_wiinin_ticket(possibilities)

plays = 0
won = False
rounds = 1_000_000

while not won:
    new_ticket = our_ticket(possibilities)
    won = chances_to_win(new_ticket, winning_ticket)
    plays += 1
    if plays >= rounds:
        break

if won:
    print(f'the winning ticker is {winning_ticket}'.title())
    print(f'our ticker is {new_ticket}'.title())
    print(f'its took {plays} to win'.title())