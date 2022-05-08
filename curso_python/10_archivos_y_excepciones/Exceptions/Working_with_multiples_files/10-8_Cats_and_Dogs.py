"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block
executes properly.
"""

filename1 ="cats.txt"
filename2 ="dogs.txt"

while True:
    print("Enter 'q' to quit")
    pet = input("What animal do you have cat [1] or dog [2]: ")
    if pet == 'q':
        print("Thaks")
        break
    if pet == '1':
        name_cat = input("What's your cat name: ")
        if name_cat == 'q':
            print("Thaks")
            break
        else:
            with open(filename1, 'a') as f: #f= file_object
                f.write(f"{name_cat} \n")
    elif pet == '2':
        name_dog = input("What's your dog name: ")
        if name_dog == 'q':
            print("Thaks")
            break
        else:
            with open(filename2, 'a') as f:  # f= file_object
                f.write(f"{name_dog} \n")

filenames = ["cats.txt", "dogs.txt", "cumbion.txt"]
# Open each file with
for files in filenames:
    print(f"Read {filenames}")
    try:
        with open(files) as f:
            contents = f.read()
        print(f"Read {files}\n{contents}")
    except FileNotFoundError:
        print(f"Sorry the file {files} does not exist.")