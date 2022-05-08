#poligons regulares

import turtle as t
t.setup(600, 600)
t.shape('turtle')
t.color('#839192')

def poligono(px, py, radio, lados):
    t.penup()
    t.goto(px, py - radio)
    t.pendown()
    t.circle(radio)

    angulo= 360 / lados
    print(angulo)
    for i in range(lados):  #El rango es de 0 a n
        t.penup()           #Nos posicionamos en el centro
        t.goto(px, py)
        t.pendown()

        # Trazamos radios hacia afuera
        t.seth(angulo*i+1)            #los angulos se incrementaran hasta el rango pero le sumamos un porque comienza en
        t.forward(radio)
        print(t.pos())                #Se imprime las cordenadas
    pass


poligono(0, 0, 100, 7)


t.exitonclick()