#tuplas
"""son listas inmtables, no s epueden modificar y eliminar
pero hay una manera de modificarlo y es converti la tupla a lista
las tuplas son mas rapidas y no consumen mucho espacio
"""

tupla=(4,"hola",4.5,[1,2,3],4)

print(tupla.index(4.5))#se subica en que posicion esta

print("\n",tupla.count(4))#cuntas veces hay un elemento

tupla=(4,"hola",4.5,[1,2,3],4)
lista=list(tupla)
lista.append(7)
tupla=tuple(lista)
print(type(tupla), tupla)