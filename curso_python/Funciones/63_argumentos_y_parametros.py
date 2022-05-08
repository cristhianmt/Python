#Argumentos y parametros

def resta(num1, num2): #recibee los parametros
    return num1 - num2

print(resta(5,4))# Paso de argumentos por pocision, el primer parametro se guarda en num1 y el segundo en num2


print('\npodemos enviar argumentos por nombres')

def resta_1 (num_1,num_2):
    return (num_2-num_1)
print(resta_1(num_2=4, num_1=2))

