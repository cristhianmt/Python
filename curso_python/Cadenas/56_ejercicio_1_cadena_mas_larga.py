'''
Hacer un programa donde debera imprimir por la consola  la palabra
con mas caracteres de do palabras dadas. En el caso de que ambas Palabras tengan
la misma cantidada de caracteres, deberas mostrar el mensaje "son iguales"
'''


cadena_1 = input("Digite la primera cadena: ")
cadena_2 = input("Digite la egunda cadena: ")



if len(cadena_1) > len(cadena_2):
    print("\nla cadena uno es mayor")
elif len(cadena_2) > len(cadena_1):

    print("\nLa cadena 2 es mayor")
elif len(cadena_1) == len(cadena_2):
    print("\nAmbas cadenas son iguales de longitud")