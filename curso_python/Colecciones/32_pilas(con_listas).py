
'''
Pilas son estrestucturas de datos
pero en python no estan pero se pueden simular con listas
primero en entrar ultimo en salir
'''

pila=[1,2,3]
pila.append(4)
pila.append(5)
print(pila)

#sacar elemento al final
print("\nsacar el ultimo elemento")
n=pila.pop()
print(f"sacando el elemento {n} de: ",pila)


#