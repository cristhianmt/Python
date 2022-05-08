list=["Lunes","Martes","Miercoles","Jueves","Viernes",40,5.77,[1,2,3],True]
print(list)
print(len(list))#Imprime el numero de elementos en una lista

list=[1,2,4,5]
list.append(6)#agrega un nuevo elemento al final
print("\n",list)

list=[1,2,4,5,6]
list.insert(2,3)#insertar un elemento en la posicion elegida por el usauario
print("\n",list)

list=[1,2,3,4,5,6]
list.extend([7,8,9,10])#concatenar un elemento al final
print("\n",list)

list1=[1,2,3,4,5,6]
list2=[7,8,9,10,11]
list3=list+list2
print("\n",list3)#agregar una lista a otra lista

list=[1,2,3,4,5,6,"cristhian"]
print("\n",0 in list)#condicion de in en la cual dice si un elemento esta en una lista

list=[1,2,3,4,5,6,"cristhian"]
print("\n",list.index(5))#te regresa el elemtno que esta en el indice que marco el usuario

list=[1,2,3,4,5,6,"cristhian",1,2,3,4]#pueden haber valores repetidos
print("\n",list.count(1))#cuenta cuantos elementos se repite

""" remover elementos"""
list=[1,2,3,4,5,6,"cristhian"]
list.remove("cristhian") #elimina el elemento selccionado
print("\n",list)

list=[1,2,3,4,5,6,"cristhian"]
list.pop(3)#elimina el elemento seleccionado en el indice
print("\n",list)

list=[1,2,3,4,5,6,"cristhian"]
list.clear()#eliminar una lista completa
print("\n",list)



"""mostrar la lista al reves"""
list=[1,2,3,4,5,6,"cristhian"]
list.reverse()
print("\n",list)


"""copiar la lista"""
list=[1,2,3,4,5,6,"cristhian"]*2#se copia la lista
print("\n",list)

list=[2,1,3,5,4]
list.sort()#odenar los elementos en enteros del menor al mayor
print("\n",list)

list=[2,1,3,5,4]
list.sort(reverse=True)#odenar los elementos en enteros del mayor al menor
print("\n",list)

