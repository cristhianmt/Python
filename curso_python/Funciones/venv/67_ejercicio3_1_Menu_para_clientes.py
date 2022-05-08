'''
Ejercicio 3
Menu eficiente
Crear u programa que tenga una lista de clientes, cada cliente tienen su
Nombre, Apellidi e ID, el programa tendra el siguuiete menu de opciones:
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar clientes  por DNI
4. Eliminar clientes
5. Salir
'''
def agregar(id, nombre, apellido):
    cliente={}
    cliente['ID']=id
    cliente['Nombre']=nombre
    cliente['Apellido']=apellido
    Clientes.append(cliente)

def mostrar():
    for i in Clientes:
        print(f"ID: {i['ID']}, Nombre: {i['Nombre']}, Apellido: {i['Apellido']}")

def mostrar_por_i(id):
    for i in Clientes:
        if i['ID'] == id:
            print(f"ID: {i['ID']}, Nombre: {i['Nombre']}, Apellido: {i['Apellido']}")
        return True
    return False
def eliminar(id):
    for i in Clientes:
        if i['ID'] == id:
            Clientes.remove(id)
        return True
    return False

Clientes=[]
while True:
    opcion=int(input('''\t....:Menu:....
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar clientes  por DNI
4. Eliminar clientes
5. Salir

Digite su opcion: '''))
    if opcion == 1:
        id = input('Digite su ID: ')
        nombre = input('Digite su nombre: ')
        apellido = input('Digite su apellido: ')
        agregar(id, nombre, apellido)
    elif opcion == 2:
        mostrar()
    elif opcion == 3:
        id=input('Digite su ID: ')
        if mostrar_por_i(id):
            print('ID encontrada')
        else:
            print('ID no encontrada')
    elif opcion == 4:
        id=input('Digite su ID: ')
        if eliminar(id):
            print('ID eliminada')
        else:
            print('ID no enconrada')
    elif opcion == 5:
        print('Gracias por usar el sistema')
        break
    else:
        print('¡¡¡Se equivoco de opcion pendejo!!!')