"""10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt."""

file_guest = "guest.txt"

name = input("what's your name: ")

with open(file_guest, 'w') as file_object:
    file_object.write(name)

with open(file_guest) as file_object:
    line = file_object.readline()
print(line)