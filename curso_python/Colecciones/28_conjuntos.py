#Conjuntos
"""
son coleccion donde los elementos estan desordenados, su principal carateristica es que no pueden estar duplicado
solo hay valores unico
"""
conjunto=set()
conjunto={1,2,3,"hola",1,2,3}#se pueden agregar diferentes valores y no se puede poner listas
print(conjunto)

conjunto={1,2,3,"hola",1,2,3}
conjunto.add(5)#agregar un elemento
conjunto.add(6)
print("\n",conjunto)

conjunto={1,2,3,"hola",1,2,3}
conjunto.discard("hola")#eliminar un elemento especifico
print("\n",conjunto)

conjunto={1,2,3,"hola",1,2,3}
conjunto.clear()#Eliminar un conjunto completo
print("\n",conjunto)

conjunto={1,2,3,"hola",1,2,3}
print("\n", 3 in conjunto )#buscar un conjunto
print("\n", 3 not in conjunto )#decir si un elemento no estan en un set

