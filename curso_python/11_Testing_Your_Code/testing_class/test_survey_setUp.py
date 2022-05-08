"""
setUp() metodo se usa cuando tenemos varios valores y nos facilita el uso
ya que no agregamos los valores uno por uno

"""

import unittest
from survey import AnonymousSurvey

class Survey_test(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """Create a survey and set of responses for use in all test methods"""
        question = "What lenguage did you first lear to speak? "
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Spanish','English','Mandarin']


    def test_store_single_responses(self):
        """Test that a single response is stored propetly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)


    def test_Three_responses(self):
        """Test that three individual responses are steored propetly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()