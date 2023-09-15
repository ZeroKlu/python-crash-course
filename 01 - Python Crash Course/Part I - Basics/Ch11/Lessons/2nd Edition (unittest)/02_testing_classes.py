# Available Asserts:
#      ASSERT                          VERIFIES
#   ------------------------------------------------
#   assertEqual(x, y)            x == y
#   assertNotEqual(x, y)         x != y
#   assertTrue(x)                x == True
#   assertFalse(x)               x == False
#   assertIn(item, list)         item is in list
#   assertNotIn(item, list)      item is not in list

import unittest

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """Show the survey question."""
        print(self.question)
        
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
        
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

def language_survey():
    # Define a question, and make a survey.
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)

    # Show the question, and store responses to the question.
    my_survey.show_question()
    print("Enter 'q' at any time to quit.\n")
    while True:
        response = input("Language: ")
        if response == "q":
            break
        my_survey.store_response(response)

    # Show the survey results.
    print("\nThank you to everyone who participated in the survey!")
    my_survey.show_results()
    
class AnonymousSurveyTestCase(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
    # The setUp method allows you to create your test case variables once and 
    #     use them globally in all your unit tests
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "Mandarin"]

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

def main():
    print("Chapter 11:\nExercise 2 - Testing a Class\n")
    unittest.main()
    
if __name__ == "__main__":
    main()
