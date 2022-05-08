"""
Refactoring , refactorazr hace que el codigo se mas limpio y tenga un orden
"""
import json
def greer_user():
    """Greet the  user by name"""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What's your name?")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back { username}")
greer_user()