#bulce for se le conoce por un determinado numero de ciclos

'''
puden inprimir lista, sets ,diccionarios

i es el numbre del iterador'''
for i in[1,2,3,4,5, "cristhian"]:
    print("elemento: ",i)

elemento=[1,2,3,4,5, "cristhian"]
for i in elemento:
    print(f"elemento:{elemento} ")

diccionario={
    "marca":"ford",
    "modelo":"raptor",
    "año":"2020",
    "color":"negro"
}


#i representara los elmentos
print("\nimprimir los elementos")
for i in diccionario:
    print(diccionario[i])

print("\nimprimir la clave con sus elementos")
for i in diccionario:
    print(f"{i}: {diccionario[i]}")

print("\nimprimir la clave con sus elementos pero mas profecional")
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")


diccionario="cristhian"
print("\nimprimir cadena con salto de linea")
#el elemento i recorrera letra por letra e imprimira caracter por caracter
for i in diccionario:
    print(f"{i}")

print("\nimprimir cadena sin salto de linea y seguido")
#el elemento i recorrera letra por letra e imprimira caracter por caracter
for i in diccionario:
    print(f"{i}",end=" ")#imprimira cada caracter sin salto de linea pero con un espacio
