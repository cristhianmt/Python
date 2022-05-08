'''
llenar una lista con los numero del 1  al 10, luego modificar los elementos
de la lista multiplicandolos por un valor qu el usuario difite
'''

print("\nUtilizando un indice externo para la multiplcaion con ")
#crear y agregar elementos a la lista
lista=list(range(1,11))
#mostra la lista
print("Lista original")
for i in lista:
    print(i,end="-")
#modificar los elementos de la lista
valor=int(input("\nDigite un valor a multiplicar: "))
#multiplicar todos los elementos por el valor utilizando un indice externo
indice=0
for i in lista:
    lista[indice]*=valor
    indice+=1
#mostrar lista modificada por el usuario
print("\nLista modificada por el valor, indice externo")
for i in lista:
    print(i,end="-")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


print()
print("\nUtilizando un indice interno para la multiplcaion con 'enumarate' ")
#crear y agregar elementos a la lista con un indice externo
lista=list(range(1,11))
#mostra la lista
print("Lista original")
for i in lista:
    print(i,end="-")
#modificar los elementos de la lista
valor=int(input("\nDigite un valor a multiplicar: "))
#multiplicar todos los elementos por el valor utilizando un indice interno
for indice, i in enumerate(lista):
    lista[indice]*=valor
#mostrar lista modificada por el usuario
print("\nLista modificada por el valor, indice interno")
for i in lista:
    print(i,end="-")
