'''
Hacer un programa que determine si una palabra o frase es palindroma
Una cadena oalindroma se lee igual de izquierda a derecha que de
deracha a izquierda.

Ejemplo:
oso
reconocer
anita lava la tina
'''

cadena = input("Digite la palabra: ")
#primero quitamos los espacios en blaco en la cadena
cadena=cadena.replace(" ","")
#invertir la cadena
cadena_2=cadena[::-1]#copiando la cena invertida
print(f"\nLa cadena invertida es: {cadena_2}")
if cadena==cadena_2:
    print("\nEs una palabra palindroma")
else:
    print("\nNo es una palabra polindroma")