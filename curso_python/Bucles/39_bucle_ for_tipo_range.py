#el bucle for tipo range se le dice que haga un numero especifico de repeticiones

#el conteo i comineza siempre desde cero
for i in range(10):
    print(i,"hola")

print("\ncon el ciclo for range podemos recir que desde un numero hasta otro numero imprima")
for i in range(0,5):
    print(i,"hola")

print("\nmostar los numero pares desde el 2 hasta el 20")
for i in range(2,21,2):#son el tercer valor en el range se pone que saltara de dos en dos
    print(i,end=", ")

print("\nmostar los numero pares desde el 20 hasta el -2")
for i in range(20,-4,-2):#se imprimira al reves de dos en dos
    print(i,end=", ")

