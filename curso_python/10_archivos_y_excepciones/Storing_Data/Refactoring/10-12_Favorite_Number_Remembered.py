"""
10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
"""
import json

filename = "number_10-12.json"

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = int(input("What's your favorite number? "))
    with open(filename, 'w') as f:
        json.dump(number, f)
        print(f"We'll remember your {number}!!")

else:
    print(f"Your favorite number is: {number}")