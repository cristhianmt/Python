"""
UNIT TESTS AND TEST CASES
A PASSING TEsT

Crearemos un programa que ponga aprueba el programa
y diga si es ocrrecto su funcionamiento
"""


import unittest  #importaremos unittest para automatizar pruebas
from name_funtion import get_formatted_name #importamos el archivo que queremos hacerle la prueba

class NameTestCase(unittest.TestCase): #la clase Name_Test_case heredara el metodo
    """Test for 'name_funtion.py'"""

            #Metodo
    def test_first_last_name(self):
        "Do names like 'Janis Joplin ' word?"
        formatted_name = get_formatted_name('janis', 'joplin') #Mandaremos los objetos a la funcion
        self.assertEqual(formatted_name, 'janis joplin')
        '''Si el metodo de afrimacion asserEqual coincide con formatted_name, enotonces esta funcionando correctaente'''

if __name__== '__main__':  # __name__ == '__main__' se utiliza para ejecutar las pruebas
    unittest.main()