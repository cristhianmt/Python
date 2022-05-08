"""
Hacer un rpgrama que pida 3 numeros y determine cual es el mayor
"""
a=int(input("Digite el primer numero: "))
b=int(input("Digite el segundo numero: "))
c=int(input("Digite el tercer numero: "))
if a>b and a>c:
    print(f"El primer numero {a} es mayor")
elif b>a and b>c:
    print(f"El segundo numero {b} es mayor")
elif c>a and c>b:
    print(f"El tercer numero {c} es mayor")