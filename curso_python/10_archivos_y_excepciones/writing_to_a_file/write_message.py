"""
read mode ('r')
write mode ('w')
append mode ('a')
or a mode that allows
you to read and write to the file ('r+').
"""

filename = 'programming.txt'
#in open() The first "filename" arguments is the file we eant to open
#the second 'w' argument tell to python that we want to open the| file in write mode
#be carful if the file exist withi 'w' python rewrite
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

with open(filename) as file_object:
    read = file_object.read()
print(read)

