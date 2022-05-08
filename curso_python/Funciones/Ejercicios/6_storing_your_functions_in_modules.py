'''Almacenar las funciones en modulos
Una ventaja de las funciones es la forma en que separan los bloques de
código de su programa principal. Al usar nombres descriptivos para sus
funciones, su programa principal será mucho más fácil de seguir.
Puede ir un paso más allá almacenando sus funciones en un archivo
separado llamado 'module' y luego importando ese módulo a su programa
principal. Una declaración de 'import' le dice a Python que
haga que el código en un módulo esté disponible en el archivo de
programa actualmente en ejecución.
Almacenar sus funciones en un archivo separado le permite ocultar los
detalles del código de su programa y centrarse en su lógica de nivel superior.
También le permite reutilizar funciones en muchos programas diferentes.
Cuando almacena sus funciones en archivos separados, puede compartir esos archivos
con otros programadores sin tener que compartir all su programa.
Saber cómo importar funciones también le permite usar bibliotecas de funciones que otros programadores han escrito.
'''
import pizza

print('Importing an Entire Module, line 24'.upper())
'''A module is a file ending in .py that contains the code you want to import into your
Functions program. Let’s make a module that contains the function make_pizza(). To
make this module, we’ll remove everything from the file pizza.py except the
function'''
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\nImporting Specific Functions, liine 31'.upper())
print('''from module_name import function_name
from module_name import function_0, function_1, function_2''')
from pizza import make_pizza
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza(25, 'chorizo', 'queso', 'chile')


print('''\nUsing as to Give a Function an Alias, line 37'''.upper())
print('from module_name import function_name as fn')
from pizza import make_pizza as mp
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
mp(25, 'chorizo', 'queso', 'chile')


print('''\nUsing as to Give a Module an Alias, line 45'''.upper())
print('import module_name as mn')
import pizza as p
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
p.make_pizza(25, 'chorizo', 'queso', 'chile')


print('''\nimporting all functions in a module  with a *, line 51'''.upper())
print('from module_name import *')
from pizza import *
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza(25, 'chorizo', 'queso', 'chile')


print('''\nstyling functions, line 58'''.upper())
print("def function_name(parameter_0, parameter_1='default value')")
print("""Tener una buena identacion del programa ayudara a enterderle mejor
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
        function body...
""")