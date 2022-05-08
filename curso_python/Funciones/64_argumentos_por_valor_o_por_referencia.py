#Argumentos por valor o por referencia


#Argumentos por valor
def doblar_valor(numero):
    numero *=2
    print(numero)

n=5             #el argumento por valor pasa la copia de un numero por defecto pero sin modificar el original
doblar_valor(n) #retorna el valor de la copia modificado
print(n) #imprime el valor original


print("\nal igual podemos modificar el valor original")

def doblar_valor_1(numero_1): # 5. saca el valor y lo envia al argumetno
    numero_1*=2 #3. el parametro realiaza la operacion
    return numero_1 #4. retona el valor

num = 3 # 1. asignamos valores
n = doblar_valor_1(num) #2. el argumento pasa al parametro 6.recive el valor del parametro y lo guarna en una variable
print(n) #7. imprimimos el valor modificado


print('''\nArgumentos por referencia
son colecciones por colecciones, listas, sets diccionarios esos se pasan por argumentos
por referencia y es automatico''')

def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i]*=2

n = [5,10,15,20]
doblar_valores(n)
print('\nValor por referencia, pero modificando la variables original\n',n)

def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i]*=2

n = [5,10,15,20]
doblar_valores(n[:]) #El valor original no se modificara solo la copia y esto se hace mediante [;]
print('\nSe puede usar el argumetento por referencia sin modificar el valor real\n',n)