'''
Hacer un programa para calcular el factorial de un numero positivo
'''

numero=int(input("Digite eun numero: "))
while numero<0:
    print("Error -> El numero debe ser positivo")
    numero=int(input("Digite un numero: "))


#calcular el factorial
factorial=1
for i in range(1,numero+1):
    factorial*=i
#imprimir los numeros
print(f"el factorial es: {factorial}")