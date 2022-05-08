"""
contruir un programa que simule l funcionamiento de una calculadora que pueda realizar cuatro operaciones
artimeticas basicas (suma, resta, multiplicaion y division), el usuario debe especificar la operacion con el primer
caracter del nombre de la operacion
"""

a = float(input("Digite su primer numero: "))
b = float(input("Digite su segundo numero: "))
letra=str(input("""Que opcion desea tomar
S.suma
R.resta
M.multipliacion
D.division
Diguite su opcion: """)).lower()

if letra=='s':
    c=a+b
    print(f"Su suma es: {c}")
elif letra=='r':
    c=a-b
    print(f"Su resta es: {c}")
elif letra=='m':
    c=a*b
    print(f"Su multiplicaion es: {c:2f}")
elif letra=='d':
    c=a/b
    print(f"Su division es: {c:2f}")
else:
    print("Opcion invalida")