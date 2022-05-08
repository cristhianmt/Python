"""
Hacer u programa que pida 2 numeros y se de cuenta cual de ellos es par, o si lo ambos son
"""
a=int(input("Digite el primer valor: "))
b=int(input("Digite el segundo valor: "))
if a%2==0 and b%2==0:
    print("Ambos numero son pares")
elif a%2==0 and b%2!=0:
    print(f"El numero {a} es par")
elif a%2!=0 and b%2==0:
    print(f"El numero {b} es par")
else:
    print("Ambos numeros son  impares")



