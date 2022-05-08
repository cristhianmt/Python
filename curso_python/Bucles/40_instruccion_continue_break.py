# Instrucción continue y break
for i in range(10):
    if i==5:#cuando encuentra la condicion verdadera
        continue#sube e ignora el valor de if, oea ignora el 5 y pasa al 6
    print(i, end=" ")


print("\nuso del break")
for i in range(10):
    if i ==5:
        break
    print(i, end=" ")
print("\nprograma finalizado")