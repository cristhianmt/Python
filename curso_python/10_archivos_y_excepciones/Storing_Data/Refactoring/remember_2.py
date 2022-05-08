"""
Refactoring , refactorizar hace que el codigo se mas limpio y tenga un orden
"""
import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username_1.json'
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
    filename = 'username_1.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greer_user():
    """Greet the  user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}")
    else:
        username = get_new_user()
        print(f"We'll remember you when you come back, {username}!")

greer_user()
