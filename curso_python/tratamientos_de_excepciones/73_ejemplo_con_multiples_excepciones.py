#Ecepciones

def dividir():
    while True:
        try:
            num_1 = float(input('Digite un numero: '))
            num_2 = float(input('Difite un numero: '))
            resultado = num_1 / num_2
            print(f"El resultado es: {resultado:.2f}")
        except ValueError:
            print("Error: Digite correctamente los valores numericos")
        except ZeroDivisionError:
           print("Error: No se puede dividir entre 0")
        else:
            break

dividir()
