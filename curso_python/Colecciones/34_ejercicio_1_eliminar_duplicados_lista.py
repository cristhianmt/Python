#escriba un programa donde tenga un lista y que, a continuacion, elimine los elementos rrepetidos, por ultimo
#mostrar la lista

#crear lista
lista=["alan","cristhian","mari","samuel","cristhian","cristhian",1,2,3,2,2,3]
print(lista)
#pasar una lista a un conjunto
conjunto=set(lista)
print(type(conjunto),conjunto)
#pasar un conjunto a una lista
lista=list(conjunto)
print(type(lista),lista)


print('''\npero lo podemos hace en una sola linea de codigo''')
#crear lista
lista=["alan","cristhian","mari","samuel","cristhian","cristhian",1,2,3,2,2,3]
print(lista)
lista=list(set(lista))
print(type(lista),lista)
