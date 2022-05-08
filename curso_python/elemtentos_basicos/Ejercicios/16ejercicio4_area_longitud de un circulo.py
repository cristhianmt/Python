"""Hacer un prgrama para ingresar el radio de un circulo
y se reporte su area y la longitud de la circunferecnia
"""

print("""IMOPRTAR MODULOS 
import math 
area=math.pi*radio**2
longitud=2*math.pi*radio
""")
import math #importa el modulo math
radio=float(input("\nDigite el radio del circulo: "))
area=math.pi*radio**2
longitud=2*math.pi*radio
print(f"\nEl are es: {area:.2f}")#despues del resultado se imprimira en pantalla 2 decimales
print(f"La longitud es: {longitud:.2f}")#despues del resultado se imprimira dos decimales


print("""\n\nOTRA MANERA DE IMPORTAR MODULOS 
from math import pi
area=pi*radio**2
longitud=2*pi*radio
""")
from math import pi
radio=float(input("\n Digite el radio del circulo: "))
area=pi*radio**2
longitud=2*pi*radio
print(f"\nEl are es: {area:.2f}")#despues del resultado se imprimira dos decimales
print(f"La longitud es: {longitud:.2f}")#despues del resultado se imprimira dos decimales