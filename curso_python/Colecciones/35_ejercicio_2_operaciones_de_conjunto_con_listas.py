'''
escriba un programa que tenga dos listas y que, a continuacion,
cree las siguientes listas (en las que no deben de haber repeticiones

lista de palabras que aparecen en las dos listas
lista de palabras que aparecen en la primera lista, pero no en la segunda
lista de palabras que aparecen en la segunda lista, pero no en la primera
lista de palabras que aprescan en ambas listas
'''

lista_1=["a","b","c","d","e","f"]
lista_2=["a","b","c","g","h","i"]

#lista de palabras que aparecen en las dos listas
a=set(lista_1)
b=set(lista_2)
union=list(a|b)
print(f"\nlista de palabras que aparecen en las dos listas: {union}")


#lista de palabras que aparecen en la primera lista, pero no en la segunda
solo_a=list(a-b)
print(f"\ndiferencia de  la lista a sin repeticion: {solo_a}")


solo_b=list(b-a)
print(f"""\nlista de palabras que aparecen en la segunda lista, pero no en la primera: {solo_b}""")

interseccion=list(a&b)
print(f"""\nlista de palabras que aprescan en ambas listas: {interseccion}""")
