import turtle as t
t.setup(600, 600)
t.shape('turtle')
t.color('#DE1860')

def poligono(px, py, radio, lados):
    # Desativamos el trazo
    t.penup()

    #Calculamos los angulos
    angulo=360 / lados
    print(angulo)

    #Creamos una lista para lamacenar los angulos
    vertice=[]
    for i in range(lados):
        t.goto(px, py)
        t.seth(angulo * i+1)
        t.pendown()
        t.forward(radio)
        vertice.append(t.pos())
    t.goto(vertice[-1])
    for j in vertice:
        t.goto(j)


    pass

poligono(0, 0, 200, 7)



t.exitonclick()