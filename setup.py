from setuptools import setup, find_packages

# pip install -e .
setup(
  name="systemt_ai",
  version="0.1",
  packages=find_packages(),
  install_requires=[
    "python-dotenv",
    "psycopg2-binary",
    "pandas",
    "numpy",
    "scikit-learn",
    "xgboost",
    "tensorflow_decision_forests",
    "boto3",
    "shap",
    "matplotlib",
    "mysql-connector-python"
  ],
  author="Hai M Nguyen",
  description="SystemT-AI is a project that uses Machine Learning to predict various market signals.",
)