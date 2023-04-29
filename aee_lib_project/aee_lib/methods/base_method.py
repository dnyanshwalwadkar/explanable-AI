from abc import ABC, abstractmethod

class ExplanationMethod(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def explain(self, input_data, **kwargs):
        pass
