import tensorflow as tf
import numpy as np
from .base_method import ExplanationMethod
from ..explanation import Explanation

class IntegratedGradientsMethod(ExplanationMethod):
    def __init__(self, model, baseline=None):
        super().__init__(model)
        self.baseline = baseline

    def explain(self, input_data, num_steps=50, **kwargs):
        if self.baseline is None:
            self.baseline = np.zeros_like(input_data)

        if self.baseline.shape != input_data.shape:
            raise ValueError("Baseline shape must match input_data shape.")

        integrated_gradients = self._integrated_gradients(input_data, num_steps=num_steps, **kwargs)
        return Explanation(input_data, integrated_gradients)

    def _integrated_gradients(self, input_data, num_steps=50, **kwargs):
        input_dtype = input_data.dtype
        input_data = tf.cast(input_data, tf.float32)
        self.baseline = tf.cast(self.baseline, tf.float32)
        
        input_shape = input_data.shape
        input_data = tf.expand_dims(input_data, axis=0)
        self.baseline = tf.expand_dims(self.baseline, axis=0)

        interpolated_inputs = [
            self.baseline + (float(step) / num_steps) * (input_data - self.baseline)
            for step in range(num_steps + 1)
        ]

        with tf.GradientTape(persistent=True) as tape:
            tape.watch(interpolated_inputs)
            predictions = [self.model(interpolated_input, training=False) for interpolated_input in interpolated_inputs]

        gradients = [tape.gradient(prediction, interpolated_input)
                     for prediction, interpolated_input in zip(predictions, interpolated_inputs)]
        
        del tape

        avg_gradients = np.mean(gradients, axis=0)
        integrated_gradients = (input_data - self.baseline) * avg_gradients

        return integrated_gradients.numpy().astype(input_dtype).reshape(input_shape)
