#Ejercicio1.1
"""
Determinar la solucion logica de la siguiente operacion

((3+5*8)<3  and ((-6/3 * 4) +2 < 2)) or (a>b)
    false   and      -6        < 2        or
    false   and         true              or
                false                     or
"""

a=float(input("\nDigite a: "))
b=float(input("\nDigite b: "))
resultado= ((3+5*8)<3 and (-6/3 * 4)+2<2) or (a>b)

print(f"El resultado es {resultado}")