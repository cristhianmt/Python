'''
Base
'''

import turtle as t             #cargamos el modulo Turtle y lo nombramos como t para mejores practicas

t.setup(600,600)               #Configuramos un espacio de dibujo tamaño de pixeles
t.shape('turtle')              #Le damos la forma de la tortuga
t.color('#48C9B0')             #le damos un color a la tortuga puede ser hexadecimal

print(t.pos())                 #La cordenada donde se encuentra la tortuga
# El codigo ira aqui
t.forward(250)                 #Metodo forward que sirve para moverse a la derecha
t.left(90)                     #Metodo left gira cualquier grado
t.forward(250)
print('Esquina superior derecha',t.pos())
t.left(90)
t.forward(500)
print('Esquina superior izquierda',t.pos())
t.left(90)
t.forward(500)
print('Esquina inferior izquierda',t.pos())
t.left(90)
t.forward(500)
print('Esquina inferior derecha',t.pos())

                   
t.exitonclick()