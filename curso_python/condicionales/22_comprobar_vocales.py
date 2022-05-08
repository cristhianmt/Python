"""
Hacer un programa que pida un caracter e indique si es una vocal o no
"""
a=str(input("Digite una letra: ")).lower() #se transfoma en minusculas
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print(f"La palabra {a} es vocal")
else:
     print("No es una vocal")
