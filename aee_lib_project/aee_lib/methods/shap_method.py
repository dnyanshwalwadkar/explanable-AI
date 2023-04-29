from .base_method import ExplanationMethod
from ..explanation import Explanation
import shap

class ShapMethod(ExplanationMethod):
    def __init__(self, model, mode="kernel", background_data=None):
        super().__init__(model)
        self.mode = mode
        self.background_data = background_data

    def explain(self, input_data, **kwargs):
        if self.mode == "kernel":
            return self._explain_kernel(input_data, **kwargs)
        elif self.mode == "deep":
            return self._explain_deep(input_data, **kwargs)
        else:
            raise ValueError("Invalid mode specified. Supported modes are 'kernel' and 'deep'.")

    def _explain_kernel(self, input_data, **kwargs):
        if self.background_data is None:
            raise ValueError("background_data must be provided for kernel mode.")
        
        explainer = shap.KernelExplainer(self.model.predict, self.background_data)
        shap_values = explainer.shap_values(input_data, **kwargs)
        return Explanation(input_data, shap_values)

    def _explain_deep(self, input_data, **kwargs):
        explainer = shap.DeepExplainer(self.model, self.background_data)
        shap_values = explainer.shap_values(input_data, **kwargs)
        return Explanation(input_data, shap_values)
