"""
Hacer un programa  que simule in cajero automatico con un salod inicial de
$1000 y tendra el siguente menu de operaciones
1.Ingresar dinero a la cuenta
2.retirar dinero de la cuenta
3.mostrar dinero disponible
4.salir
"""
dinero=int(input("""Operaiones que se pueden realiar
1.Ingresar dinero a la cuenta
2.retirar dinero de la cuenta
3.mostrar dinero disponible
4.salir
¿Que operacion desea realizar: """))
saldo=1000
if dinero==1:
    extra=float(input("Cuanto dinero desea ingrear: "))
    saldo+=extra
    print(f"Su dinero actual es: {saldo}")
elif dinero==2:
    retirar=float(input("Cuanto dinero desea retirar: "))
    if retirar<1000:
        saldo-=retirar
        print(f"Su dinero actual es: {saldo}")
    else:
        print("saldo insuficiente para retirar")
elif dinero==3:
    print(f"Su dinero actual es: {saldo}")
elif dinero==4:
    print("Buen dia")
else:
    print("Error al digitar la opcion")