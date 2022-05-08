print("\n\nimporting multiple Classes from a module".title())

from car import Car
from electric_car import ElectricCar as EC

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla =EC('tesla', 'roadster', '2021')
print(my_tesla.get_descriptive_name())


print("\n\nimporting an entire module".title())
import car
my_skiline = car.Car('nissan','skilene', 2022)
print(my_skiline.get_descriptive_name())

my_hummer= EC('hummer', "electric", 2021)
print(my_hummer.get_descriptive_name())

print("\n\nImporting All Classes from a Module".title())
print("""Importar todos los modulos no es recomendado por dos razones
Primero, es útil poder leer las declaraciones de importación en la parte 
superior de un archivo y tener una idea clara de las clases que utiliza un programa.
segundo 
Con este enfoque, no está claro qué clases está utilizando desde el módulo. Este enfoque
también puede generar confusión con los nombres en el archivo. Si accidentalmente importa 
una clase con el mismo nombre que otra cosa en su archivo de programa, puede crear errores  
que son difíciles de diagnosticar

Si necesita importar muchas clases desde un módulo, es mejor que
importando todo el módulo y usando la sintaxis 

module_name.ClassName.

No verá todas las clases utilizadas en la parte superior del archivo,
pero verá claramente dónde se utiliza el módulo en el programa. 
También evitará los posibles conflictos de nombres que pueden surgir al 
importar todas las clases en un módulo.
""")