"""
condicionales combinados
"""

edad=int(input("Digite sus edad: "))
if 0<edad<100:
    print("Edad correcta")
    if edad >=18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print("Edad incorrecta")
