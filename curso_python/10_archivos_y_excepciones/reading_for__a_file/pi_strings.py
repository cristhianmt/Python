#working with a file's contents
# imprimira en una sola line el texto pero con un espacio con el metodo readline()
print(" linea 4")
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))




print("metodo strip(), linea 19")
#pero tambien esta el metodo strip() en la cual remueve los espacios al principio y al fi nal
print('\n')
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))



#large Files: one million digits
print("\nopen a file with million  digits")
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(f'{pi_string[:53]}')          #podemos delimitar hasta donde se puede imprimir
print(len(pi_string))


print("\n")
## buscar en el archivo pi_million_digits si aparece mi cumpleaños
for line in lines:
    pi_string += line.strip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
     print('Your birthday appers in the first millions digits of pi!!')
else:
    print('Your  birthday does not apper in the firs digits op pi :c.')