'''
Hacer un programa que pida una cadena de por teclado, luego
meta los caracteres en una lista sin repetir caracteres
'''

cadena = input("Digite la palabra: ")

lista = []

for i in cadena:
    if i not in lista:# si el caracter aun no esta en la lista
        lista.append(i)#lo agregamos
print(lista)