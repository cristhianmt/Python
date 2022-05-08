#condicionales
"""
son de las estructuras de control mas importante
sirven para comparar dos valores
verdadero o falso
"""

numero=int(input("Digite un valor: "))

if numero>0: #los dos puento significa que termina la condicion
    print("El numero es positivo") #seran las instrucciones a ejecutar
    """no utilizan {} con en otros programas ya que utilizan 
        identacion que son los espacios de despues de la condicion"""
elif numero==0: #caso contrario de if
    print("el numero es 0")
else:
    print(("numero negativo"))

