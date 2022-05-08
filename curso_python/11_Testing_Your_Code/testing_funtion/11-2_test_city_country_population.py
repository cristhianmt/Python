import unittest
from City_country_population import City_Country_Population_funtions, City_Country_Population_funtions_2

class Test_City_Country_Population(unittest.TestCase):

    def test_c_c(self):
        formatted_name = City_Country_Population_funtions("Mexico", "Mexico")
        self.assertEqual(formatted_name, f"Mexico Mexico")

    def test_c_c_p(self):
        formatted_name = City_Country_Population_funtions("Mexico", "Mexico", 120000)
        self.assertEqual(formatted_name, f"Mexico Mexico Population: {120000}")

    def test_c_c(self):
        formatted_name = City_Country_Population_funtions_2("Mexico", "Mexico")
        self.assertEqual(formatted_name, f"Mexico Mexico")

    def test_c_c_p(self):
        formatted_name = City_Country_Population_funtions_2("Mexico", "Mexico", 120000)
        self.assertTrue(formatted_name)

if __name__ == '__main__':
    unittest.TestCase