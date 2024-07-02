import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import joblib
import yaml
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_path='config/config.yaml'):
    """Load configuration from a YAML file."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def load_data(file_path):
    """Load processed data from a file."""
    logger.info(f"Loading data from {file_path}")
    return pd.read_csv(file_path)

def load_model(model_path):
    """Load a trained model from a file."""
    logger.info(f"Loading model from {model_path}")
    return joblib.load(model_path)

def evaluate_model(model, X_test, y_test):
    """Evaluate the model and print metrics."""
    logger.info("Evaluating model")
    y_pred = model.predict(X_test)
    logger.info(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    logger.info(classification_report(y_test, y_pred))

if __name__ == "__main__":
    config = load_config()
    test_data_path = config['data']['test_data_path']
    model_path = config['model']['model_output_path']

    df = load_data(test_data_path)
    X_test = df.drop('target', axis=1)
    y_test = df['target']

    model = load_model(model_path)
    evaluate_model(model, X_test, y_test)
