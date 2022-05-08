'''
Realizar un juego para adivinar un numero. para ello generar un numero
aleatorio entre 0-100, y luego ir pidiendo numeros indicando  "es mayor" o es "menor"
segun sea mayor o menor con respecto a N. El proceso termina cuando el usuario acierta
y mostrar el numero de  intentos
'''
#generar un numero aleatorio importando la libreria random()
import random
aleatorio=random.randint(0,100)


print('\t.:Juego adivina el número:. ')
#pedir al usuario un numero
contador=0
while True:
    numero=int(input("Digite un valor: "))
    contador+=1
    if numero>aleatorio:
        print("\tNo es el número, digita un numero menor: ")
    elif numero<aleatorio:
        print("\tNo es el número, digite un numero mayor:")
    elif numero==aleatorio:
        print(f"\n\t¡¡Felicidades acabas de adivinar el numero {aleatorio}!!")
        break
print(f"\tNumero de intentos que te tomo al adivinar: {contador}")