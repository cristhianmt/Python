"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

filename = "programming_poll.txt"


while True:
    print("Enter 'q' to exist.")
    name = input("What's your name? ")

    if name == 'q':
        break
    else:
        ask = input("Why do you like programming? ")
        with open(filename, 'a') as file_object:
            file_object.write(f"{name} likes programming because: {ask} \n")
