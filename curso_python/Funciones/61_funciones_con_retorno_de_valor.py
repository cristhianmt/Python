"""
Funciones con retorno de valor
"""


def multiplicacion(num_1, num_2):
    resultado = num_1 * num_2
    return resultado  # retorna un valor a multiplicaion


print(multiplicacion(3, 4))  # con un print se puede llama la funcion con retorno

mult = multiplicacion(5, 5)  # o se puede almacenar
print(f"\n {mult}")


def prueba():
    return "Hola", 1, [2, 3, 4, 5]


print(prueba())

resulltado = prueba()
print(f"\n{resulltado}")
