import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            pass

root_dir = "aee_lib_project"

dirs = [
    os.path.join(root_dir, "aee_lib"),
    os.path.join(root_dir, "aee_lib", "methods"),
    os.path.join(root_dir, "aee_lib", "utils"),
    os.path.join(root_dir, "tests"),
    os.path.join(root_dir, "examples")
]

for directory in dirs:
    create_directory(directory)

files = [
    os.path.join(root_dir, "aee_lib", "__init__.py"),
    os.path.join(root_dir, "aee_lib", "explanation_generator.py"),
    os.path.join(root_dir, "aee_lib", "explanation.py"),
    os.path.join(root_dir, "aee_lib", "methods", "__init__.py"),
    os.path.join(root_dir, "aee_lib", "methods", "base_method.py"),
    os.path.join(root_dir, "aee_lib", "methods", "lime_method.py"),
    os.path.join(root_dir, "aee_lib", "methods", "shap_method.py"),
    os.path.join(root_dir, "aee_lib", "methods", "integrated_gradients_method.py"),
    os.path.join(root_dir, "aee_lib", "utils", "__init__.py"),
    os.path.join(root_dir, "aee_lib", "utils", "visualization.py"),
    os.path.join(root_dir, "README.md"),
    os.path.join(root_dir, "requirements.txt")
]

for file_path in files:
    create_file(file_path)
