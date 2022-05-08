#Metodos para cadenas
cadena = "HOLA CRISTHIAN".lower()#convierte la cadena a minusculas
print(cadena)

print("\nconvierte la primera letra a mayuscula linea 6")
cadena = "\nhola cristhian".capitalize()
print(cadena)

print("\nconvierte las primera letras de cada palabra a mayuscula linea 10")
cadena = "\nhola cristhian".title()
print(cadena)

print("\ncuantas veces aparece un elemento linea 14")
cadena = "hola cristhian".count('a')
print(cadena)


print("\ncuantas veces aparce una palabra linea 19")
cadena = "hola cristhian hola hola".count("hola")
print(cadena)


print("\nbuscar donde esta el indice donde aparece una letra linea 24")
cadena = "hola cristhian".find("o")
print(cadena)

print("\nbuscar donde esta el indice donde aparece una palabra completa linea 28")
cadena = "hola cristhian hola".find("cristhian")
print(cadena)


print("\nbuscar donde esta el indice donde aparece la ultima palabra completa linea 33")
cadena = "hola cristhian hola cristhian".rfind("cristhian")
print(cadena)

print("\nsi toda esta tiene solo valores numericos linea 37")
cadena = "123456789123456789".isdigit()
print(cadena)


print("\nsi la cadena esta tiene solo caracteres alfabeticos linea 42")
cadena = "abcedeghij".isalpha()
print(cadena)

print("\nsi la cadena esta tiene solo valores alfanumericos linea 46")
cadena = "123456abcdefgh".isalnum()
print(cadena)

print("\nii la cadena esta tiene solo valores numericos linea 50")
cadena = "123456789123456789".isdigit()
print(cadena)


print("\nsi toda la cadena esta en mayuscula linea 55")
cadena = "HOLA COMO ESTAS".isupper()
print(cadena )

print("\nsi toda la cadena esta en miniscula linea 59")
cadena = "hola como estas".islower()
print(cadena )

print("\nsi una palabra en la caden es un titulo linea 62")
cadena = "Hola Como Estas".istitle()
print(cadena )

print("\nsi toda la cadena esta conformada con puros espacios linea 66")
cadena = "             ".isspace()
print(cadena )


