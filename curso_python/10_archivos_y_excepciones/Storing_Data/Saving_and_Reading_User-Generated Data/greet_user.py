"""
Saludaremos al usuario que hemos agregados a la lista
username
"""
import json
filename = "username.json"
with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back {username}!")
