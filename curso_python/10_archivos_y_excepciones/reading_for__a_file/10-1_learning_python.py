"""
10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can. . . . Save the file as learning_python.txt in
the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by
reading in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.
"""

print("\n-------------Reading in the entire file---------------------")
file_name = 'learning_python.txt'
with open(file_name) as file_object:
    lines = file_object.read()
print(lines)


print("\n-------------Looping over the lines---------------------")
pi_string = ''
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())



print("\n-------------Lines in a list ---------------------")

with open(file_name) as file_object:
    lines = file_object.readlines()#readlines toma cada line del archivo y la almacena en un una lista

for line in lines:      #usamos un bucle para imprimir cada linea de lineas
    print(line.rstrip())