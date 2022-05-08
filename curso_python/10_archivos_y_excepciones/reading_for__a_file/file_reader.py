#open() Funtion es para abrir cualquier archivo y necesita ser nombrado el archivo
#para buscarlo
print('Leer un archivo en la misma carpeta, linea 4')
with open('pi_digits.txt') as file_objet: # with una vez abrira el archivo y lo nombrara con un as
    contents=file_objet.read() #read leera el archivo
print(contents)

print('\n')
# abre un archivo desde un directorio
print('Leer un archivo desde un directorio, linea 11')
with open('text_files/filename.txt') as file_object:
    contents = file_object.read()
print(contents)


print('\n')
#se puede abrir cualquir archivo desde un directorio solo invirtiendo las (\) a (/)
print('Leer un archivo desde una direccion completa usando /, linea 19')
file_path = '/Users/MR.MARK/Desktop/cumputacion/programacion/Python/curso_python/archivo_excepciones.txt'
with open(file_path) as file_objet:
    contents = file_objet.read()
print(contents)


print('\n')
#se puede abrir cualquir archivo desde un directorio con dobles (\\)
print('Leer un archivo desde una direccion completa usando //, linea 28')
file_path = '\\Users\\MR.MARK\\Desktop\\cumputacion\\programacion\\Python\\curso_python\\archivo_excepciones.txt'
with open(file_path) as file_objet:
    contents = file_objet.read()
print(contents)


print('\n')
print('Leer un archivo linea por linea, linea 35')
filename = 'pi_digits.txt'
with open(filename) as  file_objet:
    for line in file_objet:
        print(line)


print('\n')
print('Leer un archivo linea por linea pero con el formato rstrip(), linea 144')
filename = 'pi_digits.txt'
with open(filename) as  file_objet:
    for line in file_objet:
        print(line.strip())

print('\nAlmacenar cada linea en un bloque, linea 50')
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()#readlines toma cada line del archivo y la almacena en un una lista

for line in lines:      #usamos un bucle para imprimir cada linea de lineas
    print(line.rstrip())

