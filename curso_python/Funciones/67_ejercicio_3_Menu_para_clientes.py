'''
Ejercicio 3
Crear u programa que tenga una lista de clientes, cada cliente tienen su
Nombre, Apellidi e ID, el programa tendra el siguuiete menu de opciones:
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar clientes  por DNI
4. Eliminar clientes
5. Salir
'''
def agregar(opcion):
    cliente = {}
    id = input('Digite su Id: ')
    nombre = input('Digite el nombre: ')
    apellido = input('Digite su apellido: ')
    cliente['Id'] = id
    cliente['nombre'] = nombre
    cliente['apellido'] = apellido
    Clientes.append(cliente)

def mostrar_todos_clientes(opcion):
    for i in Clientes:
        print(f"Id:{i['Id']}. Nombre: {i['nombre']}, Apellido: {i['apellido']} ")

def mostrar_id(opcion):
    id = input('Digite su Id: ')
    for i in Clientes:
        if i['Id'] == id:
            print(f"Id:{i['Id']}. Nombre: {i['nombre']}, Apellido: {i['apellido']} ")
            return True
    return print('Id no escontrada')

def eliminar (opcion):
    valor = input('Digite su elemento a eliminar')
    for i in Clientes:
        if i['Id'] == valor:
            Clientes.remove(i)
            return print(f'Cliente {i} eliminado')
    return print("Cliente no encontrado")


Clientes = []
while True:
    opcion=int(input('''\t ....:MENU:....
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar clientes  por DNI
4. Eliminar clientes
5. Salir

Diguite su opcion: '''))
    if opcion == 1:
        agregar(opcion)
    elif opcion == 2:
        mostrar_todos_clientes(opcion)
    elif opcion == 3:
        mostrar_id(opcion)
    elif opcion == 4:
        eliminar(opcion)
    elif opcion == 5:
        break
    else:
        print("Opcion erronea")