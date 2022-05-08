
"""Call the funtion get_formatted_name from name_funtion file"""
from name_funtion import get_formatted_name

print("Enter 'q' at any time to quit.\n")

while True:
    first =  input("What's your first name: ")
    if first == 'q':
        break
    last = input("What's you last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"Neatly formatted name: {formatted_name}\n") # nombre con formato