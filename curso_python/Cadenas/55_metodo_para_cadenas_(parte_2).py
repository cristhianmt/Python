#cadena de caracteres

print("""\nretomara un valor boleano 
esto quiere decir que dira si comienza con la primera palabra""")
cadena = "Hola mundo".startswith("H")
print(cadena)



print("""\nretomara un valor boleano 
esto quiere decir que dira si termina con la ultima palabra""")
cadena = "Hola mundo".endswith("o")
print(cadena)

print("""\nte retomara en forma de lista 
cada vez que encuentre un espacio""")
cadena = "Hola mundo como estas".split()
print(cadena)


print("""\nte retomara en forma de lista 
cada vez que encuentre un espacio o cada ves que encuentre "x" """)
cadena = "Hola*mundo*como*estas cristhian".split("*")
print(cadena)


print("""\nseparar los elementos con un caracter con el metodo join""")
cadena = "-".join("Hola mundo como estas")
print(cadena)

print("""\neliminar los espacio """)
cadena = "               mundo                  ".strip()
print(cadena)

print("""\neliminar los caracteres o simbolos """)
cadena = "***************mundo**************".strip("*")
print(cadena)

print("""\nremplazar valors por otro""")
cadena = "hola mundo".replace("o","0")
print(cadena)