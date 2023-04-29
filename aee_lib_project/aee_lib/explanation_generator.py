from .utils.visualization import (visualize_lime_explanation,
                                  visualize_shap_explanation,
                                  visualize_integrated_gradients)

class ExplanationGenerator:
    def __init__(self, model, explanation_method):
        self.model = model
        self.explanation_method = explanation_method

    def generate_explanation(self, input_data, **kwargs):
        explanation = self.explanation_method.explain(input_data, **kwargs)
        return explanation

     def visualize_explanation(self, explanation, **kwargs):
            explanation_data = explanation.get_explanation_data()

        if isinstance(self.explanation_method, LimeMethod):
            visualize_lime_explanation(explanation.get_input_data(), explanation_data, **kwargs)
        elif isinstance(self.explanation_method, ShapMethod):
            visualize_shap_explanation(explanation.get_input_data(), explanation_data, **kwargs)
        elif isinstance(self.explanation_method, IntegratedGradientsMethod):
            visualize_integrated_gradients(explanation.get_input_data(), explanation_data)
        else:
            # Add visualization calls for other explanation methods as needed
            pass
