"""
11-3. Employee: Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.
Write a test case for Employee. Write two test methods, test_give_default
_raise() and test_give_custom_raise(). Use the setUp() method so you don’t
have to create a new employee instance in each test method. Run your test
case, and make sure both tests pass.
"""

import unittest
from employees import Employees

class Employees_test(unittest.TestCase):

    def setUp(self):
        self.cristhian = Employees('Cristhian','Martinez',65000)

    def test_given_default_raise(self):
        self.cristhian.give_raise()
        self.assertEqual(self.cristhian.salary, 70000)

    def test_given_custom_raise(self):
        self.cristhian.give_raise(6000)
        self.assertEqual(self.cristhian.salary, 71000)

if __name__ == '__main__':
    unittest.main()