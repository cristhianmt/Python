"""
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
"""

while True:
    print("Enter 'q' to quit")
    try:
        num_1 = input("\nGive me the first number: ")
        if num_1 == 'q':
            break
        num_1 = int(num_1)

        num_2 = input("Give me the second number: ")
        if num_2 == 'q':
            break
        num_2 = int(num_2)

    except ValueError:
        print("Sorry i need a number!!\n")
    else:
        sum = num_1+num_2
        print(f"The result is: {sum}")

