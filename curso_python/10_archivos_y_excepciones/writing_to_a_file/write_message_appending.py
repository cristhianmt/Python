#appending file
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I also love finding meaning in large dataset,\n")
    file_object.write("I love creating new games,\n")
    file_object.write("I love creating apps that can run in the browser")
with open(filename) as file_object:
    read = file_object.read()
print(read)