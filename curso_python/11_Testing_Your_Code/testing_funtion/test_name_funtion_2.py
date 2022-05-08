import unittest
from name_funtion_2 import get_formatted_name

class Name_Test_Case(unittest.TestCase):
    def test_first_last(self):
        formatted_name = get_formatted_name('cristhian', 'martinez')
        self.assertEqual(formatted_name, 'Cristhian Martinez')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

    def test_first_middle_last(self):
        formatted_name = get_formatted_name('maria', 'galicia','fernanda')
        self.assertEqual(formatted_name, 'Maria Fernanda Galicia')

if __name__== '__main__':  # __name__ == '__main__' se utiliza para ejecutar las pruebas
    unittest.main()
