'''
Hacer un rograma que pida un numero por teclado y gurade en una lista su tabla de multiplicacion
hasta el 10
Por ejemplo si se digita el 5 la lista tendra:
5 10 15 20 25 30 35 40 45 50
'''
#pedir el usuario un numero
valor=int(input("Digite un valor a multuplicar: "))

lista=[]
#agregamos los elementos a la lista
#multiplicando el valor
for i in range(1,11):
    lista.append(i*valor)

print("\nTabla de multiplicr\n",lista)