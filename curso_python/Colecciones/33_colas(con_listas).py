"""
colas primero en entrar primero en salir
es importando el modulo _collections

pero hay otra forma pero mas rapida
"""
cola=["maria","cristhian","alan"]
#agreagar mas elementos
cola.append("samuel")
cola.append("raul")
print(cola)

#sacando elemento por el principio de la cola

n=cola.pop(0)
print(f"\n:atendiendo a  {n}")
print(cola)

n=cola.pop(0)
print(f"\n:atendiendo a  {n}")
print(cola)

n=cola.pop(0)
print(f"\n:atendiendo a  {n}")
print(cola)

n=cola.pop(0)
print(f"\n:atendiendo a  {n}")
print(cola)

n=cola.pop(0)
print(f"\n:atendiendo a  {n}")
print(cola)



"""importar el modulo _collections"""

from _collections import deque
