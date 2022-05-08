'''
Lanzar nuestras propias excepciones
'''

def verificando_edad(edad):
    if edad < 0:
        raise ValueError ('La edad no puede ser negativa')
    elif edad < 18:
        print('Eres muy joven')
    elif edad < 30:
        print('Eres joven')
    elif edad < 50:
        print('Eres maduro')

edad =int(input("Digite sus edad: "))
try:
    verificando_edad(edad)
except ValueError as Edad_negativa:
    print(Edad_negativa)

print('Programa terminado')