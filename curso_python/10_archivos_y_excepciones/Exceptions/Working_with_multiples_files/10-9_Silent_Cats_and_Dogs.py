"""10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
"""
filenames = ["cats_1.txt","dogs_2.txt"]

while True:
    print("Enter 'q' to quit")
    pet= input("Enter cat [1] or dog [2]: ")
    if pet == 'q':
        break
    elif pet == '1':
        name_cat = input("What's your name cat: ")
        if name_cat == 'q':
            break
        else:
            with open(filenames[0], 'a') as f:
                f.write(f"{name_cat}\n")
    elif pet == '2':
        name_dog = input("What's your dog name: ")
        if name_dog == 'q':
            break
        else:
            with open(filenames[1], 'a') as f:
                f.write(f"{name_dog}\n")
    else:
        print("Incorret opction")

filenames = ["cats_1.txt","dogs_2.txt", "michi.txt"]

for files in filenames:
    try:
        with open(files) as f:
            contents = f.read()
        print(f"\nRead the file {files}\n{contents}")
    except FileNotFoundError:
        pass