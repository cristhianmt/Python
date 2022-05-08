"""
Solicitar el nombre del usuario
"""

import json
username = input("What's your name: ")
filename = "username.json"
with open(filename, "a") as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")