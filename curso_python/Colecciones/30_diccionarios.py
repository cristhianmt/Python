#Diccionarios, sn desordenados
diccionario={
    "azul":"blue",
    "rojo":"red",
    "verde":"gren"
}
print("mostrar todos los elementos del diccionario: ",diccionario)

print("\nmostrar solo un elemento en especifico: ",diccionario["azul"])


diccionario["amarillo"]="yellow"
print("\nagregar nuevos elemntos al diccionari:",diccionario)

diccionario["azul"]="BLUE"
print("\ncambiar un elemento",diccionario)


del(diccionario["verde"])
print("\nelimnar un elemento",diccionario)


print("\nlos diccionarios aceptan cualquier tipo de dato")

diccionario={
    "cristhian":[23,1.70],
    "alan":[18,1.70],
    "samuel":[56,165]
}
print(diccionario)

print("\npara encontar una palabra clave")
if "samuel" in diccionario:
    print("si esta")
else:
    print("no esta")




print("\ndentro de un dicionario de puede poner otro diccionario")
diccionario={
    "cristhian":[23,1.70],
    "alan":{"edad":18,"estatura":1.70},
    "samuel":[56,165]
}


print("\nbuscar un elemento con un input")
x=str(input("digite el valor a busacar en el  diccionario: "))
if x in diccionario:
    print("si esta y el valor es:",diccionario[x])
else:
    print("no esta")

print("\no existe de otra manera mas contraida")

diccionario={
    "cristhian":[23,1.70],
    "alan":{"edad":18,"estatura":1.70},
    "samuel":[56,165]
}
x=str(input("digite el valor a busacar en el  diccionario: "))
print(diccionario.get(x,"No existe el valor"))

