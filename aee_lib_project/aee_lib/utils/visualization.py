import matplotlib.pyplot as plt
import numpy as np

def visualize_lime_explanation(input_data, explanation_data, num_features=5, positive_only=False):
    image, mask = explanation_data
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    ax1.imshow(input_data)
    ax1.set_title("Input Image")
    ax1.axis("off")

    ax2.imshow(input_data)
    ax2.imshow(mask, alpha=0.5, cmap="jet" if positive_only else "coolwarm")
    ax2.set_title(f"LIME Explanation (Top {num_features} Features)")
    ax2.axis("off")

    plt.show()

def visualize_shap_explanation(input_data, explanation_data, class_index=None):
    if class_index is None:
        class_index = np.argmax(np.sum(np.abs(explanation_data), axis=-1))

    shap_values = explanation_data[class_index]

    plt.imshow(input_data)
    plt.imshow(shap_values, cmap="coolwarm", alpha=0.7)
    plt.title(f"SHAP Explanation (Class {class_index})")
    plt.axis("off")
    plt.show()

def visualize_integrated_gradients(input_data, integrated_gradients):
    attribution_map = np.sum(np.abs(integrated_gradients), axis=-1)
    normalized_map = attribution_map / np.max(attribution_map)

    plt.imshow(input_data)
    plt.imshow(normalized_map, cmap="coolwarm", alpha=0.7)
    plt.title("Integrated Gradients Explanation")
    plt.axis("off")
    plt.show()

# Add other visualization functions as needed
