'''
Excepciones
'''
print("Excepciones con try: y except")
while True:
    try:
        numero = int(input("Digite un numero: "))
        print(f"la suma es: {numero+10}")
        break
    except:
        print('Ha ocurrido un error ')

print('Programa terminado')


print("\nExcepciones con else y finally")
while True:
    try:
        numero_1 = int(input('Digite un numero: '))
        numero_2 = int(input('Digite el segundo numero:'))
        print(f"la suma es: {numero_1 + numero_2}")
    except:
        print('Ha ocurrido un error')

    else:
        print('Programa terminado exitosamente')
        break
    finally:        #Siempre se va a ejecutar con el try y con el except
        print("iteracion finalizada")
