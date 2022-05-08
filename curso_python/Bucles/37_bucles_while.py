#bucles while es un trozo de codigo que se repite varias veces loop
#existen dos tipos de bucles el while y el for

from math import sqrt

numero=int(input("Diguite un numero: "))
while numero<0:
    print("Error, debe ser un numero positivo")
    numero = int(input("Diguite un numero: "))

print(f"Su raiz cudrada es: {(sqrt(numero)):.2f}")

i=0
while i<10:
    print(i,"Hola mundo")
    i+=1
