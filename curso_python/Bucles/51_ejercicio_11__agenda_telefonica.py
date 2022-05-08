'''
Hacer un programa que simule una agenda de contactos. Crear
un diccionario donde la clave sea nombre del usuario y el valor
sea el telefono, el programa tendra el siguiente menu

1. Nuevo contacto
2. Borrar contacto
3. Ver contactos existentes
4. salir
'''

agenda = {}
while True:

    print(""" \tMenu
1. Nuevo contacto
2. Borrar contacto
3. Ver contactos existentes
4. salir""")
    opcion=int(input("Digite su opcion: "))

    print()
    if opcion==1:
        nombre = input("Digite el nombre del contacto: ")
        telefono=input("Digite el numero: ")
        if nombre not in agenda:
            agenda[nombre]=telefono
            print("Contacto agregado correctamente!!")
        else:
            print("Ese nombre de contacto ya exite")
    elif opcion==2:
        nombre = input("Digite el nombre del contacto: ")
        if nombre in agenda:
            del(agenda[nombre])
            print("Contacto eliminado")
        else:
            print("Ese contacto no existe")
    elif opcion==3:
        print("Agenda de contactos")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Telefono: {valor}")
    elif opcion==4:
        print("Gracias por utilizar el programa")
        break
    else:
        print("Opcion erronea")
    print()