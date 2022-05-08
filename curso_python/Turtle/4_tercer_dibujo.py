import turtle as t

t.setup(600, 600)
t.shape('turtle')
t.color('#DE1860')

#un po  uito de programacion estructurada

def rectangulo(px, py, ancho, alto):
    # Nos posiionamos en la esquina superior derecha
    # del rectangulo que vamos a dibujar sin dejar rastro
    # y miramos hacia la izquierda para empesar siempre igual
    t.penup()
    'metodo llamado goto se le pasa una cordenada con una x y "y" '
    t.goto(px + ancho / 2, py + alto / 2)
    t.seth(180) # simpre le dice que mire hacia un determinado angulo sin poner varios left()
    t.pendown()
    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)
    t.forward(ancho)
    t.left(90)
    t.forward(alto)

rectangulo(0, 0, 400, 300)
rectangulo(0, 0, 300, 200)
rectangulo(0, 0, 200, 100)
rectangulo(0, 0, 100, 50)

t.exitonclick()