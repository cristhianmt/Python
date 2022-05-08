'''
hacer un programa que simule  un cajero automatico con un saldo
inicial de $1000 y tendra el siguiente menú de opciones:

1.Ingresar dinero a la cuenta
2.Retirar dinero de la cuenta
3.Mostar dinero disponible
4.salir
'''

saldo_inicial=1000

while True:
    opcion=int(input('''
            1.Ingresar dinero a la cuenta
            2.Retirar dinero de la cuenta
            3.Mostar dinero disponible
            4.salir
            Digite su opcion: '''))

    if opcion ==1:
        extra=int(input("Cuanto dinero desea ingresar: "))
        saldo_inicial+=extra
        print(f"Su dinero actual es:${saldo_inicial}")
    elif opcion==2:
        retirar=int(input("Cuando dinero desea retirar: "))
        if retirar<saldo_inicial:
            saldo_inicial-=retirar
            print(f"Su dinero altual es: ${saldo_inicial}")
        if retirar>saldo_inicial:
            print("Saldo insuficiente para retirar")
    elif opcion==3:
        print(f"Su saldo es: ${saldo_inicial}")
    elif opcion==4:
        print(" \n\"Gracias po usar nuestro servicio\" ")
        break
    else:
        print("Se equivico de opcion")
