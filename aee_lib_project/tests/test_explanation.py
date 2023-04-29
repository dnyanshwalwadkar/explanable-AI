import unittest
from autoencoding_explanations.explanation import Explanation

class TestExplanation(unittest.TestCase):
    def test_initialization(self):
        input_data = "input_data_example"
        explanation_data = "explanation_data_example"
        explanation = Explanation(input_data, explanation_data)
        
        self.assertEqual(explanation.get_input_data(), input_data)
        self.assertEqual(explanation.get_explanation_data(), explanation_data)

    # Add more test functions as needed

if __name__ == "__main__":
    unittest.main()
