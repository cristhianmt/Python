#Conjuntos

a=set((1,2,3))
b=set((3,4,5,6))

print(a==b)
print(len(a))


a=set((1,2,3))
b=set((3,4,5,6))
c=a|b#unir dos conjuntos
print("\nunir dos conjuntos",c)

a=set((1,2,3))
b=set((3,4,5,6))
c=a&b
print("\ninterseccion de dos conjuntos",c)

a=set((1,2,3))
b=set((3,4,5,6))
c=a-b
print("\ndifrecencia del conjunto a",c)

a=set((1,2,3))
b=set((3,4,5,6))
c=b-a
print("\ndifrecencia del conjunto B",c)

a=set((1,2,3))
b=set((3,4,5,6))
c=a^b
print("\ndifrecencia simetrica de ambos conjuntos",c)

a=set((1,2,3))
b=set((3,4,5,6))
c={1,2,3,4,5}
print("\nsi es que a es un subconjunto del conjunto c",a.issubset(c))

a=set((1,2,3))
b=set((3,4,5))
c={1,2,3,4,5,6}
print("\nsi es que b es un subconjunto del conjunto c",b.issubset(c))

a=set((1,2,3))
b=set((3,4,5))
c={1,2,3,4,5,6}
print("\nc es un super conjunto",c.issuperset(a))


a=set((1,2,3))
b=set((3,4,5))
c={1,2,3,4,5,6}
print("\na no comparte ningun elemento de b",a.isdisjoint(b))#no comparte elemntos en comun, pero si comparte


a=frozenset({1,2,3}) #conjunto inmutable, es decir no podriamos cambiar cualquier elemento
b={3,4,5}
c={1,2,3,4,5,6}
print("\nfrozenset, significa que ya no se puede modificar cualquier elemento")

