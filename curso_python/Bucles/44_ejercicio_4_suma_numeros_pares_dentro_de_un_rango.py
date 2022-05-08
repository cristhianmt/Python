'''
Hacer un programa para sumar numeros pares dentro de un rango

suma de numeros pares del 2 al 30
suma=240
'''

#Pedir al usuario los rangos
valor_1=int(input("Digite el principio del rango : "))
valor_2=int(input("Digite el final del rango: "))
suma=0
#sumar numeros pares con el ciclo for y range
for i in range(valor_1,valor_2+1):
    if i%2==0:# si el numero es par
        suma+=i

print(f"la suma de numeros pares es es: {suma}")

