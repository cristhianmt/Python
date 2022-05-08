'''
Ejercicio 1
Desarrollar un programa que pueda calcular el valor del tipo de cambio
de moneda (de tu moneda - hacia el dolar y viceversa)
'''

def dolar_pesos(dolar):
    return dolar*20

def peso_dolar(peso):
    return peso/20

while True:
    print('''\t.:CAMBIO DE DIVISAS
1. Cambio de Dolar a Pesos Mexicanos
2. Cambio dePesos mexicanos Dolar
3. Salir''')
    opcion=input('\nDigite su opcion: ')

    if opcion == '1':
        dolar=float(input('Cuanto es la cantidad de dolares a cambiar: '))
        print(f"La cantidad de dolares a pesos es igual a= US${dolar_pesos(dolar):.2f} \n")

    elif opcion == '2' :
        peso=float(input('Cuanto es la cantidad de pesos a cambiar: '))
        print(f'La cantidad de pesos a dolar es= ${peso_dolar(peso):.2f} MN\n')
    elif opcion == '3':
        print('Gracias por usar el sistema\n')
        break
    else:
        print('Opcion incorrecta')