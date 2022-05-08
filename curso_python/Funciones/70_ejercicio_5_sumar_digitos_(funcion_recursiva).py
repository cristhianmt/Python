'''
Desarrrollar un programa que permita sumar los digitos de un
numero con ayuda de una funcion recursiva
ejemplo
entrada=123
salida=6
'''

def sumar_digitos(num):
    if num == 0:
        resultado = 0
    else:
        resultado = sumar_digitos(int(num / 10)) + (num % 10)
    return resultado
num = int(input('Digite el numero: '))

print(sumar_digitos(num))