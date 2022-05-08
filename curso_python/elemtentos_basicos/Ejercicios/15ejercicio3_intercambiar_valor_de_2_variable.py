#Hacer un programa para intercambair el valor de dos variables

a=float(input("\nDigite a: "))
b=float(input("\nDigite b: "))

a,b=b,a

print(f"El resultado a es: {a}")
print(f"El resultado b es: {b}")