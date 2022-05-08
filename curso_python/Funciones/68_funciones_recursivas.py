#Funciones recursivas
'''
Son funciones que se llaman asi mismas
osea que es como un buble que se manda a llamar repetidamente
'''

def cuenta_regresiva(num):
    if num>0:
        print(num)
        cuenta_regresiva(num - 1)
    else:
        print('Booooom !!!')

cuenta_regresiva(10)