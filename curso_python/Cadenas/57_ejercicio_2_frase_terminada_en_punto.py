'''
Hacer un programa para detectar su una frase introducida por el usuario finaliza
con un punto "." o no. Dberas imprimir  por consola una de las siguientes opciones
"Termina con un punto" o por el contrario "No termina con el punto"
'''

frase=input("Digite su frase: ")

if frase.endswith("."):#si el ultimo caracter de cadena termina con un "."
    print("Termina con un punto")
else:
    print("No termina con un punto")
