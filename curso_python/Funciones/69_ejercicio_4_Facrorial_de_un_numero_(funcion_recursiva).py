'''
Desarrollar un programa para calcular el factorial de un
numero con ayuda de una funcion recursiva
'''

def factorial(num):
    if num>0:
        resultado = num * factorial(num-1)
    else:
        resultado = 1

    return resultado

num=int(input('Digite un numero: '))
print(factorial(num))