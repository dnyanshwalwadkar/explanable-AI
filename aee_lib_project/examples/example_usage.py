from autoencoding_explanations.explanation_generator import ExplanationGenerator
from autoencoding_explanations.methods import LimeMethod, ShapMethod, IntegratedGradientsMethod
import your_deep_learning_model

# Load your deep learning model
model = your_deep_learning_model.load_model("path/to/your/model")

# Load input data for explanation
input_data = your_deep_learning_model.load_input_data("path/to/your/input/data")

# Initialize explanation generator with LIME method
lime_explanation_generator = ExplanationGenerator(model, LimeMethod)

# Generate LIME explanation
lime_explanation = lime_explanation_generator.explain(input_data)
lime_explanation_generator.visualize_explanation(lime_explanation)

# Initialize explanation generator with SHAP method
shap_explanation_generator = ExplanationGenerator(model, ShapMethod)

# Generate SHAP explanation
shap_explanation = shap_explanation_generator.explain(input_data)
shap_explanation_generator.visualize_explanation(shap_explanation)

# Initialize explanation generator with Integrated Gradients method
integrated_gradients_explanation_generator = ExplanationGenerator(model, IntegratedGradientsMethod)

# Generate Integrated Gradients explanation
integrated_gradients_explanation = integrated_gradients_explanation_generator.explain(input_data)
integrated_gradients_explanation_generator.visualize_explanation(integrated_gradients_explanation)
