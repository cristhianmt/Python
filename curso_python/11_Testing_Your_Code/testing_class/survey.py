# A Class to test
#Clase de escuesta anonima
class AnonymousSurvey:
    """collect anonymmous answer to a survey question"""
    def __init__(self, question):
        """Store  a question an preparate  to store reponses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show to survey question"""
        print(self.question)

    def store_response(self, new_response):
        """Store a single responses to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have benne given"""
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")