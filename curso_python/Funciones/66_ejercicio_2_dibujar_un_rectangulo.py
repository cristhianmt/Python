'''
Ejercicio 2
Hacer u programa que pida la anchura y altura de un rectangulo y con ayuda de una funcion
lo dibuje con *
ancho = 7
alto = 3

********
********
********
'''
def dibujar(ancho, alto):
    for i in range(alto):
        for j in range(ancho):
            print('*',end="-")
        print()
ancho=int(input("Digite el ancho: "))
alto=int(input("Digite el alto: "))

dibujar(ancho, alto)