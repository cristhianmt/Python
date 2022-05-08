import turtle as t

t.setup(600, 600)
t.shape('turtle')
t.color('#73C6B6')


def poligono(px, py, radio, lados):
    t.penup()
    angulo= 360/ lados
    print(angulo)
    vertices = []
    for i in range(lados):
        t.goto(px, py)
        t.seth(angulo * i+1)
        t.forward(radio)
        vertices.append(t.pos())
    t.goto(vertices[-1])
    t.pendown()
    for j in vertices:
        t.goto(j)

'''
Hacemos que la totuga se mueva mas rapido
'''
t.speed(200)
for n in range(3, 20): #ponemos en un rango los radios y los lados
    poligono(0,0,n*10,n)

t.exitonclick()