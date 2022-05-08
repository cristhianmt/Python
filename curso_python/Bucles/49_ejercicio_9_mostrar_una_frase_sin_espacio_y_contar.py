'''
Hacer un programa donde el usuario ingrese una frase, se le
devolvera la misma frase pero sin espacios en blaco y ademas un
 contador de cuantos caracteres tiene la frase (son contar los espacios en blnco)

Ejemplo
frase: Hola que tal
frase fina: Holaquetal?
num de caracteres: 11
'''
#pedir al usuario la frase
palabra=input("Digite la frase: ")
palabra_2 = ""
for i in palabra:
    if i != " ":
        palabra_2 += i
palabra = palabra_2
print(f"Frase final {palabra}")
print(f"el numero de caracteres: {len(palabra)}")