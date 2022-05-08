'''
llenar una lista con los numeros del 1 al 50, luego mostra la listacon un
buble for, los elementos deben mostrarse de la siguiente forma

1-2-3-4-5-6---50
'''

lista_while=[]

print("agregamos a la lista del 1 al 50 con while")
#agregamos los elementos a la lista
i=1
while i<=50:
    lista_while.append(i)
    i+=1

#imprimiendo los elementos de la lista
for i in lista_while:
    print(i,end="-")



print("\nagregamos los elementos en una sola linea de codigo pero solo numericos ")
#agregagar solo elemntos numerico a la lista
lista = list(range(1,51))

#imprimimos
for i in lista:
    print(i,end="-")