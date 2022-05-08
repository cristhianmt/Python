"""
8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""

from printing_fucnctions import print_model
from printing_fucnctions import show_competed_models as scm
import pizza as p


unprited_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_model(unprited_designs, completed_models)
scm(completed_models)


p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
p.make_pizza(25, 'chorizo', 'queso', 'chile')