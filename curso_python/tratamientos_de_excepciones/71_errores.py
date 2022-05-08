'''
Ecepciones
Son errores y existen dos bloques de errores

1. el primero son errores ocasionados por el programador
2. el segundo son errores ocasionados por el usuario

'''

print("""linea 10
print('Hola amigo' #SyntaxError
prin('Hola amigo)  #NameError
""")

print("""\n linea 15
if 15> 10   #SyntaxError
    print('Es mayor')""")

print("\n Error semantico")
print("""linea 21
lista=[1,2,3]
lista.pop()      #IndexError 
lista.pop()
lista.pop()
lista.pop()
print(lista)
podemos corregirlo con u while""")
lista=[1,2,3]
while len(lista)>0:
    print(lista.pop())
print(lista)

print("""
para acceder a un elemento de una lista
""")

print("\nErrores provocados por el usuario")
numero = int(input("Digite un numero: "))
print(F"la suma es= {numero+10}")