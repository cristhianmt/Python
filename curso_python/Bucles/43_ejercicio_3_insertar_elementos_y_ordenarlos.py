'''
pide numeros y metelos en una lista, cuando el usuario meta 0
ya dejara de insertar, por ultimo, muestra los numeros ordenados de menor a mayor
'''
#Crear lista vacia
lista=list()
#Agregar elemtos por el usuario
while True:
    valor=int(input("Digite el valor: "))
    if valor>0:
        lista.append(valor)
    elif valor==0:
        break
#Imprimir los elementos de la lista de menor a mayor
print("Lista ordenada:\n",sorted(lista))