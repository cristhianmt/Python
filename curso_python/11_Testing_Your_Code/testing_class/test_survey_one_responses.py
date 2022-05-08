
#Comprobar si la clase AnonymousSurvey funciona
import unittest
from survey import AnonymousSurvey

class Survey_test(unittest.TestCase):
    """Test for the class AnonymousSurvey """
    def test_stores_single_responses(self):
        questions = "What langueage did you first learn to speak? "
        my_survey = AnonymousSurvey(questions)  #llamara a la clase AnonymousSurvey
        my_survey.store_response('Spanish')     #almacenara Spanis en la lista self.responses
        self.assertIn('Spanish', my_survey.responses) #comprobara si Spanish esta en la lista self-responses




if __name__ == '__main__':
    unittest.main()