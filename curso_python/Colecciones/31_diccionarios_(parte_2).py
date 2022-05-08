#Diccionario

equipo={
    "Red bull":{"max":33},
    "ferrari":{"vettel":5},
    "mclaren":{"sainz":55}
}
print("para saber que no existe un elemento se puede utilizar el get")
print(equipo.get("ferrari","no existe dentro del diccionario:"))


print("\nhace una busqueda:", "ferrari" in equipo)

print("\nmostrar todas las claves del diccionario:", equipo.keys())


print("\nmostrar todas los elemtos del diccionario:", equipo.values())


print("\nmostrar todas las claves del diccionario:", equipo.items())


print("\nmostrar cuantas claves hay en el diccionario:", len(equipo))

print("\neliminar todas las claves del diccionario:", equipo.clear())