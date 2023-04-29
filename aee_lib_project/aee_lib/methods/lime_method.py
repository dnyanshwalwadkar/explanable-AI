from .base_method import ExplanationMethod
from ..explanation import Explanation
from lime import lime_image, lime_text
from lime.wrappers.scikit_image import SegmentationAlgorithm

class LimeMethod(ExplanationMethod):
    def __init__(self, model, mode="image"):
        super().__init__(model)
        self.mode = mode

    def explain(self, input_data, **kwargs):
        if self.mode == "image":
            return self._explain_image(input_data, **kwargs)
        elif self.mode == "text":
            return self._explain_text(input_data, **kwargs)
        else:
            raise ValueError("Invalid mode specified. Supported modes are 'image' and 'text'.")

    def _explain_image(self, input_data, num_samples=1000, num_features=5, **kwargs):
        explainer = lime_image.LimeImageExplainer(verbose=True)
        segmenter = SegmentationAlgorithm('quickshift', kernel_size=4, max_dist=200, ratio=0.2)
        explanation = explainer.explain_instance(input_data, self.model.predict, top_labels=5, hide_color=0,
                                                 num_samples=num_samples, segmentation_fn=segmenter, **kwargs)
        return Explanation(input_data, explanation.get_image_and_mask(num_features))

    def _explain_text(self, input_data, num_samples=1000, num_features=5, **kwargs):
        explainer = lime_text.LimeTextExplainer(class_names=self.model.classes_)
        explanation = explainer.explain_instance(input_data, self.model.predict_proba, num_features=num_features, 
                                                 num_samples=num_samples, **kwargs)
        return Explanation(input_data, explanation.as_list())
