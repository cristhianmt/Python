"""
10-13. Verify User: The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person who
last used the program.
Before printing a welcome back message in greet_user(), ask the user if
this is the correct username. If it’s not, call get_new_username() to get the correct
username.
"""

import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'verify_user.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_user():
    """Prompt for a new username."""
    username = input("What's your name? ")
    filename = 'verify_user.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greer_user():
    """Greet the  user by name"""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back {username}")
        else:
            username = get_new_user()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_user()
        print(f"We'll remember you when you come back, {username}!")


greer_user()
