print("Gime two numbers")
print("Enter to 'q' quit ")
while True:
    num_1 = input("Plase give me one number: ")
    if num_1 == 'q':
        break
    num_2 = input("Plase give me one more number: ")
    if num_2 == 'q':
        break
    try:
        answer = int(num_1) / int(num_2)
    except ZeroDivisionError:
        print("Yo can't divided by 0!")
    else:
        print(f"{answer:0.2f}")
