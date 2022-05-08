import turtle as t
t.setup(600, 600)
t.shape('turtle')
t.color('#DE1860')

def poligono(px, py, radio, lados):
    t.penup()
    t.goto(px, py - radio)
    t.pendown()
    t.circle(radio)

    angulo = 360 / lados

    vertices = []                   #Creamos una lista para almacenar los puntos de los vertices

    for i in range(lados):
        t.penup()
        t.goto(px, py)
        t.pendown()

        t.seth(angulo*i+1)          #Trazamos los vertices hacia afuera
        t.forward(radio)
        vertices.append(t.pos())    #Se van añadiendo a la lista los vertices

    t.penup()
    t.goto(vertices[-1])             #Nos posicionamos en la primer cordenada del vertice
    t.pendown()
    for j in vertices:
        t.goto(j)

'''
Hacemos que la tortuga se meva mas rapido y dibujamos
'''
t.speed(200)
poligono(0, 0, 200, 7)

t.exitonclick()