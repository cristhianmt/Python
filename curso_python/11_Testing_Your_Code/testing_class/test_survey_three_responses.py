import unittest
from survey import AnonymousSurvey

class Survey_test(unittest.TestCase):
    def test_stores_single_responses(self):
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_stores_three_responses(self):
        """Test that three individual responses are stored propretly"""
        question = "What lenguages did you first learn to speak? "
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()