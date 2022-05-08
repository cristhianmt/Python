"""
Fuciones
son bloques de codigo que estaran dentro de nuestros programas
y nos van a servir a nosotros para resolver un problema en especifico
y reutilizar el codigo cuantas veces queramos

Existen 
funciones sin retorno de valor
funciones con retorno de valor
"""


# en la funcion lo nombramos la accion que la funcion hara
def saludo():
    print("Hola Cristhian")


# llamar a una funcion
saludo()
# llamar la funcion cunatas veces quieramos
saludo()


# agragar parametros a la funcion
def saludo(nombre):  # parametro
    print(f"Hola {nombre}")


saludo("alan")
saludo("Cristhian")


def multiplicaion(numero):
    for i in range(1, 11):
        print(f"{numero} * {i} = {numero * i}")


multiplicaion(5)
print()
multiplicaion(2)
