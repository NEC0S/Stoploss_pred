import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import yaml
import logging
from pathlib import Path
import os

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

def train_model(X, y):
    """Train a machine learning model."""
    logger.info("Training model")
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def save_model(model, output_path):
    """Save the trained model to a file."""
    logger.info(f"Saving model to {output_path}")
    Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_path)

if __name__ == "__main__":
    config = load_config()
    feature_data_path = config['data']['feature_data_path']
    model_output_path = config['model']['model_output_path']

    df = load_data(feature_data_path)
    X = df.drop('target', axis=1)
    y = df['target']

    model = train_model(X, y)
    save_model(model, model_output_path)
