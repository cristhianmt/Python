'''
escriba un programa deonde cree una lista con los siguientes personajes

nombre: Aragom
clase: Guerrero
raza: Dunadan del Norte


nombre: Gandalf
clase: Mago
raza: Istar



nombre: Legolas
clase: Arquero
raza: Elfo Sidar

'''

personajes=[] #crear lista vacia
print("\nlisa nueva",personajes)
#crear cada personaje
p_1={
"nombre": "Aragom",
"clase": "Guerrero",
"raza": "Dunadan del Norte"
}

p_2={
"nombre": "Gandalf",
"clase": "Mago",
"raza": "Istar"
}

p_3={
"nombre": "Legolas",
"clase": "Arquero",
"raza": "Elfo Sidar"
}

#agregar cada personaje a la list
personajes.append(p_1)
print("\n agregar personaje uno",personajes)

personajes.append(p_2)
print("\n agregar personaje dos",personajes)

personajes.append(p_3)
print("\n agregar personaje tres",personajes)
